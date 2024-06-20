from rest_framework import viewsets, permissions
from .models import PantryItem
from .serializers import PantryItemSerializer

class PantryItem(viewsets.ModelViewSet):
    queryset = PantryItem.objects.all()
    serializer_class = PantryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)