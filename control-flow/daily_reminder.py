# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = ""

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder_message = f"'{task}' is a **high priority** task"
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += ". Aim to complete it as soon as possible."
    case "medium":
        reminder_message = f"'{task}' is a **medium priority** task"
        if time_bound == "yes":
            reminder_message += " that you should prioritize today."
        else:
            reminder_message += ". Plan to work on it soon."
    case "low":
        reminder_message = f"'{task}' is a **low priority** task"
        if time_bound == "yes":
            reminder_message += ". Try to get it done today if possible."
        else:
            reminder_message += ". Consider completing it when you have free time."
    case _:
        reminder_message = f"'{task}' has an unrecognized priority level."
        if time_bound == "yes":
            reminder_message += " However, it is time-bound, so try to address it today!"
        else:
            reminder_message += " Please clarify its priority."

# Provide a customized reminder
print(f"\nReminder: {reminder_message}")
