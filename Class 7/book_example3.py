class Book:

    def __init__(self, ISBN, title, used):
        self._ISBN = ISBN
        self.title = title
        self._owner = "Biblioteque Brossard"
        self.used = used

    def is_book_used(self):
        return self.used

    def set_isbn(self, isbn_value):
        self.ISBN = isbn_value

    def get_isbn(self):
        return self.ISBN

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title



book1 = Book("123456789", "War of the Worlds", False)
book1.set_title("Some other title")

book2 = Book("234567890", "Insomnia", False)
book3 = Book(None, "Insomnia Part 2", True)


array_of_books = [book1, book2, book3]

for b in array_of_books:
    print(b.title)
    print("Book used?", end=" ")
    if b.is_book_used():
        print("Yes")
    else:
        print("No")