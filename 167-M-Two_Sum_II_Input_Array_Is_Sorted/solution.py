from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            ij = numbers[i] + numbers[j]
            if ij == target:
                break
            elif ij > target:
                j -= 1
            else:
                i += 1

        return [i+1, j+1]