class Solution:
    # Define a method that returns an array where each element is the product of all elements except itself
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        n = len(nums)
        
        # Initialize three lists to store intermediate and final results, all starting with 1s of length n
        left_products = [1] * n  # To store products of elements to the left of each index
        right_products = [1] * n  # To store products of elements to the right of each index
        final_results = [1] * n  # To store the final results

        # Calculate left_products: the product of all elements to the left of each index
        for i in range(1, n):
            left_products[i] = nums[i - 1] * left_products[i - 1]

        # Calculate right_products: the product of all elements to the right of each index
        for i in range(n - 2, -1, -1):
            right_products[i] = nums[i + 1] * right_products[i + 1]

        # Calculate the final results by multiplying left_products and right_products for each index
        for i in range(n):
            final_results[i] = left_products[i] * right_products[i]

        # Return the final array where each element is the product of all elements except itself
        return final_results
