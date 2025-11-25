from django.urls import path

from .views import list_books, LibraryDetailView, LibraryListView


app_name = "relationship_app"

urlpatterns = [
    path("", LibraryListView.as_view(), name="library_list_view"),
    path("books/", list_all_books, name="books_list"),
    path("library/<pk>/", LibraryDetailView.as_view(), name="library_detail_view"),
]
