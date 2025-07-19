task= input("Enter your task : ").strip()
priority = input("Enter the priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound, yes/no : ").strip().lower()
match priority:
    case "high":
        if time_bound == "yes":      
            print(f"{task} is marked as {priority} priority that requires immediate attention today!")
        else:
            print(f"{task} is marked as {priority} priority. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":      
            print(f"{task} is marked as {priority} priority that requires immediate attention today!")
        else:
            print(f"{task} is marked as {priority} priority. Consider completing it when you have free time.")
            
    case "low":
        if time_bound == "yes":      
             print(f"{task} is marked as {priority} priority that requires immediate attention today!")
        else:
            print(f"{task} is marked as {priority} priority. Consider completing it when you have free time.")
            
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")