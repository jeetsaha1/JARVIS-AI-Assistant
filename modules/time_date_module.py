from datetime import datetime

def get_time():
    return f"The current time is {datetime.now().strftime('%I:%M %p')}."

def get_date():
    return f"Today’s date is {datetime.now().strftime('%d %B %Y')}."
