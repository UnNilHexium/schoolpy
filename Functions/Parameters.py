#Positional param - position of argments / order in which they are passed matters
#                 - they are required, as in, complulsary to pass, lest you will get an error
#Default param    - when a param is set to a default value in the function definition
#                 -  thus, if non existant, it need not be passed
#Keyword param    - explicitly state what parameter is assigned what parameter
#                 - position does not really matter, among the keyword parameters themselvs
#                 - position should be taken care of in priority order
#                 - overcomes the problem of having to rember order of passing parameters
#priority order is- positional, keyword, default

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
# area_per(5,l=4) raises an error

area_p(b=4,l=1) # notice positions are switched, but explicit difining make it ok!