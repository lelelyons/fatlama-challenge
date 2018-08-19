from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Items, calculate_distance, closest_items
from .serializers import ItemsSerializer

import pdb
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_item(name, lat, lng, item_url, img_urls):
        Items.objects.create(
            item_name=name,
            lat=lat,
            lng=lng,
            item_url=item_url,
            img_urls=img_urls
        )

    def setUp(self):
        self.create_item('bike', 10, 10, 'bike.com', 'img-url.com')
        self.create_item('camera', 55, 30, 'camera.com', 'img-url.com')
        self.create_item('wings', 20, 14, 'wings.com', 'img-url.com')
        self.create_item('blender', 12, 40, 'blender.com', 'img-url.com')

class GetItemsTest(BaseViewTest):

    def test_search_with_no_params(self):
        response = self.client.get(reverse('search'))

        expected = Items.objects.all()
        serialized = ItemsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_with_search_term(self):
        response = self.client.get(reverse('search'), { 'searchTerm': 'bike' })

        expected = Items.objects.get(item_name='bike')
        serialized = ItemsSerializer(expected)
        self.assertEqual(response.data[0], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_with_lat_and_lng_no_search_term(self):
        response = self.client.get(reverse('search'), { 'lat': '20', 'lng': '14' })

        expected = Items.objects.get(lat=20, lng=14)
        serialized = ItemsSerializer(expected)
        self.assertEqual(response.data[0], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_with_all_params(self):
        response = self.client.get(reverse('search'),
                                   { 'searchTerm': 'blend', 'lat': '12', 'lng': '40' })

        expected = Items.objects.get(item_name='blender')
        serialized = ItemsSerializer(expected)
        self.assertEqual(response.data[0], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class HelperFunctions(BaseViewTest):
    def test_calculate_distance_between_same_point(self):
        distance = calculate_distance((55, 55), (55, 55))
        self.assertEqual(distance, 0)

    def test_calculate_distance_between_diff_points(self):
        distance = calculate_distance((55, 55), (10, 10))
        self.assertEqual(round(distance, 2), 6355.92)

    def test_closest_items_returns_k_closest_items(self):
        points = [
            { 'distance' : 3},
            { 'distance' : 4},
            { 'distance' : 1},
            { 'distance' : 5}
        ]
        closest_points = closest_items(points, 2)
        expected = [
            { 'distance' : 1},
            { 'distance' : 3}
        ]
        self.assertEquals(closest_points, expected)

