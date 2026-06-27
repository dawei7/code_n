class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(nums: list[int], head: ListNode) -> ListNode:
    # Convert nums to a set for O(1) average lookup time
    val_set = set(nums)
    
    # Use a dummy node to handle cases where the head itself needs to be removed
    dummy = ListNode(0)
    dummy.next = head
    
    current = dummy
    
    # Traverse the list and remove nodes whose values are in the set
    while current.next:
        if current.next.val in val_set:
            # Skip the node
            current.next = current.next.next
        else:
            # Move to the next node
            current = current.next
            
    return dummy.next
