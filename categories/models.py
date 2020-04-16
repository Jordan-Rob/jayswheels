from django.db import models

from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    description = models.TextField(null=False, blank=False, max_length=120)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])
