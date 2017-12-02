# Write a method that takes a string and returns the number of vowels
# in the string. You may assume that all the letters are lower cased.
# You can treat "y" as a consonant.
#

def count_vowels(string):
    string_list = list(string)
    print (string_list)
    vowels = ["a", "e", "i", "o", "u"]
    index1 = 0
    count =0
    while index1 < len(string_list):

        for i in vowels:

            if i == string_list[index1]:
                count +=1
        index1 +=1
    return count
print (count_vowels ('abcd'))
print (count_vowels('color'))
print (count_vowels('colour'))
print (count_vowels('cecilia'))
