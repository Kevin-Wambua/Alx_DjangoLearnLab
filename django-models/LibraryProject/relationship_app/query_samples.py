from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (e.g., "George Orwell")
george = Author.objects.get(name="George Orwell")
books_by_george = Book.objects.filter(author=george)
print("Books by George Orwell:", list(books_by_george))

# 2. List all books in a specific library (e.g., "Central Library")
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in Central Library:", list(books_in_library))

# 3. Retrieve the librarian for a specific library (e.g., "Central Library")
librarian = Librarian.objects.get(library=library)
print("Librarian of Central Library:", librarian.name)
