# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr: ListNode
        fast_ptr: ListNode

        slow_ptr = fast_ptr = head

        while fast_ptr and fast_ptr.next != None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
            fast_ptr = fast_ptr.next
        
        return slow_ptr
            