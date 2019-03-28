# Benson Thomas John, 2019
# Program that outputs whether or not today is a day that begins with the letter T. 

# Referenced: https://docs.python.org/3/library/datetime.html?highlight=date#module-datetime

# import date class from datetime module
from datetime import date

# returns the number for today, 1 for Monday, 2 for Tuesday, etc.
day = date.today().weekday()

#Check whether the day either Tuesday or Thursday
if(day == 1 or day == 3):
    print("Yes - today begins with a T")
# Else prints No
else:
    print("No - today doesn't begin with a T")
