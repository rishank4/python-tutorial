import string

#Function to check if a string os a pangram
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)  #Set of all lowercase letter
    return set(s.lower()) >= alphabet #Check if input contains all letter

#Example usage
sentence="Pack my box with five dozen liquor jugs"
if is_pangram(sentence):
    print("The given string is a pangram.")
else:
    print("The given string is not a pangram")