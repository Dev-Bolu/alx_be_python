class ValueTooHighError(Exception):
    def __init__(self,number):
        self.number = number
        super().__init__(f"Value {number} is too high.")
"""
    def __str__(self):       
        return f'Sorry, the number "{self.number}" is too high'
    """
num1 = int(input("Enter a number: "))
try:
    if num1 > 100:
        raise ValueTooHighError(num1)
    else:
        print(f"The number {num1} is within the acceptable range.")
except ValueTooHighError as e:
    print(e)
        