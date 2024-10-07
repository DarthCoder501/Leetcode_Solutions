class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If str1 less than str2 swap them 
        if(len(str1) < len(str2)):
            return self.gcdOfStrings(str2, str1)
     
        # If str1 does not start with str2, no common discover return empty string
        elif not str1.startswith(str2):
            return "" 
        elif(len(str2) == 0): # Check if str2 is empty
            return str1 # When the length str2 = 0 str1 is the common divisor
        else:
            # Recursively cut off the common prefix and repeat the process
            return self.gcdOfStrings(str1[len(str2):], str2)
