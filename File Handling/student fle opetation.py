import pickle
def add_data():
    f1=open("ABC.dat","ab")
    rno=int(input("Enter yout roll number"))
    name=input("Enter your name")
    clas=input('enter your class')
    marks=int(input("Enter your marks"))
    s_data=[rno,name,clas,marks]
    pickle.dump(s_data,f1)
    f1.close()
    return 
def read_data():
    f1=open("ABC.dat","rb")
    s_data= pickle.load(f1)
    while s_data:
        print(s_data)
        s_data=pickle.load(f1)
    print("EOF reached")
    f1.close()
    return
def search_file():
    return
while True:
    print("Student file operations\n    A:Add a new record\n    B:View all records\n    C:Search for a record\n     D:Exit")
    x=input("Enter your option").lower()
    if x=="a":   
        add_data()
        y=input("Add one more?")
        if y=="n":
            break
    elif x=="b":
        read_data()
    elif x=="c":
        search_file():
    elif x=="d":
        print("breaking")
        break
    else:
        print("invalid input!")