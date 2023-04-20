from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Book, Review
from .forms import ReviewForm



def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    book_of_the_month = Book.objects.get(id=2)
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books, 'book_of_the_month': book_of_the_month})

def myreadinglist(request):
    return render(request, 'books/myreadinglist.html')


@login_required
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    review_form = ReviewForm()
    return render(request, 'books/detail.html', {
        'book': book, 'review_form': review_form
        })

def add_review(request, book_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.user_id = request.user.id
        new_review.book_id = book_id
        new_review.save()
    return redirect('detail', book_id=book_id)


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'


class BookUpdate(UserPassesTestMixin, UpdateView):
    model = Book
    fields = '__all__'

    def test_func(self):
        return self.request.user.is_superuser


class BookDelete(UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['rating', 'comment']
    success_url = '/'

    def get_success_url(self):
        book_id = self.object.book.id
        return reverse('detail', kwargs={'book_id': book_id})

class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = '/'

    def get_success_url(self):
        book_id = self.object.book.id
        return reverse('detail', kwargs={'book_id': book_id})