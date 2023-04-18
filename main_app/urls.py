from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('books/<int:book_id>/', views.book_detail, name='detail'),
    path('books/create/', views.BookCreate.as_view(), name = 'books_create')
]