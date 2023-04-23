from django.db import models
from django.db.models import Avg
from django.urls import reverse
from django.contrib.auth.models import User

RATING_CHOICES = (
    (1, '1 star'),
    (2, '2 stars'),
    (3, '3 stars'),
    (4, '4 stars'),
    (5, '5 stars'),
)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    numofpages = models.IntegerField('Number of Pages')
    genre = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=800)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
    
    def average_rating(self) -> float:
        rating = Review.objects.filter(book=self).aggregate(Avg("rating"))["rating__avg"] or 0
        return round(rating * 2) / 2


class Review(models.Model):
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(
        'Select Rating',
        choices=RATING_CHOICES,
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book rating - {self.rating}"
    
class ReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.user}'s Reading List"
    

class BooksRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.user}'s Books Read"
    