"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Create empty dictionary to count the occurence of each value
        freq = [[] for i in range(len(nums) + 1)] # Create a list of empty lists, one for each possible frequency (0 to len(nums))

        for n in nums: # Count the freq of each # in nums
            count[n] = 1 + count.get(n, 0) # Get the current count (default 0), then iterate 1
        for n, c in count.items(): # Group the numbers by their freq
            freq[c].append(n) # add 'n' to list at index 'c' in freq
        
        res = [] # Store the top k frequent elements
        for i in range(len(freq) - 1, 0, -1): # Go from highest frequency to lowest so the commont number is found first
            for n in freq[i]: # Every number that appears 'i' times
                res.append(n) # Add it to the res list
                if len(res) == k: # Stop once k elements have been found
                    return res
