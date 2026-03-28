from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    @staticmethod
    def serialize_tree(r: TreeNode, curr_str: str = "") -> str:
        curr_str += f"#{r.val}"
        if r.left:
            curr_str = Solution.serialize_tree(r.left, curr_str)
        else:
            curr_str += "#n"
        
        if r.right:
            curr_str = Solution.serialize_tree(r.right, curr_str)
        else:
            curr_str += "#n"
        
        return curr_str


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        str_p, str_q = "", ""
        if p:
            str_p = Solution.serialize_tree(p)
        
        if q:
            str_q = Solution.serialize_tree(q)
        
        return str_p == str_q