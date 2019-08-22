from django.db import models

# Create your models here.

class Category(models.Model):
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.name