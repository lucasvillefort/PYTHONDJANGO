from django.db import models


# after creating a model, we need to create migrations to make the..
# ...python execute this
# Create your models here.
# it is a child of moderls.models
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
