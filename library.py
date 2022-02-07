# libs:
import pickle
import os

# PATH :
PATH = "C:/Users/markazi/Desktop/python-faradars/python/"

# validation :

def check_validation():

    if not os.path.exists(PATH + "j20-users.dat"):
        f = open(PATH + "j20-users.dat", "wb")
        users_dict = {}
        pickle.dump(users_dict, f)
        f.close()

    if not os.path.exists(PATH + "j20-books.dat"):
        f = open(PATH + "j20-books.dat", "wb")
        books_dict = {}
        pickle.dump(books_dict, f)
        f.close()

    if not os.path.exists(PATH + "j20-borrows.dat"):
        f = open(PATH + "j20-borrows.dat", "wb")
        borrows_dict = {}
        pickle.dump(borrows_dict, f)
        f.close()
# functions:

def add_users(name, family, father_name, code, birthday):
    check_validation()

    f = open(PATH + "j20-users.dat", "rb")
    users_dict = pickle.load(f)
    f.close()

    user_id = len(users_dict)
    users_dict[user_id] = [name, family, father_name, code, birthday]

    f = open(PATH + "j20-users.dat", "wb")
    pickle.dump(users_dict, f)
    f.close()

    print("welcome to our library ... your user id is :", user_id )

def add_book(title, author, subject, year):
    check_validation()

    f = open(PATH + "j20-books.dat", "rb")
    books_dict = pickle.load(f)
    f.close()

    books_dict[title] = [author, subject, year]

    f = open(PATH + "j20-books.dat", "wb")
    pickle.dump(books_dict, f)
    f.close()

def search_book(title):
    check_validation()

    f = open(PATH + "j20-books.dat", "rb")
    book_dict = pickle.load(f)
    f.close()

    print(book_dict[title])

def borrow(user_id, title):
    check_validation()

    f = open(PATH + "j20-borrows.dat", "rb")
    borrows_dict = pickle.load(f)
    f.close()

    borrows_dict[user_id] = title

    f = open(PATH + "j20-borrows.dat", "wb")
    pickle.dump(borrows_dict, f)
    f.close()

def show_all_info():
    check_validation()

    f = open(PATH + "j20-users.dat", "rb")
    user_dict = pickle.load(f)
    f.close()

    f = open(PATH + "j20-books.dat", "rb")
    books_dict = pickle.load(f)
    f.close()

    f = open(PATH + "j20-borrows.dat", "rb")
    borrows_dict = pickle.load(f)
    f.close()

    print("-----------------users-----------------")
    print(user_dict)
    print("-----------------books-----------------")
    print(books_dict)
    print("-----------------borrows---------------")
    print(borrows_dict)
    print("----------------------------------")

#start :
os.system("cls")
ch = 1
while ch != 0 :

    print("1-Add User\n2-Add new Book\n3-Search\n4-Barrow\n5-Show All\n2-Exit")
    ch = int(input("Enter Your Choice : "))
    os.system("cls")

    if ch == 1:
        name = input("Enter Name : ")
        family = input("Enter Family : ")
        father_name = input("Enter Father Name : ")
        code = input("Enter Nationalty Code : ")
        birthday = input("Enter Birthday : ")
        add_users(name, family, father_name, code, birthday)
    
    elif ch == 2:
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        subject = input("Enter Subject: ")
        year = input("Enter Year: ")
        add_book(title, author, subject, year)
    elif ch == 3:
        title = input("Enter Title: ")
        search_book(title)
    elif ch == 4:
        user_id = input("Enter User id : ")
        title = input("Enter Title : ")
        borrow(user_id, title)
    elif ch == 5:
        show_all_info()