from rest_framework import serializers
from .models import PantryItem

class PantryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantryItem
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']