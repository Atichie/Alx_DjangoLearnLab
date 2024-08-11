# Update the title of the book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eight-Four"
book.save()()

# Verify update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book.title)

