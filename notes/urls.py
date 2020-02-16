from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', views.register_view),
    path('login', views.login_view),
    path('logout', views.logout_view),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]