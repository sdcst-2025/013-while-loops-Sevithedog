#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
You may need to use the:
print( variable , end='') option to print on one line
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""
n = float(input("Enter a number: "))
np = n 
count = 1
while not np == n*12:
    print(f"{int(np)},", end="")
    count = count + 1
    np = (n*count)
else:
    print(f"{int(np)}", end="")
    exit()
