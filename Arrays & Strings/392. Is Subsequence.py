class Solution:
    # Define a method that checks if string 's' is a subsequence of string 't'
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize two pointers, l for 's' and r for 't', both set to 0
        l, r = 0, 0 

        # Loop through both strings as long as there are characters left in 's' and 't'
        while l < len(s) and r < len(t):
            # If the current character in 's' matches the current character in 't'
            if s[l] == t[r]: 
                # Move to the next character in both 's' and 't'
                l += 1 
                r += 1 
            else:
                # If the characters don't match, only move to the next character in 't'
                r += 1

        # After the loop, check if all characters in 's' were matched
        if l == len(s):
            # If all characters in 's' were found in 't' in order, return True
            return True
