from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})


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


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = '__all__'


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/'


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['rating', 'comment']
    success_url = '/'