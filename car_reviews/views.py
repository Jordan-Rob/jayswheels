
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView

)

from .models import Review

# Create your views here.


class ReviewCreateView(CreateView):
    model = Review
    fields = ('title', 'description', )
    template_name = 'review_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.car = self.request.car
        return super().form_valid(form)


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review_detail.html'


class ReviewUpdateView(UpdateView):
    model = Review
    fields = ('title', 'description')
    template_name = 'review_update.html'


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('car_detail')
