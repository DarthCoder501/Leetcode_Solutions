class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 # Creates left pointer 
        longest = 0 # Tracks length of longest substring
        sett = set() # Set to store characters 
        n = len(s) # Length of string 

        # Loops thorugh each char in s 
        for r in range(n):
            # While we have an invalid substring(repeating characters)
            while s[r] in sett: 
                sett.remove(s[l]) # Remove the char at s[l]
                l += 1 # Move onto the next char 
            
            w = (r-l) + 1 # Create our sliding window length 
            longest = max(longest,w) # Get the longest substring length so far 
            sett.add(s[r]) # Add the char s[r] 

        return longest # Return the longest substring length found 
