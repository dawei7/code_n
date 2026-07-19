## General
**The middle element simultaneously enforces ordering and balanced sizes**

For inclusive interval `[left,right]`, choose a middle index. Strict array ordering makes every value on the left smaller than the root and every value on the right larger, so the recursive intervals are exactly valid BST key sets.

Either middle may be chosen for an even-length interval. The problem accepts multiple balanced shapes, and both choices keep subtree sizes within one.

**Repeated midpoint splits bound subtree-height difference**

Splitting at a midpoint makes child interval sizes differ by at most one. Each recursive level roughly halves interval size, so both child heights are determined by sizes that differ by at most one and can differ in height by at most one. Applying the same midpoint rule at every node establishes height balance throughout the tree.

**Each recursive interval owns every one of its values exactly once**

`build(left, right)` returns a height-balanced BST containing exactly the values in `nums[left:right+1]`, with no value duplicated or omitted.

**Trace an odd-sized interval and its even children**

For `[-10, -3, 0, 5, 9]`, choose `0` as the root. Recursing on `[-10, -3]` and `[5, 9]` creates two balanced BST subtrees whose values are respectively smaller and larger than the root.

**Middle splits preserve both order and height balance**

Choosing the middle value leaves only smaller keys in the left interval and larger keys in the right, so recursively attaching those intervals satisfies BST ordering at the root.

The two interval sizes differ by at most one. Repeating middle splits gives balanced child trees whose heights differ by at most one, and every input value belongs to exactly one interval and creates one node. The completed tree is therefore a height-balanced BST containing the full array.

## Complexity detail
Every one of the `n` values creates exactly one node, giving $O(n)$ time. Balanced interval splitting limits recursion depth to $O(\log n)$; returned nodes are output rather than auxiliary storage.

## Alternatives and edge cases
- **Insert values one at a time:** can require $O(n \log n)$ time even with a careful insertion order.
- **Always choose an endpoint:** preserves BST ordering but creates an unbalanced chain.
- **Array slicing:** remains correct but copies subarrays and adds avoidable allocation.
- Empty input maps to a null root. A one-element interval creates a leaf with two empty children.
- The array must be strictly increasing for the strict BST contract; duplicate-key placement would require a stated policy.
