from bookshelf.models import Book

b = Book.objects.get(id=1)
b.delete()

print(b)
# Book object (None)