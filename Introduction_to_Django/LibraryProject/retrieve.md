from bookshelf.models import Book

b = Book.objects.first()

print(b.title)
# 1984

print(b.author)
# George Orwell

print(b.publication_year)
# 1949