
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect

schema_view = get_schema_view(
    openapi.Info(
    title = "CrudAPI",
    default_version = 'v1',
    description = "API for user registration, authentication and task management using Django REST framework.",
    contact = openapi.Contact(email="cheruiyotevans646@gmail.com"),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)


urlpatterns = [
    path('', lambda request: redirect('swagger/')),
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
