# Benson Thomas John, 2019
# Program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.  

# loop through the numbers from 1000 to NOT including 10000
for num in range(1000, 10000):
    
    # Check whether the number is 1000 as program prints numbers BETWEEN 1000 and 10000 AND not divisble by 12 and skip the number
    if num == 1000 or num % 12 == 0:
        continue
        
    # Check whether the number is divisible by 6
    elif num % 6 == 0:
        print(num)
