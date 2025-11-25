from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books, LibraryDetailView, LibraryListView, UserCreateView


app_name = "relationship_app"

urlpatterns = [
    path("", LibraryListView.as_view(), name="library_list_view"),
    path("books/", list_books, name="books_list"),
    path("library/<pk>/", LibraryDetailView.as_view(), name="library_detail_view"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
]
