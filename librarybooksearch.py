def find_book(books, index, target):
    '''Searches for a book in the library using recursion.'''

    if index == len(books):
        return -1  # Book not found

    if books[index].lower() == target.lower():
        return index  # Book found

    return find_book(books, index + 1, target)

library = [ 
    "Harry Potter ",
    "To Kill a Mockingbird",
    "The Great Gatsby",
    "The Alchemist",
    "Diary of a wimpy Kid",
    "Wings of Fire",
    "The Hunger Games",
    "Atomic Habits",
]

print(find_book.__doc__)

book_name = input("Enter the book to search: ")

result = find_book(library, 0, book_name)

if result == -1:
    print("Book not found in the library.")

else:
    print("Book found at Shelf Position:", result)
    print("Book Name:", library[result])

