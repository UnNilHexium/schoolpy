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
    book_no=input('Please enter book no. to search: ')
    with open('book.csv','r') as f:
        r=csv.reader(f)
        for data in r:
            if data[0]==book_no:
                print(data)
            

 def modify():
    book_no = input('Please enter book no. to modify: ')
    

    with open('book.csv', 'r') as f:
        r = csv.reader(f)
        booklist = list(r)
    
    flag = 0
    
   
    for row in booklist:
        if row[0] == book_no:
            current_price = float(row[1])
            new_price = current_price + (current_price * 0.1)  
            row[1] = str(round(new_price, 2)) 
            flag = 1
            break  
            
    if flag == 0:
        print('Record not found')
    else:
        with open("book.csv", 'w', newline='') as f:
            w = csv.writer(f)
            w.writerows(booklist)

def modify():
    book_no=input('Please enter book no. to modify: ')
    with open('book.csv','r') as f:
        r=csv.reader(f)
        booklist=list(r)
        i=0
        flag=0
        while True:
            if str(booklist[i][0])==book_no:
                booklist[i][0]+=booklist[i][0]*0.1
                flag=1
                break
            else:
                i+=1
        if flag==0:
            print('record not found')
        else:
            f.close()
            f=open("book.csv",'w',newline='')
            w=csv.writer(f)
            w.writerows(booklist)
            f.close()
                 
