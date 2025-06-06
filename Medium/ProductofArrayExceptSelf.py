"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # Create a list filled with all 1s which will store the final answer

        prefix = 1 # Create a variable (prefix) equal to 1 to help keep track of the products of all element to left from the current index
        for i in range(len(nums)): # Iterate left to right in nums
            res[i] = prefix # Set to the current index value. res[i] holds all elements before the index i.
            prefix *= nums[i] # Update prefix by multiplying nums[i] for the next index
        
        postfix = 1 # Create a variable (prefix) equal to 1 to help keep track of the products of all element to right from the current index
        for i in range(len(nums) - 1, -1, -1): # Iterate through right to left in nums
            res[i] *= postfix # Multiply the current value (res[i]) by the postfix value
            postfix *= nums[i] # Update postfix by multiplying nums[i] for the next index to the left
        
        return res # Return the final result.