"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # result will be stored in a list
        nums.sort() # Sort the number in order to make the searching method easier

        for i, a in enumerate(nums): # Iterate through the index and value
            if a > 0: # If the current value is greater zero then break because the sum can then not equal zero
                break

            if i > 0 and a == nums[i - 1]: # Skip the duplicate numbers
                continue

            l, r = i + 1, len(nums) - 1 # Using the 2 pointer method. The left index will start at index (i) and the righ pointer will start at the end
            while l < r: # Keep checking while both pointer do not cross
                threeSum = a + nums[l] + nums[r] # add the sum of the current trio of numbers
                if threeSum > 0:
                    r -= 1 # If the sum is too big, move r left to reduce the value.
                elif threeSum < 0:
                    l += 1 # If the sum is too small, move l right to increase the value.
                else:
                    res.append([a, nums[l], nums[r]]) # When a valid trio of numbers is found add it to the list
                    l += 1 # Move both to move and iterate through and find more combinations
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # Skip duplicate values on the left to avoid repeating the same trio of numbers.
                        l += 1
                        
        return res