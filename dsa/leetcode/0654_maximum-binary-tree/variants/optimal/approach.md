## General
**Maintain roots whose right side is still open**

Process values from left to right with a monotonically decreasing stack of tree nodes. The stack represents a chain of ancestors that may still receive a larger value on their right.

**Place every smaller suffix below the new value**

For a new node, pop every smaller stack top. The last popped node is the root of the entire consecutive suffix that the new value dominates, so it becomes the new node's left child. If a larger node remains on the stack, the new node is the next value in that larger node's right region and becomes its right child. Push the new node afterward.

**Why these links reproduce the recursive definition**

When a node is popped, the first later value larger than it has arrived. Everything already grouped below that node lies between the two values and is also smaller than the new value, so the popped subtree belongs on the new node's left. A node that remains below the new node is the nearest earlier larger value, making the new subtree part of its right segment. Each value therefore receives exactly the parent selected by the nearest-greater relationships implied by the recursive maximum split. After all values are processed, the bottom of the stack is the global maximum and hence the required root.

## Complexity detail
Every node is pushed once and popped at most once, so the total time is $O(N)$. The monotonic stack and constructed nodes use $O(N)$ space; the stack alone can contain all nodes for a decreasing input.

## Alternatives and edge cases
- **Recursive maximum search:** mirrors the definition directly, but rescanning every subarray becomes $O(N^2)$ on sorted input and may create deep recursion.
- **Cartesian-tree nearest-greater arrays:** can determine parents in linear time, but stores more auxiliary relationships than the direct stack construction.
- A one-element array produces a single-node tree.
- Increasing input creates a left-skewed tree rooted at the final value.
- Decreasing input creates a right-skewed tree rooted at the first value.
- Distinct input values make every maximum and parent choice unambiguous.
