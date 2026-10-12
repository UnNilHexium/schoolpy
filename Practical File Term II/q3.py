import mysql.connector as m 

try:
    mycon = m.connector(user="root", host="localhost", password="")
else:
    print("Defalut Credentials Invalid ! \nExiting!")

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

def define_column():
    n = input("Column name - ")
    d = input("datatype in sql syntax - ")
    f = input ("any flags and conditions, in sql syntax - ")
    return (n,f,d)

def alter():
    print("What action do you want to take?")
    print("1. Add Column")
    print("2. Modify Column")
    print("3. Drop Column")
    action = int(input("Enter choice (1, 2, or 3): "))

    if action == 1:
        # Assuming define_column() returns: (col_name, data_type, details)
        col_name, data_type, details = define_column()
        sql = f"ALTER TABLE products ADD COLUMN {col_name} {data_type} {details}"

    elif action == 2:
        col_name = input("Enter the column name to modify: ")
        new_type = input("Enter the new data type (e.g., VARCHAR(100) NOT NULL): ")
        sql = f"ALTER TABLE products MODIFY COLUMN {col_name} {new_type}"

    elif action == 3:
        col_name = input("Enter the column name to drop: ")
        sql = f"ALTER TABLE products DROP COLUMN {col_name}"

    else:
        print("Invalid option selected.")
        return None

    print(f"\nGenerated Query:\n{sql}")
    return sql
