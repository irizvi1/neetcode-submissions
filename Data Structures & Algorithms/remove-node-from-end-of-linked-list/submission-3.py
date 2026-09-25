# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #make dummy node (0, head), set l to it and r to head
        #loop while n > 0, moving r to the right nad decrementing n each time
        #antoher while loop moveing l and r to the right until r reaches te end
        #l will be one behinf the node to be remove

        dummy = ListNode(0, head)
        l = dummy
        r = head

        while n > 0:
            r = r.next
            n-=1
        while r != None:
            r = r.next
            l = l.next
        l.next = l.next.next

        return dummy.next



        