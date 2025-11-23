from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()

print(book)
# Book object (None)