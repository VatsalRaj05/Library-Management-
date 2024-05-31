import os,pickle
if not os.path.exists('data'):
    books={}
    members={}
    lib=(members,books)
    with open("data","wb") as f:
        pickle.dump(lib,f)

with open("data","rb") as f:
    lib=pickle.load(f)
    members,books=lib

def add_mem():
    n=input("Enter the name of the member:")
    members[n]={"id":0, "age":0, "gender":" ", "bk_borrowed":[]}
    a=int(input("Enter the age of the member:"))
    b=input("Enter the gender of the member:")
    c=int(input("Enter the id of the member:"))
    
    members[n]["age"]=a
    members[n]["gender"]=b
    members[n]["id"]=c
    print("Member added successfully")

def view_mem():
    for m in members:
        print(f'ID:{members[m]["id"]} Name:{m} Age:{members[m]["age"]} Gender:{members[m]["gender"]}')

def del_mem():
    view_mem()
    n=int(input("Enter the ID of the member to be deleted:"))
    for m in members.copy():
        if n==members[m]["id"]:
            if len(members[m]["bk_borrowed"]) !=0:
                for bk in members[m]["bk_borrowed"]:
                    books[bk]['status']='Available'
            del members[m]
            print("Deleted Successfully")
            break
        else:
            print("ID not found")

def search_mem(books):
    print("1.Search by ID:")
    print("2.Search by Name:")
    n=int(input("Enter your choice:"))
    if n==1:
        a=int(input("Enter the ID of the member:"))
        for m in members:
            if a==members[m]["id"]:
                print(f'ID:{members[m]["id"]}   Name:{m}  Age:{members[m]["age"]}   Gender:{members[m]["gender"]}   No.of books borrowed:{len(members[m]["bk_borrowed"])}')
                print("Here's the list of books borrowed:")
                if len(members[m]["bk_borrowed"])==0:
                    print("No books borrowed.\n")
                else:
                    for i in members[m]['bk_borrowed']:
                        # i=members[m]['bk_borrowed'][j]
                        print(f"ID:{books[i]['id']}   Title:{i}    Author Name: {books[i]['auth_name']}") 
                        # break
            else:
                # print("ID not found.")
                continue
    elif n==2:
        b=input("Enter the Name of the member:")
        for m in members:
            if b==m:
                print(f'ID:{members[m]["id"]} Name:{m} Age:{members[m]["age"]} Gender:{members[m]["gender"]} No. of books borrowed:{len(members[m]["bk_borrowed"])}')
                print("Here's the list of books borrowed:")
                if len(members[m]["bk_borrowed"])==0:
                    print("No books borrowed.")
                else:
                    for i in members[m]['bk_borrowed']:
                        print(f"ID:{books[i]['id']}   Title:{i}    Author Name: {books[i]['auth_name']}") 
                        # break
            else:
                continue
    else:
        print("Invalid option")
        
        
def add_bk():
    n=input("Title of the book:")
    a=input("Author of the book:")
    i=int(input("ID of the book:"))
    books[n]={"id":0,"auth_name":"", "status":"Available"}
    books[n]["id"]=i
    books[n]["auth_name"]=a

def search_bk():
    print("1.Search by Title: \n2.Search by ID: \n3.Search by Author name: ")
    n=int(input("Enter your choice:"))
    if n==1:
        name=input("Enter the title of the book:")
        for b in books:
            if name==b:
                print(f"ID: {books[b]['id']}    Title: {b}    Author Name: {books[b]['auth_name']}    Status: {books[b]['status']} \n")
            else:
                continue
    elif n==2:
        id=int(input("Enter the ID of the book:"))
        for b in books:
            if id == books[b]["id"]:
                print(f"ID: {books[b]['id']}    Title: {b}    Author Name: {books[b]['auth_name']}    Status: {books[b]['status']} \n")
            else:
                continue
    elif n==3:
        name=input("Enter the name of the Author of the book:")
        for b in books:
            if name==books[b]["auth_name"]:
                print(f"ID: {books[b]['id']}    Title: {b}    Author Name: {books[b]['auth_name']}    Status: {books[b]['status']} \n")
            else:
                continue
    else:
        print("Invalid Option!")

def view_bk():
    print("Here's the list of all the books:")
    for b in books:
        print(f"ID: {books[b]['id']}    Title: {b}    Author Name: {books[b]['auth_name']}    Status: {books[b]['status']}")

def issue_bk(members):
    view_bk()
    i=int(input("Enter the ID of the book to be issued:"))
    m=input("Enter name of borrower:")
    for b in books:
        if i==books[b]['id']:
            if books[b]["status"]== "Issued":
                print("This book is already Issued.")
            else:
               print(f"The book has been successfully issued to {m}.")
               books[b]["status"]="Issued"
               members[m]["bk_borrowed"].append(b)
               break

        else:
            print("Invalid book ID.")


while True:
    print("-----------Library Management Program------------/n")
    print("Menu/n")
    print("1.Members\n")
    print("2.Books\n")
    print("3.Exit\n")
    n=int(input("Enter your option: "))

    if n==1:
        while True:
            print("\n1.Add members \n2.Search members \n3.View all members \n4.Delete members \n5.Exit \n")
            m=int(input("Enter Option:"))
            if m==1:
                add_mem()
            elif m==2:
                search_mem(books)
            elif m==3:
                view_mem()
            elif m==4:
                del_mem()
            elif m==5:
                break
            else:
                print("Enter valid option\n")

            with open("data","wb") as f:
                pickle.dump(lib,f)
    elif n==2:
        while True:
            print("1.Add book \n2.Search book \n3.View all book \n4.Issue Book \n5.Exit \n")
            m=int(input("Enter Option:"))
            if m==1:
                add_bk()
            elif m==2:
                search_bk()
            elif m==3:
                view_bk()
            elif m==4:
                issue_bk(members)                
            elif m==5:
                break
            else:
                print("Enter valid option \n")
            with open("data","wb") as f:
                pickle.dump(lib,f) 
    elif n==3:
        print(r"""
              Thanks for using my program
              """)
        break

    else:
        print("Invalid input \n")