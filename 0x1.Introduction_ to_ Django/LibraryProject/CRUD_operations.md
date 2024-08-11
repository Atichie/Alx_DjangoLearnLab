## CRUD Operations Documentation
from bookshelf.models import Book

# Create a new book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Retrieve the created book
book = Book.objects.get(title="1984")
print(f"Retrieved Book: {book.title}, {book.publication_year}")

# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated Book Title: {book.title}")

# Delete the book 
book.delete()

# Confirm deletion by checking if any bookss exist
books = Book.objects.all()
print(f"Books Remaining: {books.count()}")
