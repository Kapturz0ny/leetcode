from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_validator = set()
        col_validators = [set() for _ in range(9)]
        box_validators = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == ".":
                    continue

                # check row validator
                if item in row_validator:
                    return False
                row_validator.add(item)
            
                # check col validator
                if item in col_validators[j]:
                    return False
                col_validators[j].add(item)

                # check box validator
                if item in box_validators[i // 3][j // 3]:
                    return False
                box_validators[i // 3][j // 3].add(item)
            
            row_validator.clear()
        
        return True



