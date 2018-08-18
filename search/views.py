from rest_framework import generics
from .models import Items
from .serializers import ItemsSerializer

import pdb
class ListItemsView(generics.ListAPIView):
    queryset = Items.objects.all()
    pdb.set_trace()
    serializer_class = ItemsSerializer

