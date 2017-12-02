# def capitalize_words(string):
#     print string.title()
# print capitalize_words("this is a sentence")
# This is the fastest method in python

# Write a method that takes in a string of lowercase letters and
# spaces, producing a new string that capitalizes the first letter of
# each word.



def capitalize_words(string):
    split_words = string.split(" ")
    index = 0
    while index < len(split_words):
        a_word = split_words[index]
        first_letter = a_word[0].upper() # new var partially because strings are immutable in python,
# this requires that one create a new string w/ each iteration and stores the references to a new string
        split_words[index] = first_letter + a_word[1:]
        index += 1
    return " ".join(split_words)
print capitalize_words("this is a sentence")
