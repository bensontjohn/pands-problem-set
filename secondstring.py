# Benson Thomas John, 2019
# Program that takes a user input string and outputs every second word. 

# Prompt user to enter a sentence
user_input = input("Please enter a sentence: ")

# Referenced: # https://stackoverflow.com/a/47085688

# Convert the string to array using split method
arr_input = user_input.split(' ')

# Adapted: https://www.programiz.com/python-programming/methods/built-in/slice
# obj[start:stop:step] - using indexing syntax
odd_list = arr_input[0::2]

# Convert the array to string using join method
output_string = " ".join(odd_list)
# Print the string that returns every second word.
print(output_string)

