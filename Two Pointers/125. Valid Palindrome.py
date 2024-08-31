class Solution:
  def isPalindrome(self, s: str) -> bool:
      
        #Empty string to store only the alphanumeric characters from the input string 's'.
        newStr = ''
        
        # Loop through each character in the string 's'.
        for char in s: 
            # Check if the current character 'char' is alphanumeric 
            if char.isalnum():
                # If the character is alphanumeric, we add it to 'newStr' so it only has the letters/numbers from OG string.
                newStr += char 

        # After processing the string, we set two pointers: i at start j at end 
        i, j = 0, len(newStr) - 1
        
        # Calculate the length of 'newStr' and store it in 'n'. 
        n = len(newStr)

        # If the length of 'newStr' is 1 or 0, it's either a single character or empty & considered a palindrome by definition, return True.
        if n == 1 or n == 0:
            return True

        # A loop where comparing characters at the start and end of 'newStr' until the pointers 'i' and 'j' meet in the middle.
        while i < j: 
            # Compare char at 'i' and 'j', convert them to lowercase to ensure charaters are case-insensitive ('A' = 'a')
            if newStr[i].lower() != newStr[j].lower():
                # If the characters at index 'i' and 'j' are different, the string is not a palindrome, return False.
                return False 
            else:
                # If the characters are the same, we move the pointers closer to the middle
                i += 1 
                j -= 1

        # If we complete the loop without finding any mismatched characters, the string is a palindrome, return True
        return True
