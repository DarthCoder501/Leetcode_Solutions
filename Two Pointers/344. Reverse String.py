class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0 #initialize left pointer
        r = len(s) - 1 #initialize right pointer

        while l < r: 
            s[l], s[r] = s[r], s[l] #swap left pointer num with right pointer num 
            l += 1 #move up from the left
            r -= 1 #move down from the right 
