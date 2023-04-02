# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur_head = head
        if not head:
            return head
        while cur_head.next:
            if cur_head.val == cur_head.next.val:
                cur_head.next = cur_head.next.next
            else:
                cur_head = cur_head.next
        return head

# 1 -> 2 -> 2 -> 3 -> 3 -> 3


node21 = ListNode(1)
node22 = ListNode(1)
node23 = ListNode(1)
node24 = ListNode(1)
node25 = ListNode(1)
node26 = ListNode(1)

node21.next = node22
node22.next = node23
node23.next = node24
node24.next = node25
node25.next = node26

linked_list = node21

sol = Solution()

new_list = sol.deleteDuplicates(linked_list)

while True:
    print(new_list.val)
    if new_list.next is None:
        break
    new_list = new_list.next
