# Write a method that takes an array of numbers in. Your method should
# return the third greatest number in the array. You may assume that
# the array has at least three numbers in it.

def third_greatest(nums):
    index1 =0 #defines an index to search numbers from
    while len(nums) > 0:
        new_list = sorted(nums)
        return new_list[-3::len(nums)]
print third_greatest([5, 3, 7, 4, 8])
