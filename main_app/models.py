from django.db import models
from django.db.models import Avg
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    numofpages = models.IntegerField()
    genre = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=500)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
    
    def average_rating(self) -> float:
        return Review.objects.filter(book=self).aggregate(Avg("rating"))["rating__avg"] or 0

class Review(models.Model):
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book rating - {self.rating}"
    
