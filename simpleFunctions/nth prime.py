# Write a method that returns the `n`th prime number. Recall that only
# numbers greater than 1 can be prime.
#
# Difficulty: medium.

def is_prime(number):
    if number < 1: #smaller than 1 can't be prime
        return False
    index = 2 #no need to handle ops on 2 because prime and % will be zero
    while index < number: #this while loops finds what can't be prime
        if number % index ==0: #if divisible then no prime
            return False
        index +=1 #step through dividers but they can't be larger than the number
    return True
print is_prime(2)
print is_prime(3)
print is_prime(4)

def nth_prime(n):
    prime_num_count= 0 #ties to value passed in. goal of count to find possible nth prime
    instance_of_prime =2 # numbers greater than 1 can be prime. goal return prime numbers
    while True: # check if is_prime is true and passes any n value automatically
        if is_prime(instance_of_prime): # checks for primality
            prime_num_count +=1 #logic that steps through possible nth prime (n)
            if prime_num_count == n: #if not nth prime, instance_of_prime +=1 until reached
                return instance_of_prime
        instance_of_prime +=1

print nth_prime(1)
print nth_prime(2)
print nth_prime(4)
print nth_prime(5)
