# chaos.py
# This is a function to illustrate the behaviours of random numbers
# I am just adding this commit, and then push from my vscode terminal
def main():
    print("This is a program to illustrate the chaotic behaviour of numbers")
    x = eval(input("Enter a number from 0 to 1:"))
    n = eval(input("How many values do want me to print?:"))
    for i in range(n):
        x = 3.9 * x *(1 - x)
        print(x)
