# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [4, 3, 2, 4, 1, 2, 3]
print(singleNumber(nums))