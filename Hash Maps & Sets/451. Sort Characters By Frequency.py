class Solution:
    def frequencySort(self, s: str) -> str:
        d = {} # Creates a dictionary to store the frequency of characters
        res = '' # Empty string to hold new string 

        # Counts the frequency of the characters 
        for x in s:
            if x in d: 
                d[x] += 1 
            else: 
                d[x] = 1 

        # Sorts the frequency of the characters in ascending order 
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        # Loops through the dictionary and adds the characters in the new string 
        for key, values in sorted_d.items(): 
            res += key * values

        return res 
