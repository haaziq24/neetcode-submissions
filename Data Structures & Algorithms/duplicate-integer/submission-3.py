class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = {}
        for i, num in enumerate(nums):
            if num in track:
                return True 
            else:
                track[num] = i

        return False 
                

            