class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        longest_streak = 0

        for num in nums:
            if num == 1:
                count += 1
                longest_streak = max(count, longest_streak)
            else:
                count = 0

        return longest_streak