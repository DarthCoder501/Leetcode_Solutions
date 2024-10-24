class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Initalize two dictionaries to store character frequency count 
        d1 = {} 
        d2 = {}
        # Count the frequency of characters in the first string
        for x in word1: 
            if x in d1: 
                d1[x] += 1
            else: 
                d1[x] = 1

        # Count the frequency of characters in the second string 
        for x in word2: 
            if x in d2: 
                d2[x] += 1
            else: 
                d2[x] = 1
            
        # Compare the length of the strings
        if len(word1) != len(word2): 
            return False

        # Check if both strings have the same set of unique characters 
        if set(word1) != set(word2):
            return False

        # Check if both strings have the same frequency of characters 
        if sorted(d1.values()) != sorted(d2.values()):
            return False

        return True 
