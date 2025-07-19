# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = ""
"""
# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += ". Consider completing it when you have free time."
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += ". Consider completing it when you have free time."
    case "low":
        reminder_message = f"Note: '{task}' is a low priority task"
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += ". Consider completing it when you have free time."
    case _:
        reminder_message = f"'{task}' has an unrecognized priority level."
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += " Consider completing it when you have free time."

# Provide a customized reminder
print(f"\n {reminder_message}")
"""
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