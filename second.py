# Benson Thomas John, 2019
# Program that reads in a textﬁle and outputs every second line. The program should take the ﬁlename from an argument on the command line. 

# import sys module
import sys

# References: https://www.pythonforbeginners.com/system/python-sys-argv
#           : https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

# Open the file in readmode and store the value at the first index to contents.
contents = open(sys.argv[1], "r")

#Initialize the count variable to zero
count = 0

# loop through each line in the file object contents
for line in contents:
    count = count + 1
    # For every second line, print the line
    if count % 2 == 0:
        print(line, end='')
        
# close the file
contents.close()
