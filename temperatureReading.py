# Assignment 6.1
# Eric Vargas
# Description: This program will allow the user to input a series of temperatures.  The program will then calculate the
# largest temp, smallest temp, and print the number of temps entered.

# create temperature list
temperatures = []

while True:
    # Ask user to input temperature
    userTemp = input('Enter a temperature (# to stop): ')
    # Input next temp from user or sentinel value
    if userTemp == '#':
        break
    else:
        # add temperatures to the list
        temperatures.append(int(userTemp))
# Largest temperature
print('Largest temperature in list:', max(temperatures))
# Smallest temperature
print('Smallest temperature in list:', min(temperatures))

# Print the number of temperatures in the list
print('There are total {} temperatures in the list'.format(len(temperatures)))
