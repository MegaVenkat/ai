stack1 = []
stack2 = []
i = 0
while(i == 0):
    ch = int(input("Press 1 to add element in stack1,2 to pop element from stack1, 3 to add element in stack2 and 4 to remove element from stack2 : "))
    if ch == 1:
        val = int(input("Enter value to add in stack 1 : "))
        stack1.append(val)
    elif ch == 2:
        if len(stack1) == 0:
            print("Stack Underflows !")
        else:
            val = stack1.pop()
            print("Element removed from stack 1 is : "+str(val))
    elif ch == 3:
        val = int(input("Enter value to add in stack 2 : "))
        stack2.append(val)
    elif ch == 4:
        if len(stack1) == 0:
            print("Stack Underflows !")
        else:
            val = stack2.pop()
            print("Element removed from stack 2 is : "+str(val))
    else:
        print("Invalid Choice !")
    print("Stack1 : "+str(stack1))
    print("Stack2 : "+str(stack2))
    i = int(input("Press 0 to continue......"))
