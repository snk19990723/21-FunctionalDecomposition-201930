"""
Hangman.

Authors: Deng Zou and Haozhe Wu.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.
import random
####### Do NOT attempt this assignment before class! #######
def word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        print(string)

    words=string.split()
    print(words)
    r=random.randrange(0,len(words))
    item=words[r]
    print(item)

def get_guess(x):
    string= input(prompt=x)
    return string


