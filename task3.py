#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

""" 
import os
import time
n = float(input("Enter a number: "))
while n%2 != 0 or n != int(n):
    print("That is not an even integer.")
    time.sleep(1)
    os.system('cls')
    n = float(input("Enter a number: "))
else:
    print("That is an even integer!")
