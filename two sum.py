#The Two Sum problem asks us to find two numbers in an array that sum up to a given target value. We need to return the indices of these two numbers.

# Using hash table
class Solution:
    def twoSum(self, nums:[1,2,3,4,5,6], target:5):
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []
