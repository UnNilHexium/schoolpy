import csv
def addrec():
    with open('book.csv','a',newline='') as f:
        w=csv.writer(f)
        bookrec=[['a','b','c','d'],['e','f','g','h'],['i','j','k','l']]
        w.writerows(bookrec)

addrec()
