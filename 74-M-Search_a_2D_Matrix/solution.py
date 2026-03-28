from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        left, right = 0, len(matrix)
        row = None
        while left < right:
            idx = (left + right) // 2
            if matrix[idx][0] <= target <= matrix[idx][-1]:
                row = idx
                break
            elif matrix[idx][0] < target:
                left = idx + 1
            else:
                right = idx
        
        if row is None:
            return False
    
        # find within row
        left, right = 0, len(matrix[row])
        while left < right:
            idx = (left + right) // 2
            if matrix[row][idx] == target:
                return True
            elif matrix[row][idx] < target:
                left = idx + 1
            else:
                right = idx
        
        return False