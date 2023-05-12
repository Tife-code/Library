class Book:
    def __init__(self, title, author, pages, type):
        self.title = title
        self.author = author
        self.pages = pages
        self.type = type
    
    def print_info(self):
        print(f"====='BOOK DETAILS'======")
        print(f"Title: {self.title.upper()} \nAuthor: {self.author.title()} \nNumber of pages: {self.pages} \nType of Book: {self.type}")
        print("=========================")


class Library:
    def __init__(self):
        self.books_list= list()

    def add_book(self, obj):
        self.books_list.append(obj)

    def print_book(self):
        for book in self.books_list:
            book.print_info()

    def borrow_book(self, title):
        for book in self.books_list:
            if book.title.lower() == title.lower():
                self.books_list.remove(book)
                return book
        return None   
        
Oluwasanmi_Library = Library()
books = open("books.txt")
for x in  books:
    arg_list = x.strip("\n").split(", ")
    Oluwasanmi_Library.add_book(Book(arg_list[0], arg_list[1], arg_list[2], arg_list[3]))

print("BOOKS IN THIS LIBRARY INLUDE: ")
Oluwasanmi_Library.print_book()

while True:
    borrowed = input("\nEnter the title of the book you want to borrow: ") 
    borrowed_book = Oluwasanmi_Library.borrow_book(borrowed)
    if borrowed_book:
        print("\nBOOK BORROWED:")
        borrowed_book.print_info()

        print("\nBOOKS IN THE  LIBRARY NOW INCLUDE: ")
        Oluwasanmi_Library.print_book()
        break

    else:
        print("Book not found in library. Please enter another book title.")

