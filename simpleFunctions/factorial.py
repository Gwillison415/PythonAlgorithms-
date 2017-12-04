def factorial_maker(x):
    if x == 0:
        return 1
    elif x==1:
        return 1

    else: x *= factorial_maker(x-1)
    return x

print (factorial_maker(2))
print (factorial_maker(5))
print (factorial_maker(10))
