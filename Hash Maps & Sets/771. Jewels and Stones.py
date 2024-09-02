class Solution:
    # Define a method that counts how many of the stones are jewels
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Convert the string of jewels into a set for quick lookup
        s = set(jewels)
        
        # Initialize a counter to keep track of the number of jewels found in stones
        count = 0
        
        # Iterate through each stone in the stones string
        for i in range(len(stones)):
            # Check if the current stone is in the set of jewels
            if stones[i] in s:
                # If it is, increment the counter
                count += 1
        
        # Return the total count of jewels found in the stones string
        return count
