from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = None
        merged_head = None
        if list1 and list2:
            if list1.val < list2.val:
                merged_head = list1
                merged_list = list1
                list1 = list1.next
            else:
                merged_head = list2
                merged_list = list2
                list2 = list2.next
        elif list1:
            merged_head = list1
            merged_list = list1
            list1 = list1.next
        elif list2:
            merged_head = list2
            merged_list = list2
            list2 = list2.next

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    merged_list.next = list1
                    merged_list = merged_list.next
                    list1 = list1.next
                else:
                    merged_list.next = list2
                    merged_list = merged_list.next
                    list2 = list2.next
            elif list1:
                merged_list.next = list1
                merged_list = merged_list.next
                list1 = list1.next
            else:
                merged_list.next = list2
                merged_list = merged_list.next
                list2 = list2.next

        return merged_head