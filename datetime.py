import datetime

present_time = datetime.datetime.now()


# Reference: https://stackoverflow.com/a/52045942


def suffix(day_num):
    
    date_suffix = ["th", "st", "nd", "rd"]

    if day_num % 10 in [0, 1, 2, 3] and day_num not in [11, 12, 13]:
        return date_suffix[day_num % 10]
    else:
        return date_suffix[0]

num = int(present_time.strftime("%d"))

am_pm = present_time.strftime("%p").lower()
strip_lead = present_time.strftime("%I").lstrip('0')

print(present_time.strftime("%A, %B %d" + suffix(num) + " %Y" + " at " + strip_lead + ":%M" + am_pm))


# Referenced: https://www.w3schools.com/python/python_datetime.asp
# http://strftime.org/
# https://stackoverflow.com/q/38142478