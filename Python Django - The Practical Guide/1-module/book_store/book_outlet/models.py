from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# after creating a model, we need to create migrations to make the..
# ...python execute this
# Create your models here.
# it is a child of moderls.models
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"
