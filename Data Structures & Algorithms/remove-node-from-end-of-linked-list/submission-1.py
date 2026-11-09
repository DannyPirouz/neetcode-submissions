# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1

        tail = head

        while tail and tail.next:
            tail = tail.next
            length += 1
            print(length)
        position = length - n

        curr = head
        prev = head
        if position == 0:
            head = head.next
            return head
        while position != 0:
            prev = curr
            curr = curr.next
            position -= 1
        
        prev.next = curr.next
        
        return head