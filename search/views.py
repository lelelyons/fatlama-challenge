from rest_framework import generics
from .models import Items
from .serializers import ItemsSerializer

import pdb
class ListItemsView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
            queryset = Items.objects.all()
            return self.filterItems(queryset)

    def filterItems(self, queryset):
        search_term = self.request.query_params.get('searchTerm', None)
        lat = self.request.query_params.get('lat', None)
        lng = self.request.query_params.get('lng', None)

        if search_term is not None:
            queryset = queryset.filter(item_name__contains=search_term)
        return queryset
