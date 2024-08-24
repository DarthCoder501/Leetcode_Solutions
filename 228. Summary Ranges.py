class Solution:
    # Define a method that summarizes ranges of consecutive integers in a list
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Initialize an empty list to store the range summaries
        ranges = []
        # Initialize index i to iterate through the list
        i = 0 
        # Get the length of the nums list
        n = len(nums)
        
        # Loop through the list until the end
        while i < n:
            # Set the start of the range to the current number
            start = nums[i]
            
            # While the next number is consecutive to the current number, move to the next number
            while i < n - 1 and nums[i + 1] == nums[i] + 1:
                i += 1

            # If the start and end of the range are the same, add only the start number
            if start == nums[i]:
                ranges.append(str(start))
            # If the start and end of the range are different, add the range in the format "start->end"
            else:
                ranges.append(f"{start}->{nums[i]}")
            
            # Move to the next number
            i += 1

        # Return the list of ranges as strings
        return ranges
