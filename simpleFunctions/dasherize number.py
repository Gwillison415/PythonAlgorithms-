# Write a method that takes in a number and returns a string, placing
# a single dash before and after each odd digit. There is one
# exception: don't start or end the string with a dash.
#
# You may wish to use the `%` modulo operation; you can see if a number
# is even if it has zero remainder when divided by two.
#

def dasherize_number(num):
    num_string = str(num)
    result = '' #empty string to concatenate each part to
    index = 0 # loop index
    while len(num_string) > index:
        digit = int(num_string[index]) #print on (203) returns 2
        if index > 0: # meets exception not to start string with dash
            previous_digit = int(num_string[index-1]) #returns first digit in following model
            if previous_digit %2 == 1 or digit %2 == 1: #checks first and next for odd and adds "-"
                result += "-" #concatenate when or condition met
        result += num_string[index] #concatenate to result BY string index value
        index +=1 #index loop value to check to see if logic + ops are correct
    return result #return only when all indices have been run
print dasherize_number(203)
print dasherize_number(303)
print dasherize_number(333)
print dasherize_number(3223)
