# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to start the merged list
        dummy = ListNode(-1)
        # Pointer to traverse the merged list
        current = dummy
        # Pointers for list1 and list2
        pointer1 = list1
        pointer2 = list2
        
        while pointer1 is not None and pointer2 is not None:
            # If value of node in list1 is less than value of node in list2
            if pointer1.val < pointer2.val:
                current.next = pointer1  # Link the node from list1 to the merged list
                pointer1 = pointer1.next  # Move pointer1 to the next node in list1
            else:
                current.next = pointer2  # Link the node from list2 to the merged list
                pointer2 = pointer2.next  # Move pointer2 to the next node in list2
            current = current.next  # Move the current pointer to the last added node
        
        # If there are remaining nodes in list1 or list2, append them to the merged list
        if pointer1 is not None:
            current.next = pointer1
        elif pointer2 is not None:
            current.next = pointer2
        
        # Return the next of dummy node, which is the head of merged list
        return dummy.next
        