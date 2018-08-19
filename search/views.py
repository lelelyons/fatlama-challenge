from rest_framework import generics
from .models import Items
from .utils import filter_items
from .serializers import ItemsSerializer

NO_ITEMS = 20

class ListItemsView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
        items = Items.objects.all()
        return filter_items(items, self.request.query_params, NO_ITEMS)

