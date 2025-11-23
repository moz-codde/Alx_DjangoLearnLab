from bookshelf.models import Book

b = Book.objects.first()

b.title = "Nineteen Eighty-Four"
b.save()

print(b.title)
# Nineteen Eighty-Four
