# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return 
        

        kthB = head
        times = k - 1
        while times:
            kthB = kthB.next
            times -= 1
            
        kthE = head
        last = kthB.next
        
        while last:
            last = last.next
            kthE = kthE.next
        
        kthE.val, kthB.val = kthB.val, kthE.val
        
        return head