# operations.py

def add(*args):
    result = [0]
    for num in args:
        result += num
    return result

def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result                                                                              (args)

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
    

def divide(*args):
    if not args:
        return "No number provided"
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error: Division by zero"
        result /= num
        return result

        
    
    