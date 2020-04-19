from django.urls import path

from .views import (
    ReviewCreateView,
    ReviewDeleteView,
    ReviewDetailView,
    ReviewUpdateView
)

urlpatters = [
    path('reviews/create/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('review/<int:pk>/delete/',
         ReviewDeleteView.as_view(), name='review_delete'),
    path('review/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_update')
]
