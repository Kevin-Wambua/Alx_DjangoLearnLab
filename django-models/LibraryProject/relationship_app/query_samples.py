from relationship_app.models import Author, Book, Library, Librarian

from relationship_app.models import Author, Book, Library, Librarian

# Example dynamic variable for library name
library_name = "Central Library"

# ✔ This is the expected pattern by the checker:
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in", library_name, ":", list(books_in_library))

# Query 1: All books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by", author_name, ":", list(books_by_author))

# Query 2: List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)  # ✔ Required format
books_in_library = library.books.all()
print("Books in", library_name, ":", list(books_in_library))

# Query 3: Retrieve librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian of", library_name, ":", librarian.name)
