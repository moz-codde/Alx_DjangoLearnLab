from .models import Author, Book, Library, Librarian


Author.objects.get(id=1).books
Library.objects.get(id=1).books
Library.objects.get(id=1).librarian