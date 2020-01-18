from django.urls import path
from  googlemap.views import GoogleMapView, GoogleMapShowView

urlpatterns = [
    path('', GoogleMapView.as_view()),
    path('success/', GoogleMapShowView.as_view()),
]