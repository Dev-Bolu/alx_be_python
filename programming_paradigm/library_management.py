class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute (single underscore for convention)

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        status = 'Available' if self.is_available() else 'Checked Out'
        return f"Title: {self.title}, Author: {self.author} - {status}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        self._books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                book.check_out()
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        print("\nAvailable Books in the Library:")
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")


# Example Usage:
if __name__ == "__main__":
    # Instantiate Library
    my_library = Library()

    # Add Books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # List Available Books
    my_library.list_available_books()

    # Check Out a Book
    my_library.check_out_book("1984")
    my_library.check_out_book("1984")  # Try to check out again

    # Return a Book
    my_library.return_book("1984")
    my_library.return_book("1984")  # Try to return again

    # List Available Books Again
    my_library.list_available_books()
