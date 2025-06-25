"""
You are given an integer array heights where heights[i] represents the height of the i^th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4

Constraints:
2 <= height.length <= 1000
0 <= height[i] <= 1000

"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 # Create two pointers 
        res = 0 # Will store the maximum value found

        while l < r: # Loop while the left pointer is to the left of the right pointer
            area = min(heights[l], heights[r]) * (r - l) # Calculate the area formed between the two lines
            res = max(res, area) # Update the result if this area is larger than previous max

            if heights[l] < heights[r]:  # Move the pointer pointing to the shorter line
                l += 1 # Iterate to the right
            else:
                r -= 1 # Iterate to the left
    
        return res # return the largest area found