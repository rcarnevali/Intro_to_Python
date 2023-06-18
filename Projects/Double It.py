"""
Program: Double It
--------------------
Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.
"""

def main():
    curr_value = int(input("Enter a number: "))
    
    first_value = curr_value + curr_value
    
    while first_value <= 200:
        print (first_value)
        first_value = first_value + first_value

if __name__ == '__main__':
    main()
