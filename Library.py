members=[]
books=[]

def add_mem():
    n=input("Enter name: ")
    i=input("Enter ID: ")
    m=Member(n,i)
    members.append(m)
    
class Member:
    def __init__(self,name,id):
        self.name = name
        self.ID = id 
        
    def view_all():
        for m in members:
            print(m.name,m.ID)
        
    def search_by_name():
        n=input("Name to Search:")
        found=False
        for m in members:
            if m.name==n:
                print(m.ID)
                found=True
        if not found:
            print("No such Name Found!")

    def del_mem():
        Member.view_all()
        i=int(input("Enter the ID of member to be deleted :"))
        for m in members:
            if m.id==i:
                del members[m]
                print("Deleted Successfully.")
                break
            else:
                continue
            
def add_book():
    name=input("Name of the book:")
    auth=input("Author of the book:")
    id=input("ID of the book:")  
    bk=book(name,auth,id)
    books.append(bk)

class book:
    def __init__(self,name,auth,id):
        self.name=name
        self.auth=auth
        self.id=id 
        
    def issue(self):
        t=input("Enter Title: ")
        a=input("Author: ")
        self.title=t
        self.author=a
        print("\nIssuing book...\n")
        v=view_availability()
        if v=="Available":
            self.issuedto=input("Member ID to Issue the Book To: ")
            self.make_unavailable()
            print("Book Issued Successfully!\n")
        else:
            print("Sorry, The Book is Not Available.\n")
                
        def make_available(self):
            self.available="Yes"
