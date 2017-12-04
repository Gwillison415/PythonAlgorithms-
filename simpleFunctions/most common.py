# Write a method that takes in a string. Your method should return the
# most common letter in the array, and a count of how many times it
# appears.
#
# Difficulty: medium.


# def most_common_letter(string):
#     list_of_letter = list(string)
#     while len(string) >0:
#         for i in list_of_letter:
#             I = list(i)
#             print I, + list_of_letter.count(i)
# #returns never ending list of ["c"] 1 and ["a"] 2
# print most_common_letter('abca')
# print most_common_letter('abbab')

#
#
def most_common_letter(string):
    list_of_letter = list(string)
    while len(list_of_letter) >0:
        for i in list_of_letter:
            I = list(i)
            print I, + list_of_letter.count(i)
            del list_of_letter[1:len(list_of_letter)]
print most_common_letter('abca')
print most_common_letter('abbab')
