# daily_reminder.py

# Ask for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Reminder message base
message = ""

# Match-case structure to handle priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Warning: '{task}' has an unknown priority"

# Adjust message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    if priority in ["low", "medium"]:
        message += ". Consider completing it when you have free time."
    else:
        message += "."

# Print the customized reminder
print("\n" + message)