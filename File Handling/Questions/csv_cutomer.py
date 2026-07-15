import csv

def add():
    with open('cust.csv','a',newline='') as f:
        w=csv.writer(f)
        cust_no=int(input('Please enter customer number: '))
        cust_name=input('Please enter customer name: ')
        address=input('Please enter customer address: ')
        ph=int(input('Please enter customer phone number: '))
        w.writerow([cust_no,cust_name,address,ph])

def show():
    with open('cust.csv','r') as f:
        r=csv.reader(f)
        for data in r:
            print("--",data[0]," | ",data[1]," | ",data[2]," | ",data[3]," | ")

def search():
    with open('cust.csv','r') as f:
        r=csv.reader(f)
        cust_list=list(r)
    
    found = False
    search=input('Please enter Customer Number: ')
    for data in cust_list:
        if i[0] == search:
            print("--",data[0]," | ",data[1]," | ",data[2]," | ",data[3]," | ")
            found = True
    if not found:
        print('No record found')

def modify():
    with open('cust.csv','r') as f:
        r=csv.reader(f)
        cust_list=list(r)
    
    found = False
    search=input('Please enter Customer Number: ')
    newphn=input('Please enter new phone phone: ')
    temp=[]
    for data in cust_list:
        if i[0] == search:
            i[4]=newphn
            found = True
    if not found:
        print('No record found')
    else:
        with open('cust.csv','a',newline='') as f:
            w=csv.writer(f)
            w.writerows(temp)


def delete():
    with open('cust.csv','r') as f:
        r=csv.reader(f)
        cust_list=list(r)
    
    found = False
    search=input('Please enter Customer Number to remove: ')
    temp=[]
    for data in cust_list:
        if i[0] == search:
            continue
            found = True
        else:
            temp.append(i)
    if not found:
        print('No record found')
    else:
        with open('cust.csv','a',newline='') as f:
            w=csv.writer(f)
            w.writerows(temp)