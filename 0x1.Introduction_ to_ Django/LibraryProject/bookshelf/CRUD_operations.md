# Create a new book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Retrieve the created book
book = Book.objects.get(title="1984")
print(f"Retrieved Book: {book.title}, {book.author}, {book.publication_year}")

# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated Book Title: {book.title}")
book.delete()
books = Book.objects.all()
print(f"Books Remaining: {book.count()}")

