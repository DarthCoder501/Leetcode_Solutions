class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0 
        for i in range(len(stones)):
            if stones[i] in s: 
                count += 1
        return count
