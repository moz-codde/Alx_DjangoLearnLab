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
    queryset = Library.books
    template_name = "templates/relationship_app/library_detail.html"


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "relationship_app/register.html"


def register(request):
    form = UserCreationForm()
    pass


# tests
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "Libarian"

def is_member(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "Member"


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(lambda user: user.userprofile.role=="Member")
def member_view(request):
    return render(request, "relationship_app/member_view.html")
