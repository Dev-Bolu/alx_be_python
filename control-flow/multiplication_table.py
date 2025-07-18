number = int(input("Enter a number to see its multiplication table: "))
z = 0
for i in range(1, 11):
    z = number * i
    print(f"{number} x {i} = {z}")