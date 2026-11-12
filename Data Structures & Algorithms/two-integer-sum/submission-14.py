class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = []
        for i, num in enumerate(nums):
            for j, numm in enumerate(nums):
                if i == j:
                    continue
                elif num + numm == target:
                    count.append(i)
                    count.append(j)
                    return count 