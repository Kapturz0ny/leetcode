from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)-1):
            prefix *= nums[i]
            answer[i+1] = prefix

        suffix = 1
        for i in range(len(nums)-1, 0, -1):
            suffix *= nums[i]
            answer[i-1] *= suffix

        return answer