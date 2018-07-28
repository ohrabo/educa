from django.contrib import admin
from .models import Category, Marker, Rental
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Marker)
class MarkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'lat', 'lon']
    list_filter = ['name']
    search_fields = ['name', 'date']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }