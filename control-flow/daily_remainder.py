Task= input("Enter your task : ").strip()
Priority = input("Enter the priority (high/medium/low): ").strip().lower()
Time_bound = input("Is it time-bound, yes/no : ").strip().lower()
match priority:
    case "high":
        if Time_bound == "yes":      
            print(f"{Task} is marked as {Priority} priority that requires immediate attention today!")
        else:
            print(f"{Task} is marked as {Priority} priority. Consider completing it when you have free time.")
    case "medium":
        if Time_bound == "yes":      
            print(f"{Task} is marked as {Priority} priority that requires immediate attention today!")
        else:
            print(f"{Task} is marked as {Priority} priority. Consider completing it when you have free time.")
            
    case "low":
        if Time_bound == "yes":      
             print(f"{Task} is marked as {Priority} priority that requires immediate attention today!")
        else:
            print(f"{Task} is marked as {Priority} priority. Consider completing it when you have free time.")
            
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")