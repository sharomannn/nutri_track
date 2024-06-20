from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="NutriPlanner API",
        default_version='v1',
        description="API документация для NutriPlanner",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@nutriplanner.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pantry/', include('pantry.urls')),
    path('api-auth/', include('rest_framework.urls')),  # Для аутентификации
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', include('nutri_planner.frontend.urls')),  # Добавлено для фронтенда
]