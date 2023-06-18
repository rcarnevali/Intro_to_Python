# This is a translating game. 
# You get points by correctly translating the english into portuguese

"""
File: Final_Project.py
-------------------
Fill in this comment.
"""

import random
import time

def main():
    word_pairs = read_word_pairs('pairs.txt')
    english_words = read_english_words('words.txt')
    SCORE = 0

    print("Did you know in Brazil we speak Portuguese? \nHere is a chance to learn a little portuguese! \nSelect the correct option to get points. \nIf you select the wrong option it is game over.")
    time.sleep(5)
    
    print("Are you ready to play?")
    time.sleep(3)  # Delay for 3 seconds

    while True:
        random_pair = random.choice(word_pairs)
        brazil_word = random_pair[0]
        options = generate_options(word_pairs, english_words, brazil_word)
        display_options(brazil_word, options)

        user_choice = get_user_choice()
        if user_choice is None or user_choice < 1 or user_choice > 4:
            print("That is an invalid choice. Please enter a number between 1 and 4.")
            continue

        user_translation = options[user_choice - 1]
        if user_translation == find_translation_pair(brazil_word, word_pairs):
            SCORE += 1
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"The correct answer was: {find_translation_pair(brazil_word, word_pairs)}") # print the correct answer
            break

    print(f"Game Over! Better Luck next time. Your final score was: {SCORE}")

# Get the word pairs from the dictionary file
def read_word_pairs(filename):
    with open(filename, 'r') as file:
        line = file.read().strip() # works with the single line of pairs where a single space separates each pairs
        word_pairs = [pair.split(',') for pair in line.split()] # separate each word within the pair by the comma
        return word_pairs

# Get all possible english words form the data well
def read_english_words(filename):
    with open(filename, 'r') as file:
        line = file.read().strip() # works with the single line of words
        english_words = line.split(',') # each word in the data well is separated by a comma
        return english_words

# Find the equivalent english pair to be displayed as an option
def find_translation_pair(brazil_word, word_pairs):
    for pair in word_pairs:
        if pair[0] == brazil_word: # the first word of the pair is the portuguese word
            return pair[1] # the second is the equivalent english translation
    return None

# Generate possible options along with the correct one
def generate_options(word_pairs, english_words, brazil_word):
    correct_translation = find_translation_pair(brazil_word, word_pairs)
    options = random.sample(english_words, k = 3) # get 3 random words from the data well
    options.append(correct_translation) # append them with the correct answer
    random.shuffle(options) # shuffle the four options
    return options

# To display the options in the console
def display_options(brazil_word, options):
    print(f"Translate the word '{brazil_word}' to English:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

# Function to get the users input number 
def get_user_choice():
    choice = input("Enter the number of what you think is the correct answer: ")
    if choice.isdigit():
        return int(choice)
    return None

if __name__ == '__main__':
    main()
