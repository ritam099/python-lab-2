
from LibraryManager import LibraryManager

def demonstrate_library_manager():
    # Create a LibraryManager instance
    library = LibraryManager()
    
    
    books_data = [
        {"title": "Modern Operating Systems", "author": "Andrew S. Tanenbaum", "publisher": "Prentice Hall", "volume": "3rd Edition", "year": 2021, "isbn": "9780133591620"},
        {"title": "Introduction to Machine Learning", "author": "Ethem Alpaydin", "publisher": "MIT Press", "volume": "4th Edition", "year": 2022, "isbn": "9780262043791"},
        
    ]
    
    # Add sample books to the library
    for book in books_data:
        library.add_book(
            title=book['title'],
            author=book['author'],
            publisher=book['publisher'],
            volume=book['volume'],
            year=book['year'],
            isbn=book['isbn']
        )
    
    # List all books in the library
    print("All books in the library:")
    for isbn, details in library.list_books().items():
        print(f"ISBN: {isbn}, Details: {details}")
    
    # Retrieve a book's details
    isbn_to_retrieve = "9780262043791"
    print(f"\nRetrieving book with ISBN '{isbn_to_retrieve}':")
    book = library.retrieve_book(isbn_to_retrieve)
    print(book if book else f"Book with ISBN {isbn_to_retrieve} not found.")
    
    # Search for books by title
    print("\nSearching for books with title containing 'Data Structures':")
    results = library.search_books(title='Data Structures')
    for book in results:
        print(book)
    
    # Search for books by author
    print("\nSearching for books by author 'Ethem Alpaydin':")
    results = library.search_books(author='Ethem Alpaydin')
    for book in results:
        print(book)
    
    # Update a book's details
    isbn_to_update = "9781118290279"
    print(f"\nUpdating book with ISBN '{isbn_to_update}':")
    library.update_book(
        isbn=isbn_to_update,
        title="Data Structures and Algorithms in Python - Updated",
        author="Michael T. Goodrich - Updated"
    )
    print(library.retrieve_book(isbn_to_update))
    
    # Check availability of a book
    isbn_to_check = "9780133591620"
    print(f"\nChecking availability of book with ISBN '{isbn_to_check}':")
    print("Available" if library.check_availability(isbn_to_check) else "Not Available")
    
    # Remove a book
    isbn_to_remove = "9780262043791"
    print(f"\nRemoving book with ISBN '{isbn_to_remove}':")
    library.remove_book(isbn_to_remove)
    print("Book removed.")
    print("Available" if library.check_availability(isbn_to_remove) else "Not Available")

    # List all books in the library after removal
    print("\nAll books in the library after removal:")
    for isbn, details in library.list_books().items():
        print(f"ISBN: {isbn}, Details: {details}")

if __name__ == "__main__":
    demonstrate_library_manager()
