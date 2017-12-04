def is_power_of_two(num):
    if num <1:
        return False
    while True:
        if num == 1:
            return True
        elif num % 2 ==0:
            num = num /2
        else:
            return False

print is_power_of_two(1)
print is_power_of_two(6)
print is_power_of_two(64)
print is_power_of_two(78)
