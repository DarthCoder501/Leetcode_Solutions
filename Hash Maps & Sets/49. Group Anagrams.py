from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create an empty defaultdict called 'ans'. The default value for each key will be an empty list.
        ans = defaultdict(list)
        
        # Loop over each string 's' in the list 'strs' to handle each word one by one.
        for s in strs: 
            count = [0] * 26  # List with 26 zeros to keep track of how many times each letter (a to z) appears in the string 's'.

            # Now, we'll loop over each character in the string 's'(in each word). 
            for char in s: 
                # ord(char) - ord('a') gives us the position of the letter in the alphabet & correct position in our 'count' list.
                count[ord(char) - ord('a')] += 1 # We increment the value at that position by 1 to we count how many times each letter appears.
              
            # After counting letters in 's' convert 'count' into a tuple to use as a key for 'ans' dict to group all strings w/ the same letter counts.
            ans[tuple(count)].append(s) # Append the original string 's' to the list corresponding to this key.

        #ans.values() gives us all the lists of grouped anagrams as a single list of lists.
        return list(ans.values())
