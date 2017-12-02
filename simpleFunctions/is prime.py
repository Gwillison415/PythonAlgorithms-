# Write a method that takes in an integer (greater than one) and
# returns true if it is prime; otherwise return false.
#
# You may want to use the `%` modulo operation. `5 % 2` returns the
# remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
# of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`.
# More generally, if `m` and `n` are integers, `m % n == 0` if and only
# if `n` divides `m` evenly.
#

def is_prime(number):
    if number < 1: #smaller than 1 can't be prime
        return False
    index = 2 #no need to handle ops on 2 because prime and % will be zero
    while index < number: #this while loops finds what can't be prime
        if number % index ==0: #if divisible then no prime
            return False
        index +=1 #step through dividers but they can't be larger than the number
    return True
print (is_prime(2))
print is_prime(3)
print is_prime(4)
print is_prime(17)
