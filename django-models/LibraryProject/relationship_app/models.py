from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __repr__(self):
        return f"{self.title} by {self.author}"


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __repr__(self):
        return f"<Library> {self.name}"


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __repr__(self):
        return self.name


class UserProfile(models.Model):
    role = models.CharField(max_length=10, choices=("Admin", "Librarian", "Member"), default="Member")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")