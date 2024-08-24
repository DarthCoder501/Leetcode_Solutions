class Solution:
    # Define a method that merges overlapping intervals in a list
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the list of intervals based on the start time of each interval
        intervals.sort(key=lambda interval: interval[0])
        
        # Initialize the merged list with the first interval
        merged = [intervals[0]]

        # Get the length of the intervals list
        n = len(intervals)

        # Loop through the intervals starting from the second one
        for i in range(1, n):
            # Check if the current interval overlaps with the last interval in the merged list
            if merged[-1][1] >= intervals[i][0]:
                # If they overlap, merge them by updating the end time of the last interval
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                # If they don't overlap, add the current interval to the merged list
                merged.append(intervals[i])
        
        # Return the merged list of intervals
        return merged
