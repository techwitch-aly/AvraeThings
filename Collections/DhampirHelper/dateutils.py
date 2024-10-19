def is_leap_year(year):
    # Check if the year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    # Days in each month, with February adjusted for leap years
    days_in_months = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_months[month - 1]

def unix_to_date(unix_timestamp):
    # Number of seconds in a day
    seconds_in_day = 86400
    
    # Start from the Unix epoch (January 1, 1970)
    days_since_epoch = unix_timestamp // seconds_in_day
    remaining_seconds = unix_timestamp % seconds_in_day
    
    year = 1970
    # Calculate the year
    while True:
        days_in_year = 366 if is_leap_year(year) else 365
        if days_since_epoch >= days_in_year:
            days_since_epoch -= days_in_year
            year += 1
        else:
            break
    
    # Calculate the month and day
    month = 1
    while True:
        days_in_current_month = days_in_month(year, month)
        if days_since_epoch >= days_in_current_month:
            days_since_epoch -= days_in_current_month
            month += 1
        else:
            break
    
    day = int(days_since_epoch + 1)  # Days are 1-based, not 0-based
    
    # Format the result as MM/dd/yyyy
    return f"{month:02d}/{day:02d}/{year}"