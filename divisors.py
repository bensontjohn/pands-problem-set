for num in range(1000, 10000):
    if num == 1000 or num % 12 == 0:
        continue
    elif num % 6 == 0:
        print(num)