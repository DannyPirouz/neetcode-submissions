# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        visited = []

        while fast and fast.next:
            if fast.val in visited:
                return True
            fast = fast.next.next
            
            if slow and slow.next:
                visited.append(slow.val)
                slow = slow.next
        return False




