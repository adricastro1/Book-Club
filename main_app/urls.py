from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('books/<int:book_id>/', views.book_detail, name='detail'),
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:book_id>/add_review/', views.add_review, name='add_review'),
    path('books/<int:book_id>/reviews/<int:pk>/edit/', views.ReviewUpdate.as_view(), name='review_update'),
]
