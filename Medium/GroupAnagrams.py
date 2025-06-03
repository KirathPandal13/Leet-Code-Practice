"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs: #Iterate through each string in the input list
            count = [0] * 26 # create a list with 26 zeros to count each letter from 'a' to 'z'
            for c in s: #Iterate through each character in the string
                count[ord(c) - ord("a")] += 1 #Increment the count for that character
            
            res[tuple(count)].append(s) # Comvert the count list to a tuple so it may be used as a dictionary key
                                        # Append the current string to the list of anagrams that share the same key.
        return res.values() # Return the values of the dictionary.

#ord() is a built-in function that returns the ASCII value of a character.