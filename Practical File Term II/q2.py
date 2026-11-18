print("++++++++ Member List ++++++++")
stack = [] 
rep = 1     

while rep:
    op = int(input("\nWhat would you like to do?\n 1 - initialise/clear stack\n 2 - push to stack\n 3 - pop from stack\n 4 - traverse stack\nChoice: "))
    
    if op == 1:
        stack = []      
    elif op == 2:
        Member_no = int(input("Please enter member number: "))
        Member_Name = input("Please enter Member Name: ")
        Age = int(input("Please input member age"))
        temp = (Member_no, Member_Name, Age)
        stack.append(temp)
    elif op == 3:
        if len(stack) == 0:
            print("Stack is empty! Nothing to pop.")
        else:
            print("Member Number \t Member Name \t Member Age")
            temp= stack.pop()
            print(temp[0], "\t\t\t" , temp[1], "\t\t\t" , temp[2])  
    elif op == 4:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Member Number \t Member Name \t Member Age")
            for i in range(len(stack) - 1, -1, -1):
                temp= stack[i]
                print(temp[0], "\t\t\t" , temp[1], "\t\t\t" , temp[2]) 
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
    
    rep = int(input("\nWould you like to go again? (0 -- stop, any other number -- continue): "))