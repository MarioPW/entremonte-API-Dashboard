from rest_framework import viewsets
from .serializer import Item_serializer, Category_serializer
from .models import Item, Category

class Item_view(viewsets.ModelViewSet):
    serializer_class = Item_serializer
    queryset = Item.objects.filter(available=True)

class Category_view(viewsets.ModelViewSet):
    serializer_class = Category_serializer
    queryset = Category.objects.filter(available=True)