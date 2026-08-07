## Function Contract

**Inputs**

- `head`: The head `ListNode` of a singly linked list containing $1 \le N \le 10^5$ nodes, sorted in non-decreasing order by absolute values.

```python
class ListNode:

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next
```

**Return value**

Return the `ListNode` head of the relinked list sorted in non-decreasing order by signed values.
