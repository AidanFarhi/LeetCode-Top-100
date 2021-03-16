public class ReverseLinkedList {
    // Given the head of a singly linked list, 
    // reverse the list, and return the reversed list.
    // Can you do it recursively and iteratively?
    private class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    // Iterative approach
    public ListNode reverseListIterative(ListNode head) {
        ListNode dummy = null;  // dummy head
        ListNode current = head;
        while (current != null) {
            ListNode n = current.next;
            current.next = dummy;
            dummy = current;
            current = n;
        }
        return dummy;
    }

    public ListNode reverseListRecursive(ListNode head) {
        if (head.next != null) {
            head = reverseListRecursive(head.next);
        }
        return head;
    }
}
