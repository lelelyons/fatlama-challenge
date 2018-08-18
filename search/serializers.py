from rest_framework import serializers
from .models import Items

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('item_name', 'lat', 'lng', 'item_url', 'img_urls')
