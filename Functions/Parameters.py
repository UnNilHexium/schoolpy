#Positional param - position of argments / order in which they are passed matters
#                 - they are required, as in, complulsary to pass, lest you will get an error
#Default param    - when a param is set to a default value in the function definition
#                 -  thus, if non existant, it need not be passed

def area_p(l,b=5):
    a=l*b
    p=2*(l+b)
    print("area = ",a,"perimeter = ",p)
    return
x=int(input("Enter length: "))
y=input("Enter Breadth(defult=5): ")
if y == '':
    area_p(x)
else :
    y= int(y)
    area_p(x,y)
