class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in nums:
            if i==val:
                nums.remove(i)
                
        return len(nums)