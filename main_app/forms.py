from django import forms
from .models import Review, Book

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')

        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'})
        }



class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'numofpages', 'genre', 'synopsis')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'numofpages': forms.NumberInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control', 'style': 'min-width: 300px;'}),
        }

        labels = {
            'title': 'Title',
            'author': 'Author',
            'numofpages': 'Number of Pages',
            'genre': 'Genre',
            'synopsis': 'Synopsis',
        }