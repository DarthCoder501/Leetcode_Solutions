class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 #initialize left pointer
        n = len(height) #get length of height array 
        r = n - 1 #initialize right pointer
        max_area = 0 #initialize max area variable 

        while l < r: 
            for i in range(n): #loops thorugh height variable 
                width = r - l #sets width as differences in index
                length = min(height[l], height[r]) #sets length to smaller number
                area = width * length #gets area of the "container"
                max_area = max(max_area, area) # max area is an area already found or new area 

                if height[l] > height[r]: #move 'l' pointer to potentially higher num height[l]>height[r]
                    r -= 1
                else: #move 'r' pointer to potentially higher num height[l]>height[r]
                    l += 1 
                    
        return max_area
