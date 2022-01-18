def create_stack():
    stack = []
    return stack


def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("Pushed item is: " + str(item))


def pop(stack):
    if (check_empty(stack)):
        return -1

    return stack.pop()


stack = create_stack()
push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)
print("popped item: " + str(pop(stack)))
print("stack after popping an element: " + str(stack))
