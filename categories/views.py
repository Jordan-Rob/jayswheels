from django.shortcuts import render

from django.views.generic import ListView

from .models import Category
# Create your views here.

class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'

