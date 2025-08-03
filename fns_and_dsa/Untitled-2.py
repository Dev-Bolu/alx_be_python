file = "cat.txt"
try :
    with open(file,"r") as f:
        content = f.read()
        print(content)

except FileNotFoundError as e:
    print(f"Error: {e}")
    print(f"Error: {e}" )