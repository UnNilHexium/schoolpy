def get_row(order):
    n=input("Please enter the elements of the row ",i,", each value seterated by a comma -")
    row=[int(num) for num in n.split(',')]
    if len(row) != order:
        print("please enter correct number of elements")
        get_row(order)
    return(row)    

def sum_r():
    sums=()
    for i in matrix:
        sums = sums + (sum(matrix[i]))
        return sums

def sum_c(i):
    sums=()
    
    for j in matrix:
        x=0
        for i in matrix[j]:
            x+=i
        sums = sums + (x)
    return sums

def sum_d():
    sum=0
    for i in matrix:
        sum+=matrix[i][i]
    return sum

def transpose(matrix):
    matrix_t=[0 for i in ]
    for i in matrix

print("please enter a square matrix")

matrix=[]
order=int(input("Please enter order of the matrix (eg. 3)"))
for i in range(order):
    matrix.append(get_row(order))
    
