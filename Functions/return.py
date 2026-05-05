#we can return values in a funtion
#this helps the calling statement use the returned values
#you can return multiple values too
#they can later be asigned global variable
# -one local variable assigned to  multiple retunred variables
#       -
# -all variables assigned one variable each
#you can return as tuple and unpack

def f1(n):
    f=1
    for i in range(1,n+1):
        f=f*1
    return f,g,h