# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next
        prev = None
        temp = None
        start = None

        while f != None and f.next != None:
            s = s.next
            f= f.next.next
        start = s
        s= s.next
        
        prev = None

        while s != None:
            temp = s
            s = s.next
            temp.next = prev
            prev = temp
        start.next= None

        s = head
        temp2 = None
        while prev != None:
            temp = s.next
            
            temp2 = prev.next
            s.next = prev
            prev.next = temp
            s = temp
            prev = temp2
       
        

            
            
            
            

        
        
        