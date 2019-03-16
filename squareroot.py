# Benson Thomas John, 2019
# Program that takes a positive ﬂoating point number as input and outputs an approximation of its square root.


# import the math module  
import math  

user_num = float(input("Please enter a positive number: "))  

# Referenced : https://docs.python.org/3/library/math.html

# Stores the square root of user_num to square_root
square_root = math.sqrt(user_num)

# Print the approximation of square_root using round method with 1 decimal place
print("The square root of", user_num, "is approx.", round(square_root, 1))
