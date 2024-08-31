class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Empty dictionary used to store each interger(as a key) in the nums list and how many times it appears(as a value) 
        major = {}

        # Loop through each integer 'x' in the list 'nums'.
        for x in nums:
            # Check if the integer 'x' is already in the dictionary 'major'.
            if x in major: 
                # If 'x' is already a key in the dictionary, increment its count by 1.
                major[x] += 1
            else: 
                # If 'x' is not already a key in the dictionary, add it with a count of 1.
                major[x] = 1
        
        # Find the key (integer) in the dictionary 'major' that has the maximum value (the highest count). 
        max_element = max(major, key=lambda x: major[x])

        # Return the integer that has the highest count
        return max_element
