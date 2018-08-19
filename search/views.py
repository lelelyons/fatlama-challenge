from rest_framework import generics
from .models import Items, filter_items
from .serializers import ItemsSerializer

NO_ITEMS =20

class ListItemsView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
        return filter_items(self.request.query_params, NO_ITEMS)

