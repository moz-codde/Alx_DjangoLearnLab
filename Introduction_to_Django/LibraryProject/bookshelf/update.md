from bookshelf.models import Book

b = Book.objects.get(id=1)

b.title = "Nineteen Eighty-Four"
b.save()

print(b.title)
# Nineteen Eighty-Four
