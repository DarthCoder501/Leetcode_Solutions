class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1) # Turns nums1 into a set 
        set2 = set(nums2) # Turns nums2 into a set 
        
        # Returns array of distinct intergers found in one array but not the other
        return [list((set1-set2)), list((set2-set1))] 
