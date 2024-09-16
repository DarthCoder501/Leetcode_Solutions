class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create a list with 0s to hold the answer for each day
        res = [0] * len(temperatures)

        # Initialize an empty stack to store tuples of (temperature, index)
        stk = []

        # Iterate over each temperature along with its index in the list
        for i, temp in enumerate(temperatures):
            # While the stack is not empty AND the current temp is greater the previous day's temp
            while stk and temp > stk[-1][0]:
                # Pop the top element from the stack, which gives the temp and index of the last entry
                stkTemp, stkIndex = stk.pop()

                # Calculate how many days it took to find a warmer temperature (difference in indices)
                res[stkIndex] = i - stkIndex

            # Push the current day's temperature and index onto the stack
            stk.append((temp, i))

        # Return the result list, which contains the number of days to wait for a warmer temperature
        return res
