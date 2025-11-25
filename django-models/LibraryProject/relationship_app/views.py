from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Library, Book

# Create your views here.
def list_books(request):
    """This view should render a simple text list of book titles and their authors."""
    books = Book.objects.all()
    return render(request, "templates/relationship_app/list_books.html", context={"books": books})
    

class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "library"
    template_name = "templates/relationship_app/library_detail.html"


class LibraryListView(ListView):
    queryset = Library.books.all()
    template_name = "templates/relationship_app/library_detail.html"


class UserCreateView(CreateView):
    fields = "__all__"
    model = User