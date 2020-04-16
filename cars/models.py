from django.db import models

from django.urls import reverse

from categories.models import Category

# Create your models here.


class Car(models.Model):
    image = models.ImageField(upload_to='images/cars/')
    make = models.CharField(null=False, blank=False, max_length=30)
    model = models.CharField(null=False, blank=False, max_length=30)
    year = models.IntegerField(null=False, blank=False)
    transmission = models.CharField(null=False, blank=False, max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('car_detail', args=[str(self.id)])
