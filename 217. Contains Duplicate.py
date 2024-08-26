class Solution:
    # Define a method that checks if there are any duplicate elements in the list
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty set to keep track of seen elements
        dupe = set()
        
        # Iterate through each element in the nums list
        for num in nums:
            # Check if the current element is already in the set
            if num in dupe:
                # If it is, return True immediately, as a duplicate is found
                return True
            
            # If the current element is not in the set, add it to the set
            dupe.add(num)
        
        # If no duplicates are found after checking all elements, return False
        return False
