
def fizzbuzz(num):
    for i in num:
        if i % 3 == 0 and i %5 ==0:
            print "fizzbuzz"
        elif i %3 ==0:
            print "Fizz"
        elif i % 5 == 0:
            print "buzz"
        else:
            print i
print fizzbuzz(range(1, 101))
