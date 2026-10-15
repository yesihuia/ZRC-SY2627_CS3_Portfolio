
class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 1
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if isinstance(number_of_pages, int) and number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.__number_of_pages}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 1
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if isinstance(issue_number, int) and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")


# Creating objects
pub1 = Publication(
    "Journal of Experimental Psychology",
    "Ratchiff, R. & Van Dongen, H."
)

pub2 = Publication(
    "Reading Today",
    "Maria Santos"
)

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Noli Me Tangere", "Jose Rizal", 480)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Science Today", "Science Club", 12)


# Printing the information
print("Publication Information:")
pub1.display_info()

print("\nSecond Publication Information:")
pub2.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nSecond Book Information:")
book2.display_info()

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())

print("\nSecond Magazine Information:")
mag2.display_info()


# Updating information
print("\nUpdating Information:")

book1.set_number_of_pages(350)
book1.set_title("The Hobbit - Revised Edition")
book1.display_info()

mag1.set_issue_number(203)
mag1.set_title("National Geographic - New Issue")
mag1.display_info()
