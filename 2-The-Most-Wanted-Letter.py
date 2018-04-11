# You are given a text, which contains different english letters
# and punctuation symbols.
# You should find the most frequent letter in the text.
# The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter,
# so for the purpose of your search, "A" == "a".
# Make sure you do not count punctuation symbols,
# digits and whitespaces, only letters.

# If you have two or more letters with the same frequency,
# then return the letter which comes first in the latin alphabet.
# For example -- "one" contains "o", "n", "e"
# only once for each, thus we choose "e".

# Input: A text for analysis as a string.

# Output: The most frequent letter in lower case as a string.
import string


import string
def checkio(text):
    text = list(text)
    for letter in text:
        if letter.lower() not in string.ascii_lowercase:
            text.remove(letter)
            
    print(text)
            

checkio('dskpokpoo899jij  ioni iojio pooo123d')