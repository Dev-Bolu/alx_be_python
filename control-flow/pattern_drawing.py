pattern_size = int(input("Enter the size of the pattern: "))
row = 0
while row < pattern_size:
    for col in range(pattern_size):
        print("*", end="")
    print()  # Move to the next line after printing one row
    row += 1