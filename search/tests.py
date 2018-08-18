from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Items
from .serializers import ItemsSerializer

# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_item(name, lat, lng, item_url, img_urls):
        if name != "":
            Items.objects.create(
                item_name=name,
                lat=lat,
                lng=lng,
                item_url=item_url,
                img_urls=img_urls
            )

    def setUp(self):
        # add test data
        self.create_item("bike", 10, 10, "bike.com", "img-url.com")
        self.create_item("camera", 10, 10, "bike.com", "img-url.com")
        self.create_item("wings", 10, 10, "bike.com", "img-url.com")
        self.create_item("blender", 10, 10, "bike.com", "img-url.com")


class GetAllitemsTest(BaseViewTest):

    def test_get_all_items(self):
        """
        This test ensures that all items added in the setUp method
        exist when we make a GET request to the items/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("items-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Items.objects.all()
        serialized = ItemsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
# Create your tests here.
