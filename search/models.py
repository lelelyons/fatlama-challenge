from django.db import models

class Items(models.Model):
    item_name = models.CharField(max_length=255, null=False, primary_key=True)
    lat = models.FloatField(null=False)
    lng = models.FloatField(null=False)
    item_url = models.CharField(max_length=255, null=False)
    img_urls = models.CharField(max_length=255, null=False)

    def get_lat(self):
        return self.lat

    def get_lng(self):
        return self.lng

    def get_name(self):
        return self.item_name
