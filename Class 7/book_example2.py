class Book:

    def __init__(self, ISBN, title, used):
        self.ISBN = ISBN
        self.title = title
        self.owner = "Biblioteque Brossard"
        self.used = used

    def is_book_used(self):
        return self.used

book1 = Book("123456789", "War of the Worlds", False)
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