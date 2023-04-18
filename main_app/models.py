from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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

class Review(models.Model):
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
