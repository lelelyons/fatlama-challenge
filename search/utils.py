from geopy.distance import vincenty
from heapq import nsmallest

def filter_items(items, param, k):
    search_term, lat, lng = get_params(param)

    if search_term is not None:
        items = items.filter(item_name__contains=search_term)

    if lat is not None and lng is not None:
        item_distances = calculate_distances(lat, lng, items)
        items = closest_items(item_distances, k)

    return items[:k]

def get_params(params):
    search_term = params.get('searchTerm', None)
    lat = params.get('lat', None)
    lng = params.get('lng', None)
    return search_term, lat, lng

def calculate_distances(lat, lng, items):
    point = [float(lat), float(lng)]

    distances = [None] * len(items)

    for i, item in enumerate(items):
        distance = calculate_distance(point, (item.get_lat(), item.get_lng()))
        distances[i] = { 'distance': distance, 'item': item }

    return distances

def calculate_distance(point1, point2):
    return vincenty(point1, point2).km

def closest_items(points, k):
    k_closest_items = nsmallest(k, points, key=lambda p : p['distance'])
    return list(map(lambda i: i['item'], k_closest_items))

