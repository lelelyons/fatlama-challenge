from django.db import models
import geopy.distance
import heapq

def filter_items(query, k):
    queryset = Items.objects.all()

    search_term, lat, lng = get_query_params(query)

    if search_term is not None:
        queryset = queryset.filter(item_name__contains=search_term)

    if lat is not None and lng is not None:
        distances = calculate_distances(lat, lng, queryset)
        k_closest_items = closest_items(distances, k)
        queryset = list(map(lambda i: i['item'], k_closest_items))

    return queryset[:k]

def get_query_params(query):
    search_term = query.get('searchTerm', None)
    lat = query.get('lat', None)
    lng = query.get('lng', None)
    return search_term, lat, lng

def calculate_distances(lat, lng, queryset):
    point = [float(lat), float(lng)]

    distances = [None] * len(queryset)

    for i, item in enumerate(queryset):
        item_point = (item.get_lat(), item.get_lng())
        distance = calculate_distance(point, item_point)
        distances[i] = { 'distance': distance, 'item': item }

    return distances

def calculate_distance(point1, point2):
    return geopy.distance.vincenty(point1, point2).km

def closest_items(points, k):
    return heapq.nsmallest(k, points, key=lambda p : p['distance'])

class Items(models.Model):
    item_name = models.CharField(max_length=255, null=False, primary_key=True)
    lat = models.FloatField()
    lng = models.FloatField()
    item_url = models.CharField(max_length=255, null=False)
    img_urls = models.CharField(max_length=255, null=False)

    def get_lat(self):
        return self.lat

    def get_lng(self):
        return self.lng

    def get_name(self):
        return self.item_name
