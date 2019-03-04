user_input = int(input("Please enter a positive integer: "))
print(user_input, end =' ')

def collatz(number):
    if number % 2 == 0:
        print(number // 2, end=' ')
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result, end=' ')
        return result

while user_input != 1:
    user_input = collatz(user_input)