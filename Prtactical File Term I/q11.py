import pickle
data = [
    ("Car", 4),
    ("Bike", 2),
    ("Truck", 6),
    ("Autorickshaw", 3),
    ("Bicycle", 2)
]

with open("SPEED.DAT", "wb") as f:
    for record in data:
        pickle.dump(record, f)

def showfile():
    count = 0
    with open("SPEED.DAT", "rb") as f:
        try:
            while True:
                record = pickle.load(f)
                print("Vehicle Type:", record[0], "| Wheels:", record[1])
                count += 1
        except EOFError:
            pass
            
    print("Total records found:", count)

showfile()