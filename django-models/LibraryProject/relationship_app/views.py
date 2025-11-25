from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Book, Library

# Create your views here.
def list_all_books(request):
    books = Book.objects.all()
    return books
    

class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "library"


class LibraryListView(ListView):
    queryset = Library.books.all()