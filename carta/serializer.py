from rest_framework import serializers
from .models import Item, Category


class Item_serializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'