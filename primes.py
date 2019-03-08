user_input = int(input("Please enter a positive integer: "))

if user_input > 1:
    for n in range(2, user_input):
        if (user_input % n) == 0:
            print("That is not a prime number")
            break
    else:
        # loop fell through without finding a factor
            print("That is a prime number")

else: 
    print("That is not a prime number")