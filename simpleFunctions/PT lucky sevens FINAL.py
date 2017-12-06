def lucky_sevens(numbers):
    num_idx = 0
    while num_idx < len(numbers)-2:
        if numbers[num_idx] + numbers[num_idx +1] + numbers[num_idx +2] ==7:
            return True
        else:
            num_idx +=1
    return False

print lucky_sevens([2,1,5,1,0])
print lucky_sevens([0,-2,1,8])
print lucky_sevens([7,7,7,7])
print lucky_sevens([3,4,3,4])
