class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

# Create an instance of the Book class
book_instance = Book("To Kill a Mockingbird", "Harper Lee", 281)
print(book_instance.display_info())

# Derived class Ebook that inherits from Book
class Ebook(Book):
    def __init__(self, title, author, pages, formate):
        super().__init__(title, author, pages)
        self.formate = formate

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Format: {self.formate}"

# Create an instance of the Ebook class
ebook_instance = Ebook("1984", "George Orwell", 328, "PDF")
print(ebook_instance.display_info())
