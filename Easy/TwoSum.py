"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,00

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Empty dictionary created to store number as key and dictionary as value.
        # val : index

        for i, n in enumerate(nums): # Loop through the list with both index (i) and number (n)
            diff = target - n # Calculate the diff to reach the target
            if diff in prevMap: # if the needed number (diff) was seen
                return[prevMap[diff], i] # return the previous number index and current one
            
            prevMap[n] = i # the current number will be stored in the dictionary
        # No return needed