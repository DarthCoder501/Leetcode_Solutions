class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {} # Initalize dict to store frequency count 
        sett = set() # Inialize a set to store unique frequencies 
        
        # Counts the frequency of each number 
        for x in arr: 
            if x in d: 
                d[x] += 1
            else: 
                d[x] = 1 
        # Iterates through the key, values in dict 
        for key, value in d.items():
            if value in sett: # Checks if number is already in the set
                return False 
            else: 
                sett.add(value) # Adds value to set if not already in set 
         
        return True 
        
