from bookshelf.models import Book

b = Book.objects.first()
b.delete()

print(b)
# Book object (None)