contents = open("File.txt", "r")
count = 0
for line in contents:
    count = count + 1
    if count % 2 == 0:
        print(line)

contents.close()