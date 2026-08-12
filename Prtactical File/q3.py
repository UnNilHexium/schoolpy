def get_row(order,i):
    print("Please enter the elements of the row ",i,", each value seterated by a comma -")
    n=input()
    row=[int(num) for num in n.split(',')]
    if len(row) != order:
        print("please enter correct number of elements")
        return get_row(order,i)
    return(row)    

def create_matrix():
    print("please enter a square matrix")
    matrix=[]
    order=int(input("Please enter order of the matrix (eg. 3)"))
    for i in range(order):
        matrix.append(get_row(order,i))
    return matrix

def sum_r(matrix):
    sums=()
    for i in range(len(matrix)):
        sums = sums + (sum(matrix[i]),)
    return sums

def sum_c(matrix):
    sums=()
    for j in range(len(matrix)):
        x=0
        for i in range(len(matrix)):
            x+=matrix[i][j]
        sums = sums + (x,)
    return sums

def sum_d(matrix):
    sum=0
    for i in range(len(matrix)):
        sum+=matrix[i][i]
    return sum

def transpose(matrix):
    
    matrix_t=[]
    for i in range(len(matrix)):
        row=[]
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        matrix_t.append(row)
    return matrix_t
    
def sum_m(matrix1,matrix2):
    sum_matrix=[[matrix1[i][j]+matrix2[i][j] for j in range(min(len(matrix1),len(matrix2))) ] for i in range(min(len(matrix1), len(matrix2)))]
    return sum_matrix

def diff_m(matrix1,matrix2):
    diff_matrix=[[matrix1[i][j]-matrix2[i][j] for j in range(min(len(matrix1),len(matrix2))) ] for i in range(min(len(matrix1), len(matrix2)))]
    return diff_matrix

def mat_def():
    print("please create matrix 1")
    matrix1=create_matrix()
    print("please create matrix 2")
    matrix2=create_matrix()
    return matrix1, matrix2

def main(matrix1,matrix2):
    mat_choice=input("what matrix would you like to work on?(matrix1, matrix2)")
    if mat_choice not in ("matrix1", "matrix2"):
        print('please choose correctly! restarting ..')
        main()
    if mat_choice=="matrix1":
        mat_choice=matrix1
    else:
        mat_choice=matrix2
    function=int(input("""what would you like to do to this matrix-
    - sum of row -1 
    - sum of column -2
    - sum of diagonal -3
    - transpose -4
    - sum with other matrix -5
    - difference with other matrix -6"""))
    if function not in range(1,7):
        print('please choose valid funtion. restarting...')
        main()
    else:
        match function:
            case 1:
                print(sum_r(mat_choice))
            case 2:
                print(sum_c(mat_choice))
            case 3:
                print(sum_d(mat_choice))
            case 4:
                transp=transpose(mat_choice)
                for i in transp:
                    print(i)
            case 5:
                a=sum_m(matrix1,matrix2)
                for i in a:
                    print(i)
            case 6:
                a=diff_m(matrix1,matrix2)
                for i in a:
                    print(i)
    global y 
    y = int(input("go again (yes-1, no-0)"))

y=1    
matrix1, matrix2 = mat_def()      
while y:
    main(matrix1, matrix2)