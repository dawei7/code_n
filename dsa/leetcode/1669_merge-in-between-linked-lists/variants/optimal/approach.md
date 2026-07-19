## General
**Locate the left splice boundary.** Start at the head of `list1` and advance $a-1$ links. The resulting node, `before`, must remain in the output and is the node whose `next` pointer will be redirected to `list2`.

**Preserve the right splice boundary.** From `before`, advance $b-a+2$ links. This reaches the node at original index $b+1$, named `after`. Saving this pointer before changing either list ensures the retained suffix cannot be lost when the removed interval is detached.

**Find the insertion tail.** Walk from the head of `list2` until its last node. Redirect `before.next` to the head of `list2`, then redirect that tail's `next` to `after`. The head of `list1` never changes because $a \ge 1$, so return it directly.

**Why exactly the intended nodes remain.** Nodes before index $a$ retain all original links except the last prefix edge, which now enters `list2`. All nodes of `list2` retain their internal order, and its former null tail edge now enters the original suffix at index $b+1$. No output edge enters any node from the removed interval $[a,b]$, while every retained or inserted node is reachable exactly once from the unchanged head.

## Complexity detail
The scans visit at most the $n$ nodes of `list1` needed to reach the right boundary and all $m$ nodes of `list2` needed to find its tail, for $O(n+m)$ time. Only a constant number of node pointers and loop counters are stored, so the operation uses $O(1)$ auxiliary space and allocates no replacement list nodes.

## Alternatives and edge cases
- **Copy values into an array:** Constructing the desired value sequence is straightforward, but rebuilding nodes violates the intended in-place splice and requires $O(n+m)$ extra space.
- **Dummy-head splice:** A sentinel can unify cases where the removed range starts at zero, but the contract guarantees $a \ge 1$, so the real predecessor always exists.
- **Recursive traversal:** Recursion can locate boundaries, but it adds $O(n+m)$ call-stack space without simplifying the two pointer rewrites.
- Indices are zero-based and `b` is inclusive; the retained suffix begins at `b + 1`.
- `a` may equal `b`, in which case exactly one node is replaced.
- `list2` may contain a single node, making its head and tail identical.
- Duplicate values do not affect the operation because boundaries are positional, not value-based.
- The legal extremes `a = 1` and `b = n - 2` still leave one original node on each side of the splice.
