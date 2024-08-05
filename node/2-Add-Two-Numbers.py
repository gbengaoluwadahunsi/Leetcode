# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def extract_number(node):
            num = ''
            while node:
                num = str(node.val) + num  # Reverse order while traversing
                node = node.next
            return num

        # Extract numbers from both lists
        num1 = extract_number(l1)
        num2 = extract_number(l2)

        # Convert extracted numbers to integers and add them
        total = int(num1) + int(num2)

        # Convert the result back to a linked list
        head = ListNode(int(str(total)[-1]))
        current = head
        for digit in str(total)[-2::-1]:
            current.next = ListNode(int(digit))
            current = current.next

        return head