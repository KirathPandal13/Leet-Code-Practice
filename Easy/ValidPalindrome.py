"""
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # Initialize two pointers. (l) starts at the left of the string and (r) starts at the right of it

        while l < r: # Continue iterating through if the pointers have not yet crossed.
            while l < r and not self.alphaNum(s[l]): # Skip all non-alphanumeric characters from the left side.
                l += 1 # Iterate (l) to the right
            while r > l and not self.alphaNum(s[r]): # Skip all non-alphanumeric characters from the right side.
                r -= 1 # Iterate (r) to the left
            if s[l].lower() != s[r].lower(): # Set (r) and (l) to lower case and if they dont match return false
                return False # Return False if not a palindrome
            l, r = l + 1, r - 1 # Move both pointers inward to check the next pair of characters.
        return True # Return True if the loop finishes
    
    def alphaNum(self, c): # Function to help return true if the character is non-alphanumeric using ASCII values.
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))