"""
Program: Mars Weight
--------------------
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

# Earth to mars weight ratio
MARS_RATIO = 0.378

def main():
    weight = float(input("Enter a weight on Earth: "))
    mars = weight * MARS_RATIO # Calculate the mars weight
    mars_rounded = round(mars,2) #round the mars weight to two deimals
    print("The equivalent weight on Mars: " + str(mars_rounded))

if __name__ == "__main__":
    main()
