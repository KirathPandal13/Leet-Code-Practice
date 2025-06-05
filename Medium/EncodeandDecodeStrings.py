"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = "" # Encode result as an empty string
        for s in strs: # Iterate through each string in the list
            res += str(len(s)) + "#" + s # Add the length of the string, a special character '#', and the string itself
        return res # Return the encoded string

    def decode(self, s: str) -> List[str]:
        res = [] # Store the final list of decoded strings
        i = 0 # Initialize a pointer to track the current position in the encoded string

        while i < len(s): # Iterate through until the entire string is processed
            j = i # # Find the position of the separator '#' starting from i
            while s[j] != "#":
                j += 1 # Moves the pointer j forward until it finds the # character in the encoded string s.
            length = int(s[i:j]) # Convert the length to an integer
            res.append(s[j + 1 : j + 1 + length]) # Extract the string of 'length' characters that starts right after the '#'
            i = j + 1 + length # Move i to the beginning of the next encoded string
        return res # Return the decoded strings