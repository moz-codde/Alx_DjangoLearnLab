from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books, LibraryDetailView, LibraryListView, UserCreateView, Admin_view, librarian_view, member_view, register



urlpatterns = [
    path("", LibraryListView.as_view(), name="library_list_view"),
    path("books/", list_books, name="books_list"),
    path("library/<pk>/", LibraryDetailView.as_view(), name="library_detail_view"),
    path("auth/login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("auth/logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("reg/", register, name="false_register"),
    path("admin-view/", Admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
]
