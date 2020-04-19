from django.db import models
from django.urls import reverse

from users.models import CustomUser
from cars.models import Car

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=160)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.id)])
