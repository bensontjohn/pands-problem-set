# Benson Thomas John, 2019
# Program that displays a plot of the functions x, x^2 and 2^x in the range [0,4].

# Referenced: Matplotlib(https://matplotlib.org/users/pyplot_tutorial.html)

# import matplotlib
import matplotlib.pyplot as plt

# plot of the functions x, x^2 and 2^x in the range [0,4]
plt.plot([0, 1, 2, 3, 4])
plt.plot([0, 1, 4, 9, 16])
plt.plot([1, 2, 4, 8, 16])

# Label for Y and X axis
plt.ylabel('x, x^2 and 2^x ')
plt.xlabel('x')

# shows the plots
plt.show()