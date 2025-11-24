from .models import Author, Book, Library, Librarian


library_name = Library.objects.get(id=1)
library = Library.objects.get(name=library_name)
library.books.all()

author_name = Author.objects.get(id=1).name
author = Author.objects.get(name=author_name)
Book.objects.filter(author=author)


librarian = library.librarian