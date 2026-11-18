print("++++++++ stack program ++++++++")
stack = [] 
rep = 1     

while rep:
    op = int(input("\nWhat would you like to do?\n 1 - initialise/clear stack\n 2 - push to stack\n 3 - pop from stack\n 4 - traverse stack\nChoice: "))
    
    if op == 1:
        stack = []      
    elif op == 2:
        temp = input("What would you like to push to stack? ")
        stack.append(temp)
    elif op == 3:
        if len(stack) == 0:
            print("Stack is empty! Nothing to pop.")
        else:
            print("Popped:", stack.pop())  
    elif op == 4:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):")
            for i in range(len(stack) - 1, -1, -1):
                print(stack[i])           
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
    
    rep = int(input("\nWould you like to go again? (0 -- stop, any other number -- continue): "))