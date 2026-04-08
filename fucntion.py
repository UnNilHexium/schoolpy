def area_p(l,b=5):
    a=l*b
    p=2*(l+b)
    print("area = ",a,"perimeter = ",p)
    return
x=int(input("Enter length: "))
y=int(input("Enter Breadth(defult=5): "))
area_p(x,y)
area_p(x)