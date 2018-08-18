from django.urls import path
from .views import ListItemsView


urlpatterns = [
    path('items/', ListItemsView.as_view(), name="items-all")
]
