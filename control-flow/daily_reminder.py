# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high":
        if time_bound == "yes":      
            print(f"Reminder: {task} is a {priority} priority that requires immediate attention today!")
        else:
            print(f"Note: {task} is marked as {priority} priority. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":      
            print(f"Reminder: {task} is a {priority} priority that requires immediate attention today!")
        else:
            print(f"Note: {task} is marked as {priority} priority. Consider completing it when you have free time.")
            
    case "low":
        if time_bound == "yes":      
            print(f"Reminder: {task} is a {priority} priority that requires immediate attention today!")
        else:
            print(f"Note: {task} is marked as {priority} priority. Consider completing it when you have free time.")
            
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")