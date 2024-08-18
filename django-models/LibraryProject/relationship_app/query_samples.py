import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author {author_name} does not exist.")

def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=Library_name)
        books = library.books.all()
        print(f"Books in {Library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist
    print(f"Library {library_name} does not exist.")

def retrieve_librarian_for _library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")


name= "__main__"
if __name__ == "__main__":
    query_all_books_by_uthor('J.K. Rowling')
    list_all_books_in_library('Central Library')
    retrieve_librarian_for_library('Central Library')


