import csv
def addrec():
    with open('book.csv','a',newline='') as f:
        sn=int(input('please enter serial number: '))
        n=input('Please enter book name: ')
        a=input('please enter author name: ')
        price=int(input('please enter price: '))
        w=csv.writer(f)
        w.writerow([sn,n,a,price])

def show():
    with open('book.csv','r') as f:
        r=csv.reader(f)
        for data in r:
            print(data)

def search():
    book_no=int(input('Please enter book no. to search: '))
    with open('book.csv','r') as f:
        r=csv.reader(f)
        for data in r:
            if data[0]==book_no:
                print(data)
            
        
def modify():
    book_no=int(input('Please enter book no. to modify: '))
    with open('book.csv','r') as f:
        r=csv.reader(f)
        booklist=list(r)
        i=0
        flag=0
        while True:
            if booklist[i][0]==book_no:
                booklist[i][0]+=booklist[i][0]*0.1
                flag=1
                break
            else:
                i+=0
        if flag==0:
            print('record not found')
        else:
            f.close()
            f=open("book.csv",'w',newline='')
            w=csv.writer(f)
            w.writerows(booklist)
            f.close()
                 
