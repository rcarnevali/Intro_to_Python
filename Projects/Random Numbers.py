"""
Program: Random Numbers
--------------------
The starter code for this program prints out a single random number in the range 1 to 100, inclusive.
"""

import random

def main():
    randomlist = []
    for i in range(0,10):
        value = random.randint(1, 100)
        randomlist.append(value)
    print(randomlist)

if __name__ == '__main__':
    main()
