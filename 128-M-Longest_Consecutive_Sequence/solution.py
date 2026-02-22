from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_ln = 0
        while len(set_nums) > 0:
            num = set_nums.pop()
            ln_counter = 1
            while len(set_nums) > 0:
                if num+1 in set_nums:
                    set_nums.remove(num+1)
                    ln_counter += 1
                    num += 1
                else:
                    break
            num -= (ln_counter-1)
            while len(set_nums) > 0:
                if num-1 in set_nums:
                    set_nums.remove(num-1)
                    ln_counter += 1
                    num -= 1
                else:
                    break
            max_ln = max(max_ln, ln_counter)

        return max_ln

