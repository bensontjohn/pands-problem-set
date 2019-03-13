# Benson Thomas John, 2019
# Program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value bytakingthecurrentvalueand,ifitiseven,divideitbytwo,butifitisodd,multiply it by three and add one. Have the program end if the current value is one

# Take input from user and convert to integer
user_input = int(input("Please enter a positive integer: "))

# Referenced: Stack Overflow - https://stackoverflow.com/a/51457215
            : https://docs.python.org/3/tutorial/controlflow.html  - used this reference for end = ' ' used inside the print function
            

# Print initial value
print(user_input, end =' ')
            
# function which accepts user_input and performs calculation
def collatz(number):
    # Check to see if the number is even
    if number % 2 == 0:
        # Print half the number and on the same line
        print(number // 2, end=' ')
        # Returns half the number
        return number // 2
    # Check to see if the number is not even
    elif number % 2 == 1:
        Calculate the new number
        result = 3 * number + 1
        print(result, end=' ')
        #returns the result
        return result

# Performs while loop until 'iser_input' becomes 1
while user_input != 1:
    # Passes 'user_input' to collatz() function until it arrives at '1'
    user_input = collatz(user_input)
