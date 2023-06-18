"""
Program: Khansole Academy
--------------------
Khansole Academy—a program that helps other people learn addition! Write a program that randomly generates a simple addition problem for the user, reads in the answer from the user, and then checks to see if they got it right or wrong.
"""

import random

def main():
    
    # Instructions
    print("Khansole Academy")
    rand_numb_1 = random.randint(1, 99)
    rand_numb_2 = random.randint(1, 99)
    print ("What is", rand_numb_1, "+", rand_numb_2, "?")
    
    # User input
    users = int(input("Your answer: "))
    
    # Calculation
    calculator = academy(rand_numb_1, rand_numb_2)
    count = 0
    
    # Output
    if users == calculator:
        print ("Correct!")
        count += 1
        if count > 1:
            print("You've gotten", count, "in a row.")
    else:
        print("Incorrect.")
        print("The expected answer is", calculator)

def academy (numb1, numb2):    
    result = numb1 + numb2
    return result
    
    
    
if __name__ == '__main__':
    main()
