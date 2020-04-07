from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    description = models.TextField(null=False, blank=False, max_length=120)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
