# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeLists:
    """
    Merge two sorted linked lists and return it as a sorted list. 
    The list should be made by splicing together the nodes of the first two lists.
    Example 1:
    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode()
        m = new_head
        n1 = l1
        n2 = l2
        while n1 or n2:
            if n1:
                if n2:
                    if n1.val < n2.val:
                        m.next = ListNode(n1.val)
                        m = m.next
                        n1 = n1.next
                    else:
                        m.next = ListNode(n2.val)
                        m = m.next
                        n2 = n2.next
                else:
                    m.next = ListNode(n1.val)
                    m = m.next
                    n1 = n1.next
            else:
                m.next = ListNode(n2.val)
                m = m.next
                n2 = n2.next

        return new_head.next