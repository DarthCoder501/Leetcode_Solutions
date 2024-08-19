class Solution:
    # Define a method that takes in two strings: word1 and word2
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize two pointers (l for word1 and r for word2) both set to 0
        l = r = 0
        # Create an empty list to store the merged characters
        merge = []

        # Loop through both strings as long as there are characters left in both
        while l < len(word1) and r < len(word2):
            # Append the current character from word1 to the merge list
            merge.append(word1[l])
            # Append the current character from word2 to the merge list
            merge.append(word2[r])
            # Move to the next character in both word1 and word2
            l += 1
            r += 1

        # If there are leftover characters in word1, add them to the merge list
        while l < len(word1):
            merge.append(word1[l])
            l += 1

        # If there are leftover characters in word2, add them to the merge list
        while r < len(word2):
            merge.append(word2[r])
            r += 1

        # Convert the list of characters into a single string and return it
        return "".join(merge)
