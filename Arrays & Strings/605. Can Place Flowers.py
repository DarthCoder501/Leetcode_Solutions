class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0 # Counts the number of flowers that can be planted
        length = len(flowerbed) # Gets length of the flowerbed

        for i in range(length):
            # Checks to see if current and adjacent positions are empty 
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length - 1 or flowerbed[i+1] == 0): 
                flowerbed[i] = 1 # Places a flower 
                count += 1 # Increments the count 

        # Returns if n flowers can be planted w/o breaking the rules 
        return count >= n   
