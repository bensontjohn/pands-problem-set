# Benson Thomas John, 2019
# Program to ask the user to input any positive integer and outputs the sum of all numbers between one and that number. 


# Prompt user input and convert the user_num to integer
user_num = int(input("Please enter a positive integer: "))

# Initialize loop variable to 1
i=1

# Referenced: https://docs.python.org/3/tutorial/controlflow.html

# Checking whether user_num is a positive integer
if(user_num > 0):

    # Initialize count variable
    count = 0
    
    # Loop i values and condition
    while(i <= user_num):

        # Adding value of i to the count variable for new count
        count = count + i 

        # Incrementing the value of i by 1
        i = i + 1

    # Print the total count
    print(count)

else:
    print("The number entered is not a positive integer.")
