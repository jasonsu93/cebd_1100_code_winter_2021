class Book:
    def __init__(self, name, author):

        self.pages = 0
        self.name = name
        self.author = author

class Author:
    def __init__(self, name, pen):
        self.name = name
        self.pen_name = pen

author1 = Author("Gene Roddenberry", "Dude")

book1 = Book("Picard", author1)
book2 = Book("Discovery", author1)


print(book1.author.name)
