# Retrieve Operation

Command:

'''python
from bookshelf.models import Book
books = Book.objects.get(title="1984")
print(f"Retrieved Book: {book.title}, {book.author}, {book.publc_year}")

