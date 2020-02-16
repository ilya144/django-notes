from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Category
from .validators import UserEmailValidator


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True}}

        validators = [
            UserEmailValidator(
                queryset=User.objects.all(),
                field='email',
            )
        ]

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            # is_staff=validated_data['is_staff']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)

        new_password = validated_data.get('password', None)
        if new_password:
            instance.set_password(validated_data['password'])
        
        instance.save()
        return instance
