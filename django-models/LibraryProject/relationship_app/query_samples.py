from .models import Author, Book, Library, Librarian


library_name = Library.objects.get(id=1)
library_name.books.all()

author = Author.objects.get(name=author_name)
Book.objects.filter(author=author)

librarian = Library.objects.get(id=1).name()