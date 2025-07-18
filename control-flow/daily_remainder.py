Task= input("Enter your task : ").strip()
Priority = input("Priority (high/medium/low): ").strip().lower()
Time_Bound = input("Is it time-bound? (yes/no) : ").strip().lower()
match Priority:
    case "high":
        if Time_Bound == "yes":      
            print(f"Reminder: {Task} is a {Priority} priority that requires immediate attention today!")
        else:
            print(f"Note: {Task} is marked as {Priority} priority. Consider completing it when you have free time.")
    case "medium":
        if Time_Bound == "yes":      
            print(f"Reminder: {Task} is a {Priority} priority that requires immediate attention today!")
        else:
            print(f"Note: {Task} is marked as {Priority} priority. Consider completing it when you have free time.")
            
    case "low":
        if Time_Bound == "yes":      
            print(f"Reminder: {Task} is a {Priority} priority that requires immediate attention today!")
        else:
            print(f"Note: {Task} is marked as {Priority} priority. Consider completing it when you have free time.")
            
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")