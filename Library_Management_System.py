from datetime import datetime
class Book:
    def __init__(self, name, id, category, quantity):
        self.name = name
        self.id = id
        self.category = category
        self.quantity = quantity
class User:
    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password
        self.borrowed_Books = []
        self.returned_Books = []
        self.borrowed_time = {}
        self.returned_time = {}
    def show_borrowed_books(self):
        if not self.borrowed_Books:
            print("\n\tYou are not borrowed any book")
        else:
            for book in self.borrowed_Books:
                borrow_time = self.borrowed_time[book.id]
                print(f"\tBook Name: {book.name}")
                print(f"\tBook ID: {book.id}")
                print(f"\tCategory: {book.category}")
                print(f"\tBorrow Time: {borrow_time}")
    def show_returned_books(self):
        if self.returned_Books:
            for book in self.returned_Books:
                return_time = self.returned_time[book.id]
                print(f"\tBook Name: {book.name}")
                print(f"\tBook ID: {book.id}")
                print(f"\tCategory: {book.category}")
                print(f"\tReturn Time: {return_time}\n")
        elif not self.borrowed_Books:
            print("\n\tYou are not borrowed any book")
        else:
            print("\n\tYou have not returned any books.")            
            
class Library:
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        self.books = []
        self.users = []
    def add_book(self, name, id, category, quantity):
        book = Book(name, id, category,quantity)
        self.books.append(book)
        print(f"\n\t{name} Book added")
    def add_user(self, name, id, password):
        user = User(name, id, password)
        self.users.append(user)
    def borrow_book(self, user, id):
        for book in self.books:
            if book.id == id:
                if book in user.borrowed_Books:
                    print("\n\tAlready Borrowed")
                    return
                elif book.quantity < 1:
                    print("\n\tNot available copy")
                    return
                else:
                    user.borrowed_Books.append(book)
                    book.quantity -= 1
                    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    user.borrowed_time[book.id] = current_time
                    print(f"\n\t{book.name} book is successfully borrowed")
            else:
                print("\n\tBook not found")
    def return_book(self, user, id):
        for book in self.books:
            if book.id == id:
                user.returned_Books.append(book)
                # book.quantity -= 1
                user.borrowed_Books.remove(book)
                book.quantity += 1
                current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                user.returned_time[book.id] = current_time
                print(f"\n\t{book.name} book is successfully returned")
            else:
                print(f"\n\t{book.name} book you are not borrowed")
    def show_users(self):
        for user in self.users:
            print(f"\n\tUser Name: {user.name}")
            print(f"\tUser Id: {user.id}")
    def show_books(self):
        for book in self.books:
            print(f"\tBook Name: {book.name}")
            print(f"\tBook ID: {book.id}")
            print(f"\tCategory: {book.category}")
            print(f"\tQuantity: {book.quantity}\n")
    def remove_user(self,id):
        for user in self.users:
            if user.id == id:
                self.users.remove(user)
                print(f"\t{user.name} with id number {user.id} has been successfully removed")
                break
pl = Library('Nupur', 'Nup Library')
admin = pl.add_user('Joy',101,'admin')
sheikhar = pl.add_user('Sheikhar',102,'adam')
pybook = pl.add_book('Python 3',145,'Programming',5)
cur_user = admin
import os
def clear_screen():
    os.system('cls')
clear_screen()
while True:
    if cur_user == None:
        print("""
           *********************************
           *                               *
           *  Welcome to Nupur's Library   *
           *                               *
           *********************************
            """)
        option = input("Login?Registration (R/L): ")
        if option == 'R' or option == 'r':
            name = input("\tEnter your name: ")
            id = int(input("\tEnter your id: "))
            password = input("\tEnter your password: ")
            user = pl.add_user(name, id, password)
            cur_user = user
        elif option == 'L' or option == 'l':
            id = int(input("\tEnter your id: "))
            password = input("\tEnter your password: ")
            match = False
            for user in pl.users:
                if user.id == id and user.password == password:
                    cur_user = user
                    match = True
                    break
            if match == False:
                print("\n\tNo user found.This id is not registed on our system")
    else:
        if cur_user.name == 'Joy':
            print("\nOptions: ")
            print("1 : Add Book")
            print("2 : Show Users")
            print("3 : Show Books")
            print("4 : Remove User")
            print("5 : Logout")
            choice = int(input("\nEnter Option: "))
            if choice == 1:
                name = input("\tEnter the book name: ")
                id = int(input("\tEnter the book id: "))
                category = input("\tEnter the book category: ")
                quantity = int(input("\tEnter the book quantity: "))
                pl.add_book(name, id, category, quantity)
            elif choice == 2:
                pl.show_users()
            elif choice == 3:
                pl.show_books()
            elif choice == 4:
                id = int(input("\tEnter the user id: "))
                pl.remove_user(id)
            elif choice == 5:
                cur_user = None
        else:
            print("\nOptions: ")
            print("1 : Borrow Book")
            print("2 : Return Book")
            print("3 : Show Books")
            print("4 : Show Borrowed Books")
            print("5 : Show Returned Books")
            print("6 : Logout")
            choice = int(input("\nEnter Option: "))
            if choice == 1:
                id = int(input("\tEnter id: "))
                pl.borrow_book(user, id)
            elif choice == 2:
                if not user.borrowed_Books:
                    print("\n\tYou are not borrowed any book")
                else:        
                    id = int(input("\tEnter book id: "))
                    pl.return_book(user, id)
            elif choice == 3:
                pl.show_books()
            elif choice == 4:
                cur_user.show_borrowed_books()
            elif choice == 5:
                cur_user.show_returned_books()
            elif choice == 6:
                cur_user = None