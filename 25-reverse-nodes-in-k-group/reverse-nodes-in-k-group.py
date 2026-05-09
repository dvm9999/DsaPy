# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        res= last = ListNode(-1)
        while head:
            khead = head            
            rkhead = None
            i = 0
            while head and i < k:
                curr = head 
                head = head.next               
                curr.next = rkhead
                rkhead = curr               
                i += 1
            if i < k:
                while rkhead:
                    curr = rkhead
                    rkhead = rkhead.next
                    curr.next = last.next
                    last.next = curr                                       
                return res.next
            last.next = rkhead
            last = khead
            last.next  = None
        return res.next
        
            
