from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        unmatched_temps = [] # [temp, original_idx]

        for i, t in enumerate(temperatures):
            while unmatched_temps and unmatched_temps[-1][0] < t:
                temp, idx = unmatched_temps.pop()
                result[idx] = i - idx

            unmatched_temps.append([t, i])

        return result