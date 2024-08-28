class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Dictionary to represent the frequency of each character needed to form the word "balloon"
        balloon_dict = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        # Dictionary to store the frequency of characters in the input text
        text_dict = {}

        # Count the frequency of each letter in the input text
        for x in text:
            if x in text_dict:
                text_dict[x] += 1
            else:
                text_dict[x] = 1

        # Check if any required character for "balloon" is missing in the input text
        if any(x not in text_dict for x in balloon_dict):
            return 0  # If any character is missing, return 0 as "balloon" cannot be formed
        else:
            # Calculate the maximum number of times "balloon" can be formed by finding the limiting character
            return min(
                text_dict['b'],            # The count of 'b'
                text_dict['a'],            # The count of 'a'
                text_dict['l'] // 2,       # The count of 'l' divided by 2 (since "balloon" requires 2 'l's)
                text_dict['o'] // 2,       # The count of 'o' divided by 2 (since "balloon" requires 2 'o's)
                text_dict['n']             # The count of 'n'
            )
