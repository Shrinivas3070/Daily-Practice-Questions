class Solution(object):
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n+1 steps ahead
        for i in range(n + 1):
            fast = fast.next

        # Move both pointers together
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete the nth node
        slow.next = slow.next.next

        return dummy.next