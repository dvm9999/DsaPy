# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        last = dummy = ListNode(-1)     
        heapify(heap)
        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i))
        while heap:
            val, idx = heappop(heap)
            last.next = lists[idx]
            last = last.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(heap, (lists[idx].val, idx))
        return dummy.next
        