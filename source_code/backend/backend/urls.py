"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from rest_framework_swagger.views import get_swagger_view

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="UHMS Ticketing APIs",
      default_version='v1',
      description="Uwata Hospital Management System Ticketing APIS",
      terms_of_service="https://uwatahospital.com/terms/",
      contact=openapi.Contact(email="emasanga@aifrruislabs.com"),
      license=openapi.License(name="UHMS License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Index With Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Rest API Auth Urls
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Ticketing Backend Api v1 urls
    re_path(r'^api/v1/', include('ticketing.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

