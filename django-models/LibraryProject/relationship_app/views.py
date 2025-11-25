from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
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
    form_class = UserCreationForm
    template_name = "relationship_app/register.html"


def register(request):
    form = UserCreationForm()
    pass


@user_passes_test(lambda user: user.profile.role == "Admin")
def admin_view(request):
    ...


@user_passes_test(lambda user: user.profile.role == "Librarian")
def librarian_view(request):
    ...


@user_passes_test(lambda user: user.profile.role == "Member")
def member_view(request):
    ...
