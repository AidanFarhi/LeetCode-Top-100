# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class OddEvenLL:
    """
    Given the head of a singly linked list, 
    group all the nodes with odd indices together followed by the nodes with even indices, 
    and return the reordered list.
    The first node is considered odd, and the second node is even, and so on.
    Note that the relative order inside both the even and odd groups should remain as it was in the input.
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]
    """
    def oddEvenList(self, head):
        # Check for LL of size 0 or 1
        if head is None or head.next is None:
            return head
        # The idea is to chain all the even nodes together
        # while chaining all the odd nodes together,
        # and then add the head of the even nodes to the end
        # of the odd nodes
        n = head
        even_head = n.next
        even_tail = even_head
        while True:
            # Termination case
            if n.next is None or n.next.next is None:
                n.next = even_head # add head of even nodes to end of odd nodes
                break
            n.next = n.next.next # chain odd nodes
            n = n.next           
            even_tail.next = n.next # chain even nodes
            even_tail = even_tail.next
        return head