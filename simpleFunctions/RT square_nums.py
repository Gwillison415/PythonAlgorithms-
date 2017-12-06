# square_nums
# Write a method square_nums that takes a number max and returns the
# number of perfect squares less than max. Do not use Math.sqrt(x) or x ** 0.5;
# we don't want you to calculate square roots for this problem.
# You will, however, want to find squares (x * x is fine).

def square_nums(num):
 i = 1
 while True:
     result = i*i
     if result >= num:
         return i - 1
     i += 1

print (square_nums(5))
print (square_nums(10))
print (square_nums (25))
