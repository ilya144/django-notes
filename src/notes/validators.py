from rest_framework.validators import BaseUniqueForValidator, qs_filter, qs_exists
from rest_framework.exceptions import ValidationError
from rest_framework.utils.representation import smart_repr


class UserEmailValidator(BaseUniqueForValidator):
    """
    I just took BaseUniqueForValidator and remove date_field
    everywhere

    This validator replace SQL unique key,
    just for using default Django User model
    """
    def __init__(self, queryset, field, message=None):
        self.queryset = queryset
        self.field = field
        self.message = message or self.message

    def set_context(self, serializer):
        """
        This hook is called by the serializer instance,
        prior to the validation call being made.
        """
        self.field_name = serializer.fields[self.field].source_attrs[-1]

        self.instance = getattr(serializer, 'instance', None)

    def enforce_required_fields(self, attrs):
        """
        The `UniqueFor<Range>Validator` classes always force an implied
        'required' state on the fields they are applied to.
        """
        missing_items = {
            field_name: self.missing_message
            for field_name in [self.field]
            if field_name not in attrs
        }
        if missing_items:
            raise ValidationError(missing_items, code='required')

    
    def filter_queryset(self, attrs, queryset):
        value = attrs[self.field]

        filter_kwargs = {}
        filter_kwargs[self.field_name] = value
        return qs_filter(queryset, **filter_kwargs)
    
    def __call__(self, attrs):
        self.enforce_required_fields(attrs)
        queryset = self.queryset
        queryset = self.filter_queryset(attrs, queryset)
        queryset = self.exclude_current_instance(attrs, queryset)
        if qs_exists(queryset):
            raise ValidationError({
                self.field: 'A user with that email already exists.'
            }, code='unique')

    def __repr__(self):
        return '<%s(queryset=%s, field=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.queryset),
            smart_repr(self.field)
        )