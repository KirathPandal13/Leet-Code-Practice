"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true
Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Create empty hash set for faster run time when trying to find duplicate
        for num in nums: # Create for loop to check duplicate
            if num in seen: # If the number is seen 
                return True # return true if duplicate
            seen.add(num) # add other number and then reiterate back through the for loop
        return False