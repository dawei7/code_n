# Delete Nodes From Linked List Present in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3217 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [delete-nodes-from-linked-list-present-in-array](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/).

### Goal
Given an array of integers and the head of a singly linked list, remove all nodes from the linked list whose values exist within the provided array. The function should return the head of the modified linked list, ensuring that the structural integrity of the remaining nodes is preserved.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the values to be removed from the linked list.
- `head`: The head node of a singly linked list.

**Return value**

- The head of the modified linked list after all nodes with values present in `nums` have been removed.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], head = [1, 2, 3, 4, 5]`
- Output: `[4, 5]`

**Example 2**

- Input: `nums = [1], head = [1, 2, 1, 2, 1, 2]`
- Output: `[2, 2, 2]`

**Example 3**

- Input: `nums = [5], head = [1, 2, 3, 4]`
- Output: `[1, 2, 3, 4]`

---

## Solution
### Approach
The problem is solved using a Hash Set for O(1) average-time complexity lookups of the values to be deleted, combined with a single-pass traversal of the linked list using a dummy head node to simplify edge cases involving the removal of the original head.

### Complexity Analysis
- **Time Complexity**: O(N + M), where N is the number of nodes in the linked list and M is the number of elements in the input array. We iterate through the array once to build the set and the list once to filter nodes.
- **Space Complexity**: O(M), required to store the unique elements of the input array in a hash set for efficient lookup.

### Reference Implementations
<details>
<summary>python</summary>

```python
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
```
</details>
