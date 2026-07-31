## Function Contract

**Inputs**

- `headA`: The first `ListNode` head, encoded in app cases with its private prefix and the shared tail.
- `headB`: The second `ListNode` head, encoded with its own prefix and the same shared tail. The runner constructs one shared set of node objects for that tail.

**Return value**

Return the first shared `ListNode`. The app displays that node as its suffix values; a `null` result is displayed as `[]`.
