from django.db import models
from scipy.spatial import distance
import heapq
import pdb

def filter_items(query, k):
    queryset = Items.objects.all()

    search_term, lat, lng = get_query_params(query)

    if search_term is not None:
        queryset = queryset.filter(item_name__contains=search_term)
    else:
        return []

    if lat is not None and lng is not None:
        distances = calculate_distances(lat, lng, queryset)
        k_closest_items = closest_items(distances, k)
    else:
        return queryset[:20]

    return list(map(lambda i: i['queryset'], k_closest_items))

def get_query_params(query):
    search_term = query.get('searchTerm', None)
    lat = query.get('lat', None)
    lng = query.get('lng', None)
    return search_term, lat, lng

def calculate_distances(lat, lng, queryset):
    distances = [None] * len(queryset)

    for i, item in enumerate(queryset):
        distances[i] = { 'distance': distance.pdist(
            [[float(lat), float(lng)], [item.get_lat(), item.get_lng()]],
            'euclidean'
        )[0],
            'queryset': item
            }
    return distances

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
