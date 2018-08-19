from django.urls import path
from .views import ListItemsView

urlpatterns = [
    path('search/', ListItemsView.as_view(), name='search')
]
