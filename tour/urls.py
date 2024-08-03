from django.urls import path
from .views import CarList, CarRetrieve, TourList, TourRetrieve, BookingDelete, BookingCreate, BookingUpdate


urlpatterns = [
    path('car/', CarList.as_view()),
    path('tour/', TourList.as_view())
]

