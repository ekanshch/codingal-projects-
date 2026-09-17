books = {
    101 : "Harry Potter",
    102 : "Diary of a Wimpy Kid",
    103 : "Matilda"
}

print("Library Books:")
for book_id, book_name in books.items():
    print(book_id, "-", book_name)

search_id = int(input("Enter the Book Id to search: "))

if search_id in books:
    print("Book Found:", books[search_id])

else:
    print("Book not Found")

new_id = int(input("Enter new book ID:  "))
new_book = input("Enter book name:  ")

books[new_id] = new_book

print("\n Updated Library:")
for book_id, book_name in books.items():
    print(book_id, "-", book_name)
    