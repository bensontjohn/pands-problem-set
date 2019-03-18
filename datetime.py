# Benson Thomas John, 2019
# Program that outputs today’s date and time in the format "Monday,January 10th 2019 at 1:15pm". 

# import datetime module
import datetime

# Referenced: https://www.w3schools.com/python/python_datetime.asp

# stores present date and time
present_time = datetime.datetime.now()


# Reference: https://stackoverflow.com/a/52045942

# function to add suffix for the day number in the date
def suffix(day_num):
    # list of suffix
    date_suffix = ["th", "st", "nd", "rd"]
    # Check if day number present in first list and not in the second list
    if day_num % 10 in [0, 1, 2, 3] and day_num not in [11, 12, 13]:
        # returns the suffix if day_num is 0, 1, 2, 3
        return date_suffix[day_num % 10]
    else:
        return date_suffix[0]

# Referenced: # http://strftime.org/

# stores the day of the month as a zero-padded decimal number.
num = int(present_time.strftime("%d"))

# stores the lowercase of present time's AM or PM
am_pm = present_time.strftime("%p").lower()

# Referenced: http://www.datasciencemadesimple.com/strip-lstriprstrip-strip-function-python/
# remove the leading zero from the hour part of the present time
strip_lead = present_time.strftime("%I").lstrip('0')

# Prints the date and time as per the format mentioned at line 2
print(present_time.strftime("%A, %B %d" + suffix(num) + " %Y" + " at " + strip_lead + ":%M" + am_pm))




# https://stackoverflow.com/q/38142478
