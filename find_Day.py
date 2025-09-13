from datetime import datetime

def get_day_of_week(date_str):
    """
    Takes a date string (YYYY-MM-DD) and returns the day of the week as a string.
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    day_name = date_obj.strftime("%A")
    return day_name

# Example usage
user_date = input("Enter a date (YYYY-MM-DD): ")
day = get_day_of_week(user_date)
print(f"The day is: {day}")