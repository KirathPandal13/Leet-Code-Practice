"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4

Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # Convert the list to a set for faster lookup time O(1)
        longest = 0 # Variable set to track the longest sequence length

        for num in numSet: # Iterate through each number in the set
            if (num - 1) not in numSet: # Check if its the start of the sequence
                length = 0 # Count the sequence length from 0
                while (num + length) in numSet: # Continue checking the next number in the sequence
                    length += 1 # Increment the sequence length by 1
                longest = max(length, longest) # Update the longest sequence if this one is longer
        
        return longest # Return the length of the longest consecutive sequence