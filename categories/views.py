from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Category
# Create your views here.


class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
