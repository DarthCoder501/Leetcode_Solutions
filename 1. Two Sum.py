class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty dictionary to store the numbers and their corresponding indices
        d = {}
        # Get the length of the input list 'nums'
        n = len(nums)

        # First loop: Populate the dictionary with each number as the key and its index as the value
        for i in range(n): 
            d[nums[i]] = i
        
        # Second loop: Iterate over the list again to find two numbers that add up to the target
        for i in range(n):
            # Calculate the number needed to reach the target sum by subtracting the current number
            y = target - nums[i]
            # Check if this needed number exists in the dictionary and is not the same as the current index
            if y in d and d[y] != i:
                # If found, return the indices of the two numbers
                return [i, d[y]]
