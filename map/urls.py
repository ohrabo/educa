from django.urls import path

from . import views

app_name = 'map'
urlpatterns = [
    path('', views.map, name='showmap'),
    # path('updatemap/', views. getLocations, name='updatemap'),
    path('index/', views.SampleFormView.as_view()),
    # path('googlemap/', views.googlemap),
]