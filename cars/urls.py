from django.urls import path

from .views import CarDetailView, CarListView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail')
]
