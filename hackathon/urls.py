from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="HACKATHON PERIFERIA 2023 - API",
        default_version='v1',
        description="API Documentation",
        terms_of_service="https://hackathon-periferia-2023-daniel-dorado.onrender.com/",
        contact=openapi.Contact(email="dpdaniel@unicauca.edu.co"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('mutants.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]