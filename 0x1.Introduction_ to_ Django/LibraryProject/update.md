# Update Operation

command:

'''python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
updated_book = Book.objects.get(title="Nineteen Eigthy-Four")
print(updated_book.title)
