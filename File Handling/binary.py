#use pickle library for binary
#dump()--> serialisation/pickling

#load()--> deserialisation/unpickling


import pickle

def write_bin():
    f = open("book.dat",'ab')
    bno=int(input('Enter Book Number: '))
    bname=input('Please Enter Book Name: ')
    aname=input('Please Enter Autor Name: ')
    price=int(input('Please enter price'))
    brecord=[bno,bname,aname,price]
    pickle.dump(brecord,f)
    f.close()

def go():
    y=input("go again?(y/n):  ").lower
    if y == 'y':
        return 1
    elif y == 'n':
        return 0
    else:
        print('invalid input, please try again')
        retun go()


def read_bin():
    try:
        f=open('book.dat',"rb")
    except FileNotFoundError:
        print('File does not exist!!')
    else:
        while True:
            try:
                record=pickle.load(f)
                print("Book no, Name, Author, Price")
                print("--",record[0],record[1],record[2],record[3])
            except EOFError:
                print('EOF reached')
                f.close()
                break



def do():
    y=input("what do you wish to do?(Read file: r, Write to file: w):  ").lower
    if y == 'r':
        return 1
    elif y == 'w':
        return 2
    else:
        print('invalid input, please try again')
        retun do()


def main():
    x=do()
    if x == 1:
        read_bin()
        while go():
            print('Printing record again-')
            read_bin()
    elif x == 2:
        write_bin()
        while go():
            write_bin()
    print('Exiting....')

main()        