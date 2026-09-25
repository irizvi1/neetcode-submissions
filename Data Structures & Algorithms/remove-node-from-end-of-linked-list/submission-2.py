# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #s slow, f fast, s will be at index f//2
       
        
        l = head
        r = head
        temp = None
        length = 0
        count  = 0
        
        

        while r!= None:
            r = r.next
            length +=1
        need = length - (n )

        dummy = ListNode(0, head)
        l = dummy

        while count < need:
            
            l=l.next
            count+=1
        
        l.next = l.next.next
        return dummy.next




        