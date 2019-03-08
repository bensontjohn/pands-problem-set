user_input = input("Please enter a sentence: ")

arr_input = user_input.split(' ')

# obj[start:stop:step] - using indexing syntax
odd_list = arr_input[0::2]

output_string = " ".join(odd_list)
print(output_string)

# https://stackoverflow.com/a/47085688

# https://www.programiz.com/python-programming/methods/built-in/slice