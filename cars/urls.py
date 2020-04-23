from django.urls import path

from .views import CarDetailView, CarListView
from car_reviews.views import ReviewCreateView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('cars/<int:pk>/review/create/',
         ReviewCreateView.as_view(), name='car_review_create')
]
