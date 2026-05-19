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
    i=1
    while True:
        try:
            s_data=pickle.load(f1)
            print(i, "|  R. no: ", s_data[0],"|    Name: ",s_data[1],"|      class: ",s_data[2],"|   marks:",s_data[3])
            i+=1
            
        except:
            break
    print("number of entries = ", i)
    print("EOF reached")
    f1.close()
    return
def search_file():
    print("what do you want to search? \nR: roll number \nC: Class)")
    x=input("Enter Option : ").lower()
     if x=="r":
        search_rno()
    elif x=="c":
        search_class()
    else:
        print("invalid input!")
    return
def search_rno():
    f1=open("ABC.dat","rb")
    r=int(input("Please enter roll number : "))
    found=False
    while True:
        try:
            s_data=pickle.load(f1)
            if r==s_data[0]:
                 print("|  R. no: ", s_data[0],"|    Name: ",s_data[1],"|      class: ",s_data[2],"|   marks:",s_data[3])
        except:

    return
def search_class():
    return
while True:
    print("Student file operations\n    A:Add a new record\n    B:View all records\n    C:Search for a record\n    D:Exit")
    x=input("Enter your option : ").lower()
    if x=="a":   
        while True:
            add_data()
            y=input("Add one more? ")
            if y=="n":
                break
    elif x=="b":
        read_data()
    elif x=="c":
        search_file()
    elif x=="d":
        print("breaking")
        break
    else:
        print("invalid input!")
