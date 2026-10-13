class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isborrowed = False

    def borrow(self):
        if not self.isborrowed:
            self.isborrowed = True
            print(f"{self.title} has been borrowed.")

        else:
            print(f"{self.title} is not available for borrowing.")

    def return_book(self):
        if self.isborrowed:
            self.isborrowed = False
            print(f"{self.title} has been returned in the library.")

        else:
            print(f"{self.title} is checked out of library.")


book1 = Book("Diary of a Wimpy Kid", "Jeff Kinney")
book2 = Book("Harry Potter", "J.K. Rowling")
book3 = Book("The Hunger Games", "Suzanne Collins")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()