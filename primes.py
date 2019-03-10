# Benson Thomas John, 2019
# Program that asks the user to input a positive integer and tells the user whether or not the number is a prime. 

#Prompt user input and convert the user_input to integer
user_input = int(input("Please enter a positive integer: "))

# Referenced: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/


# If user_input is greater than one
if user_input > 1:
    # Creating for loop to range throught the values starting 2 to user_input
    for num in range(2, user_input):

        # Check to see if user_input is dvisible, if so then not a prime number
        if (user_input % num) == 0:
            print("That is not a prime number")
            break
    else:
            # loop fell through without finding a factor
            print("That is a prime number")

else: 
    print("That is not a prime number")