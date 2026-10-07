import mysql.connector as c

mycon = m.connect(user="root", password="welcome", host="localhost")

mycur=mycon.cursor()

mycur.execute ("Create Database if nots exist Dummy;")

mycur.execute(Use Dummy;)

sql = '''create table if not exists Students (
Rno integer(2) primary key,
Name varchar(25) not null,
Class integer(2) between 1 and 12,
Section char(1) in ('A','B','C','D','E','F','G','H','I'),
Marks float(6,2) between 0 and 100
); '''

mycur.execute(sql)

def add_rec():
    Rno = int(input("Please enter roll number: "))
    Name = input("Please enter Name : ")
    Class = int(input("Please enter Class : "))
    Section = input("Please enter Section : ")
    Marks = float(input("Please enter Marks : "))
    Data = (Rno, Name, Class, Section, Marks)
    sql = '''insert into Students
    values (%s,%s,%s,%s,%s);'''
    mycur.execute(sql,Data)
    mycur.commit()
    
def del_rec():
    Rno = int(intput("please enter roll number to be destroyed : "))
    sql="Delete from Students where Rno=%s;"
    mycur.execute(sql,(Rno,))
    mycur.commit()

def upd_rec():
    Rno = int(input("Please enter roll number to be atomicaly altered, thier very composition broken and rebuilt (ORGANIC CHEMISTRY!!!!): "))
    Name = input("Please enter Name : ")
    Class = int(input("Please enter Class : "))
    Section = input("Please enter Section : ")
    Marks = float(input("Please enter Marks : "))
    Data = (Name, Class, Section, Marks,Rno)
    sql=''' Update Students
    set Name=%s, Class=%s, Section=s%, Marks=%s
    where Rno is %s;
    '''
    mycur.execute(sql, Data)
    mycur.commit()

def view_all():
    mycur.execute("Select * from Students;")
    data = mycur.fetchall()
    print(data)

def view_spec():
    Section = input("what section's data do you want to view? ")
    mycur.execute("Select * from Students where Section = %s;",(Section,))
    data = mycur.fetchall()
    print(data)
