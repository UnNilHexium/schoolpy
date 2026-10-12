import csv

def write_single_record():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    designation = input("Enter Designation: ")
    salary = input("Enter Salary: ")
    
    with open("employee.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([emp_id, name, designation, salary])
        
def write_all_records():
    records = []
    n = int(input("How many records do you want to enter? "))
    
    for i in range(n):
        print("--- Details for Employee ", i+1 , " ---")
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        salary = input("Enter Salary: ")
        records.append([emp_id, name, designation, salary])
    
    with open("employee.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["EmpID", "Name", "Designation", "Salary"])
        writer.writerows(records)
        
def display_records():
    try:
        with open("employee.csv", "r") as f:
            reader = csv.reader(f)
            print("\n" + "=" * 40)
            print(f"{'EmpID':<10} {'Name':<12} {'Designation':<15} {'Salary':<10}")
            print("=" * 40)
            
            for row in reader:
                if row:
                    print(f"{row[0]:<10} {row[1]:<12} {row[2]:<15} {row[3]:<10}")
                                
    except FileNotFoundError:
        print("\nError: 'employee.csv' does not exist yet! Add records first.\n")


while True:
    print("***** EMPLOYEE CSV MANAGEMENT *****")
    print("Write a single record (Append) - 1")
    print("Write all records in one go (Overwrite) - 2")
    print("Display all records - 3")
    print("Exit - 4")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        write_single_record()
    elif choice == "2":
        write_all_records()
    elif choice == "3":
        display_records()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.\n")