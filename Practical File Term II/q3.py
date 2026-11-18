import mysql.connector as m

try:
    mycon = m.connect(user="root", host="localhost", password="")
except:
    print("Default Credentials Invalid ! \nExiting!")
    exit()

mycur = mycon.cursor()

mycur.execute("Create database if not exists stock;")

mycur.execute("use stock;")

sql = """create table if not exists products (
Pno integer(6) primary key,
Pname varchar(20) not null, 
Rate integer(5) not null,
QOH integer(4)
);"""

mycur.execute(sql)

def execute(sql):
    try:
        mycur.execute(sql)
        mycon.commit()
    except:
        print("Invalid input. Try again!")
        return

def define_column():
    n = input("Column name - ")
    d = input("datatype in sql syntax - ")
    f = input("any flags and conditions, in sql syntax - ")
    return (n, d, f)

def alter():
    print("What action do you want to take?")
    print("1. Add Column")
    print("2. Modify Column")
    print("3. Drop Column")
    action = int(input("Enter choice (1, 2, or 3): "))

    if action == 1:
        details = define_column()
        sql = "ALTER TABLE products ADD COLUMN %s %s %s;" % details

    elif action == 2:
        col_name = input("Enter the column name to modify: ")
        new_type = input("Enter the new data type (e.g., VARCHAR(100) NOT NULL): ")
        sql = "ALTER TABLE products MODIFY COLUMN %s %s;" % (col_name, new_type)

    elif action == 3:
        col_name = input("Enter the column name to drop: ")
        sql = "ALTER TABLE products DROP COLUMN %s;" % (col_name,)

    else:
        print("Invalid option selected.")
        return

    execute(sql)

def update_tbl():
    mycur.execute("desc products")
    print(mycur.fetchall())
    col = input("Enter column to change : ")
    val = input("Enter values to update, in sql syntax, comma seperated :")
    cond = input("Enter any conditions , in sql syntax ")
    sql = '''update products
    set ''' + col + '=' + val + ' where ' + cond + ";"
    execute(sql)

def order_by():
    mycur.execute("desc products")
    print(mycur.fetchall())
    field = input("Enter field to order by")
    order = input("'A' - Ascending\n'D' - Descending").lower()
    if order == "a":
        order = "Asc"
    elif order == "d":
        order = "DESC"
    else:
        print("invalid input. try again!")
        return
    sql = '''select * from products
    order by ''' + field + " " + order + ";"
    try:
        mycur.execute(sql)
        for row in mycur.fetchall():
            print(row)
    except:
        print("Invalid input. Try again!")

def delete_from():
    mycur.execute("desc products")
    print(mycur.fetchall())
    cond = input("enter deletion condition (eg. Pno = 12345)")
    sql = '''Delete from products
    where %s ;''' % (cond,)
    execute(sql)

def group_info():
    mycur.execute("desc products")
    print(mycur.fetchall())
    category = input("what category would you like to group by? ")
    op1 = input("on what would you like to apply min, max, sum, and average function? ")
    inputs = (category, op1, op1, op1, op1, category)
    sql = '''select 
    %s,
    min(%s) as min,
    max(%s) as max,
    sum(%s) as sum,
    avg(%s) as average,
    count(*) as count
    from products
    Group by %s;''' % inputs
    try:
        mycur.execute(sql)
        for row in mycur.fetchall():
            print(row)
    except:
        print("Invalid input. Try again!")

print("++++++++ Stock List ++++++++")
rep = 1

while rep:
    op = int(input("\nWhat would you like to do?\n 1 - Alter Table Structure/Definition\n 2 - Update Table Records\n 3 - Order By ascending/descending\n 4 - Delete Records\n 5 - Group by min, max, sum, count and average\nChoice: "))

    if op == 1:
        alter()
    elif op == 2:
        update_tbl()
    elif op == 3:
        order_by()
    elif op == 4:
        delete_from()
    elif op == 5:
        group_info()
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")

    rep = int(input("\nWould you like to go again? (0 -- stop, any other number -- continue): "))