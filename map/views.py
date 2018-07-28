import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import ListView, FormView

from map.forms import SampleForm
from map.models import Marker
from django.core import serializers
#
# # class BookListView(ListView):
# #     model = Marker
#
# def map(request):
#     return render(request, 'map/hrmap.html')

# def googlemap(request):
#     return render(request, 'map/markered_map.html')

# # def updatemap(request):
# #     locations = {}
# #     markers = Marker.objects.all()
# #     for i in markers:
# #         locations[i.lat] = i.lon
# #     return render(request, 'map/markered_map.html', {'locations': json.dumps(locations)})
#
def map(request):
    markers_list=Marker.objects.all().values_list('lat', 'lon', 'description', 'marker')
    markers = json.dumps(list(markers_list))
    return render(request, 'map/hrmap.html', {'markers': markers}

                  )



class SampleFormView(FormView):
    form_class = SampleForm
    template_name = "map/index.html"


# markers = Marker.objects.values_list('lat','lon')
# markers_json = json.dumps(list(markers), cls=DjangoJSONEncoder)