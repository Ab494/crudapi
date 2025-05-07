from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterView
from rest_framework.urlpatterns import format_suffix_patterns
from . views import user_profile
from . views import UserProfileView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', user_profile, name='user_profile'),
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
]
