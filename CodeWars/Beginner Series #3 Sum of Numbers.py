def get_sum(a,b):
    #need a, b, and sum all num between
    num_difference = abs(a - b) - 1

    if a ==b:
        return b
    elif (a <= 0 and b <= 0): #if subracting finds the dif
        new_sum = a + b
        while num_difference > 0:
            new_sum -= num_difference
            num_difference -= 1
        return (new_sum)
    elif (a >= 0 and b <= 0):
        new_sum = a + b
        b_sub = b
        a_add = a
        while b_sub < 0:
            new_sum -= b_sub + 1
            b_sub += 1
        while a_add > 0:
            new_sum += a_add - 1
            a_add -= 1
        return (new_sum)
    elif (a >= 0 and b>= 0): #if subracting finds the dif
        new_sum = a + b
        while num_difference > 0:
            new_sum += num_difference
            num_difference -= 1
        return (new_sum)
    else:
        new_sum = a + b
        b_sub = b
        a_add = a
        while b_sub > 0:
            new_sum += b_sub - 1
            b_sub -= 1
        while a_add < 0:
            new_sum -= a_add + 1
            a_add += 1
        return (new_sum)




print(get_sum(-1, -3))  # == -1 // -1 + 0 = -1
print(get_sum(4, 2)) # == 2  // -1 + 0 + 1 + 2 = 2
print (get_sum(0,1))  #,1

print (get_sum(0,-1))  #,-1
