 #Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode()
        dummy = head
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            # print(f'dummy: {dummy.next}')
            # print(f'head : {head.next}')
            head = head.next
            # print(f'dummy: {dummy.next}')
            # print(f'head : {head.next}')

        if list1:
            head.next = list1
        if list2:
            head.next = list2
        return dummy.next
    # 1 -> 3
    # 2 -> 4
    # 1 -> 2 -> 3 -> 4
    def mergeTwoLists_rec(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 or not list2:
            return list1 or list2
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergeTwoLists_rec(list1.next, list2)
        return list1


sol = Solution()
node11 = ListNode(1)
node12 = ListNode(2)
node13 = ListNode(3)
node14 = ListNode(4)

node11.next = node12
node12.next = node13
node13.next = node14
#print(node11.next.next.val)
node21 = ListNode(1)
node22 = ListNode(3)
node23 = ListNode(4)
node24 = ListNode(7)
node25 = ListNode(9)
node26 = ListNode(13)

node21.next = node22
node22.next = node23
node23.next = node24
node24.next = node25
node25.next = node26

cur_node = node11
linked_list1 = node11
linked_list2 = node21

new_list = sol.mergeTwoLists_rec(linked_list1, linked_list2)

while True:
    print(new_list.val)
    if new_list.next is None:
        break
    new_list = new_list.next


# while True:
#     print (f'{cur_node.val} -> ', end='')
#     if cur_node.next is None:
#         print("None", end='')
#         break
#     cur_node = cur_node.next

