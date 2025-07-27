# operations.py (with consistent *args)

def add(*args):
    if not args:
        return 0
    result = 0
    for num in args:
        result += num
    return result

def subtract(*args):
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    if not args:
        return 1 # Start with 1 for multiplication
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    if not args:
        return "No number provided"
    if len(args) == 1:
        return args[0]
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error: Division by zero"
        result /= num
    return result