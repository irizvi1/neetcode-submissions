# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #compare each node and add the smaller one, then check the node after the one u added to the one that was larger and add smaller
    
        dummynode = ListNode(0)
        curr = dummynode
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr.next = list1
                
                list1 = list1.next
            else:
                curr.next = list2
              
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 if list1 is not None else list2
        
        return dummynode.next



