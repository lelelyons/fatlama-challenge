from django.db import models

class Items(models.Model):
    item_name = models.CharField(max_length=255, null=False, primary_key=True)
    lat = models.FloatField()
    lng = models.FloatField()
    item_url = models.CharField(max_length=255, null=False)
    img_urls = models.CharField(max_length=255, null=False)

