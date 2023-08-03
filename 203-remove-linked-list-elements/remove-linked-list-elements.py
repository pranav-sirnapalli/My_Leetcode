# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        orig = ListNode(-1, next=head)
        prev = orig
        pres = head

        while(pres != None):
            nxt = pres.next
            if(pres.val == val):
                prev.next = nxt
            else:
                prev = pres
            pres = nxt
        return orig.next