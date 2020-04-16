from django.urls import path

from .views import CategoryList, CategoryDetailView

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail')
]
