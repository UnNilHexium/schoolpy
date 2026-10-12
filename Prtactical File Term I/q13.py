import csv
import os

FILENAME = "student.csv"

def create_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            pass
        print("File created successfully.")
    else:
        print("File already exists.")

def append_records():
    n = int(input("How many records to add? "))
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        for i in range(n):
            print(f"Record {i + 1}:")
            rno = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            theory = float(input("Enter Theory Marks: "))
            prac = float(input("Enter Prac Marks: "))
            writer.writerow([rno, name, theory, prac])
    print("Record(s) appended successfully.")

def display_records():
    if not os.path.exists(FILENAME):
        print("File does not exist.")
        return
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        found = False
        for row in reader:
            if row:
                found = True
                rno = int(row[0])
                name = row[1]
                theory = float(row[2])
                prac = float(row[3])
                total = theory + prac
                result = "PASS" if total > 40 else "FAIL"
                print(f"RNo: {rno}, Name: {name}, Theory: {theory}, Prac: {prac}, Total: {total}, Result: {result}")
        if not found:
            print("File is empty.")

def update_marks():
    if not os.path.exists(FILENAME):
        print("File does not exist.")
        return
    rows = []
    updated = False
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                theory = float(row[2])
                if 35 < theory < 41:
                    row[2] = theory + 5
                    updated = True
                rows.append(row)
    
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    if updated:
        print("Theory marks updated for eligible students.")
    else:
        print("No students met the criteria for mark increase.")

def result_summary():
    if not os.path.exists(FILENAME):
        print("File does not exist.")
        return
    
    totals = []
    pass_count = 0
    fail_count = 0
    
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                theory = float(row[2])
                prac = float(row[3])
                total = theory + prac
                totals.append(total)
                if total > 40:
                    pass_count += 1
                else:
                    fail_count += 1

    appeared = len(totals)
    if appeared == 0:
        print("No records available to generate summary.")
        return

    max_total = max(totals)
    min_total = min(totals)
    avg_total = sum(totals) / appeared
    pass_percent = (pass_count / appeared) * 100

    print("Students appeared:", appeared)
    print("Max Total:", max_total)
    print("Min Total:", min_total)
    print("Average Total:", avg_total)
    print("PASS:", pass_count)
    print("FAIL:", fail_count)
    print("PASS%:", pass_percent)

while True:
    print("\n--- MENU ---")
    print("1. Create File")
    print("2. Append Record(s)")
    print("3. Display Data with Total & Result")
    print("4. Increase Theory Marks")
    print("5. Display Result Summary")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")
    
    if choice == "1":
        create_file()
    elif choice == "2":
        append_records()
    elif choice == "3":
        display_records()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        result_summary()
    elif choice == "6":
        break
    else:
        print("Invalid choice, try again.")