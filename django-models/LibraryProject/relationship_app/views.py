from django.shortcuts import render

from .models import Book

# Create your views here.
def list_all_books(request):
    books = Book.objects.all()
    result = [f"{book.title} by {book.author}" for book in books]
    return str(result)