# Write a method that takes a string in and returns true if the letter
# "z" appears within three letters **after** an "a". You may assume
# that the string contains only lowercase letters.
#
# Difficulty: medium.

def nearby_az(string):
    index1= 0 #def variable for list element search index 2 must be withing range(3) of index1
#index1 is variable position of a from which to find z
    string_list = list(string) #def variable for list of the string ["a", "b", "c"]
    while index1 < len(string): #loop through string_list, loop ends at last letter in string
        if string_list[index1] != "a": #serach for "a" postion, advance range until a is found .. index+1
            index1 += 1 #range(3) begins with a
        else: #ONCE "a" is found, exit the loop and continue on
            break
# index2 is list position of"z" (within range(2) 0,1,2 of index1)
    index2 = index1 +1 #to find position it must be 1-3 after "a" hence +1
    #index2 must be smaller than total list len
    # AND (checks if both are true)
    #index2 must be within 3 positions of index 1
    while (index2 < len(string)) and (index2 <= index1 +3):
#condition list position within range?
            if string_list[index2] == "z":
                return True
            else: #if not next to "a" +1
                index2 += 1 #(index2 <= index1 +3) will handle thatf

    return False
print (nearby_az("dbdaz"))
print (nearby_az("abcz"))
print (nearby_az("abcdz"))
print (nearby_az("a"))
print (nearby_az("z"))

#list.index(x)
#Return the index in the list of the first item whose value is x.
