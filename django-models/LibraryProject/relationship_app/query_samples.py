from .models import Author, Book, Library, Librarian


Author.objects.get(id=1).books
library_name = Library.objects.get(id=1)
Library.objects.get(name=library_name).books.all()
Library.objects.get(id=1).librarian