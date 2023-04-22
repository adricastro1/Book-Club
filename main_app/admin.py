from django.contrib import admin
from .models import Book, Review, ReadingList, BooksRead

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(ReadingList)
admin.site.register(BooksRead)