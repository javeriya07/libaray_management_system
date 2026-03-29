class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("Book added successfully!")

    def show_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"{book.title} by {book.author} - {status}")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_issued:
                book.is_issued = True
                print("Book issued successfully!")
                return
        print("Book not available!")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_issued:
                book.is_issued = False
                print("Book returned successfully!")
                return
        print("Invalid return!")

def main():
    lib = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            lib.add_book(title, author)

        elif choice == "2":
            lib.show_books()

        elif choice == "3":
            title = input("Enter book title: ")
            lib.issue_book(title)

        elif choice == "4":
            title = input("Enter book title: ")
            lib.return_book(title)

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
