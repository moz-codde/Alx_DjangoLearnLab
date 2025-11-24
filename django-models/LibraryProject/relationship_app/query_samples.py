from .models import Author, Book, Library, Librarian


library_name = Library.objects.get(id=1)
library_name.books.all()

author_name = Author.objects.get(id=1)
author_name.books.all()

librarian = Library.objects.get(id=1).name