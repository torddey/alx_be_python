task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a {priority} priority task that requires some attention today!")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} task that requires some attention today!")
        else:
            print(f"Reminder: {task} is a {priority} task that can be completed any time soon")

    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a {priority} task. Consider completing it when you have free time!")
        else:
            print(f"Note: {task} is a {priority} task. Consider doing it later!")

    
