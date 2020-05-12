# Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
# and set all the other elements to be that value. Return the changed array.
# 
# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]


def max_end3(nums):
    max_num = max(nums[0], nums[2])

    nums[0] = max_num
    nums[1] = max_num
    nums[2] = max_num

    return nums
