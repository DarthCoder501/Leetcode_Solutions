class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s) # Convert the string into a list of characters
        vowels = "aeiouAEIOU" # possible vowels in lower & upper case form
        l, r = 0, len(s) - 1 # initalizes pointers

        while l < r: 
            while l < r and s[l] not in vowels: # moves left pointer until it finds vowel
                l+= 1
            while l < r and s[r] not in vowels: # moves right pointer until it finds vowel
                r -= 1  
            s[l], s[r] = s[r], s[l] # swap the vowels that were found 
            l += 1 # move to next letter 
            r -= 1 # move to next letter 

        s = ''.join(s) # turns list back into string with reversed vowels 
        return s # returns the new string 
