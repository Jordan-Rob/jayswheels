from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Category
from cars.models import Car
# Create your views here.


class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(
            *args, **kwargs)
        context['category_cars'] = Car.objects.filter(
            category=context['object']
        )
        return context
