from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            idx = (left + right) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                right = idx
            else:
                left = idx + 1

        return -1