# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # iterate through the list
            if target - nums[i] in nums: # if the difference is in the list
                if nums.index(target - nums[i]) != i: # if is not the current number
                    return [i, nums.index(target - nums[i])] # return the solution