import pickle

products = [
    {"prod_code": "100", "prod_desc": "Keyboard", "stock":500},
    {"prod_code": "110", "prod_desc": "Satrun V", "stock":5},
    {"prod_code": "200", "prod_desc": "Toothpaste", "stock":100}
]

with open("PRODUCT.dat", "wb") as f:
    pickle.dump(products, f)

with open("PRODUCT.dat", "rb") as f:
    products = pickle.load(f)
prod_c_s=input("Please enter search value for prod_code- ")
prod_d_s=input("Please enter search value for prod_desc- ")

for i in products:
    if i["prod_code"]==prod_c_s and i["prod_desc"]==prod_d_s:
        print("record found!")
        n_stock=int(input("Please enter new stock for specified product- "))
        i["stock"]=n_stock

        with open("PRODUCT.dat","wb") as f:
            pickle.dump(products, f)
        
        break
    else:
        print("Record not found!")