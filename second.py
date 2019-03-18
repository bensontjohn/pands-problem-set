import sys

contents = open(sys.argv[1], "r")
count = 0
for line in contents:
    count = count + 1
    if count % 2 == 0:
        print(line, end='')

contents.close()