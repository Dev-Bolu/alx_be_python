
from datetime import datetime, timedelta

def  display_current_datetime():
    current_date = datetime.now()
    
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
    
    
def calculate_future_date(): 


    number_of_days = int(input("Enter number of days to add to the current date: "))
    future_date =datetime.now() + timedelta(days=number_of_days)
    formatted_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date after {number_of_days} days: {formatted_date}")

display_current_datetime()
calculate_future_date()
