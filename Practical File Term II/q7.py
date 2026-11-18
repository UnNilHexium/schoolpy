import mysql.connector as m

try:
    mycon = m.connect(user="root", host="localhost", password="")
except:
    print("Default Credentials Invalid ! \nExiting!")
    exit()

mycur = mycon.cursor()

mycur.execute("CREATE DATABASE IF NOT EXISTS company;")
mycur.execute("USE company;")

sql = """CREATE TABLE IF NOT EXISTS employee (
EmpNo INT PRIMARY KEY,
EName VARCHAR(30) NOT NULL,
Dept VARCHAR(20),
Salary INT
);"""
mycur.execute(sql)

def execute(sql):
    try:
        mycur.execute(sql)
        mycon.commit()
        print("Operation successful!")
    except:
        print("Invalid input or record error. Try again!")

def add_emp():
    eno = int(input("Enter Employee Number: "))
    ename = input("Enter Employee Name: ")
    dept = input("Enter Department: ")
    sal = int(input("Enter Salary: "))
    sql = "INSERT INTO employee VALUES (%s, '%s', '%s', %s);" % (eno, ename, dept, sal)
    execute(sql)

def modify_emp():
    eno = int(input("Enter Employee Number to modify: "))
    print("What would you like to modify?")
    print("1. Name")
    print("2. Department")
    print("3. Salary")
    ch = int(input("Enter choice (1, 2, or 3): "))
    
    if ch == 1:
        val = input("Enter new Name: ")
        sql = "UPDATE employee SET EName = '%s' WHERE EmpNo = %s;" % (val, eno)
    elif ch == 2:
        val = input("Enter new Department: ")
        sql = "UPDATE employee SET Dept = '%s' WHERE EmpNo = %s;" % (val, eno)
    elif ch == 3:
        val = int(input("Enter new Salary: "))
        sql = "UPDATE employee SET Salary = %s WHERE EmpNo = %s;" % (val, eno)
    else:
        print("Invalid choice!")
        return
        
    execute(sql)

def delete_emp():
    eno = int(input("Enter Employee Number to delete: "))
    sql = "DELETE FROM employee WHERE EmpNo = %s;" % (eno,)
    execute(sql)

def view_all():
    mycur.execute("SELECT * FROM employee;")
    records = mycur.fetchall()
    if len(records) == 0:
        print("No records found.")
    else:
        print("EmpNo \t EName \t\t Dept \t\t Salary")
        for row in records:
            print(row[0], "\t", row[1], "\t\t", row[2], "\t\t", row[3])

def view_selective():
    print("Search by:")
    print("1. Employee Number")
    print("2. Department")
    ch = int(input("Enter choice (1 or 2): "))
    
    if ch == 1:
        eno = int(input("Enter Employee Number: "))
        sql = "SELECT * FROM employee WHERE EmpNo = %s;" % (eno,)
    elif ch == 2:
        dept = input("Enter Department: ")
        sql = "SELECT * FROM employee WHERE Dept = '%s';" % (dept,)
    else:
        print("Invalid choice!")
        return
        
    mycur.execute(sql)
    records = mycur.fetchall()
    if len(records) == 0:
        print("No matching records found.")
    else:
        print("EmpNo \t EName \t\t Dept \t\t Salary")
        for row in records:
            print(row[0], "\t", row[1], "\t\t", row[2], "\t\t", row[3])

print("++++++++ Employee Management System ++++++++")
rep = 1

while rep:
    op = int(input("\nWhat would you like to do?\n 1 - Add Employee\n 2 - Modify Employee\n 3 - Delete Employee\n 4 - View All Records\n 5 - View Selective Records\nChoice: "))
    
    if op == 1:
        add_emp()
    elif op == 2:
        modify_emp()
    elif op == 3:
        delete_emp()
    elif op == 4:
        view_all()
    elif op == 5:
        view_selective()
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")
        
    rep = int(input("\nWould you like to go again? (0 -- stop, any other number -- continue): "))

mycon.close()