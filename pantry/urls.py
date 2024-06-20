from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PantryItem

app_name = 'pantry'

router = DefaultRouter()
router.register(r'items', PantryItem, basename='pantry_items')

urlpatterns = [
    path('', include(router.urls)),
]