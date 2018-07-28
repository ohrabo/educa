from django.db import models
from django.urls import reverse
from django_google_maps import fields as map_fields

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

class Marker(models.Model):
    marker = models.ForeignKey(Category, related_name='markers', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True, blank=True)
    link = models.CharField(max_length=500)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('doc-detail', args=[str(self.id)])

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
