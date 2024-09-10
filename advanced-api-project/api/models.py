from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    """
    Author model stores information about book authors.
    Each author can have multiple books (one-to-many relationship).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model stores details about each book.
    Each book is linked to one author using a foreign key.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author,related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
