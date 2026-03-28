from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            # reverse pointer
            curr.next = prev

            # move forward
            prev = curr
            curr = temp

        return prev

        # None(prev) -> 1(curr) -(head.next)> 2
        # None <(head.next)- 1(prev) <- 2(curr) 

