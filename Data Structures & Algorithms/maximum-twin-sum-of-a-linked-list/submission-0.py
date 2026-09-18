# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        s, f = head, head
        
        while f and f.next:
            f = f.next.next
            temp = s.next
            s.next = prev
            prev = s
            s= temp
        res = 0
        while s:
            res = max(res, prev.val + s.val)
            prev = prev.next
            s = s.next
        return res