class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        left=head
        right=self.getMid(head)


        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
    def getMid(self,head):
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        return slow

    def merge(self,left,right):
        tail=dummy=ListNode()
        while left and right:
            if left.val<right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next
        if left:
            tail.next=left
        if right:
            tail.next=right
        return dummy.next


        