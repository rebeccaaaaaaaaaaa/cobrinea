from rest_framework import viewsets

from .serializers import ItemSerializer
from .models import Item

class ItemSerializerViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('name')
    serializer_class = ItemSerializer