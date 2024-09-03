class Solution:
    # Define a method that finds the longest common prefix among a list of strings
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize an empty list to store the common prefix characters
        prefix = []
        
        # Sort the list of strings to get the lexicographically smallest and largest strings
        sorted_list = sorted(strs)
        
        # The first string in the sorted list (smallest)
        firststring = sorted_list[0]
        
        # The last string in the sorted list (largest)
        laststring = sorted_list[-1]

        # Loop through each character in the first string
        for i in range(len(firststring)):
            # Check if the corresponding character in the last string matches
            if len(laststring) > i and firststring[i] == laststring[i]:
                # If they match, add the character to the prefix list
                prefix.append(laststring[i])
            else:
                # If they don't match, return the common prefix found so far
                return ''.join(prefix)
        
        # If the loop completes, return the entire prefix found
        return ''.join(prefix)
