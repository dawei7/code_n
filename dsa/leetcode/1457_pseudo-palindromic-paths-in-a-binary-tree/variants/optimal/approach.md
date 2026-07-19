## General
**Reduce palindrome feasibility to frequency parity**

In any palindrome, characters on opposite sides occur in pairs. An even-length
palindrome therefore has no value with odd frequency, while an odd-length
palindrome has exactly one odd-frequency value at its center. Conversely, if a
multiset has at most one odd frequency, pair equal values around the outside
and place the optional odd value in the center. Thus a path is
pseudo-palindromic exactly when at most one of its digit counts is odd.

The actual counts are unnecessary. Store their parities in an integer mask:
bit $d$ represents whether digit $d$ has appeared an odd number of times on
the current path. Visiting a node with value `d` toggles that bit using
`mask ^ (1 << d)`. A second occurrence clears it, a third sets it again, and so
on, matching count parity exactly.

**Carry an immutable path state through iterative DFS**

Use a stack containing pairs `(node, mask_before_node)`. Pop a state, toggle
the bit for that node, and pass the resulting mask to both children. Integers
are immutable, so each pushed child receives the correct snapshot without any
backtracking mutation or frequency-array copying.

An explicit stack is important for the legal maximum of $10^5$ nodes. A
recursive depth-first search has the same algorithmic idea but can exceed the
language call-stack limit on a skewed tree. The iterative traversal handles
that shape while retaining depth-first $O(h)$ auxiliary storage.

**Recognize valid masks only at leaves**

A nonzero integer has at most one set bit exactly when
`mask & (mask - 1) == 0`; the same expression is also true for zero. Therefore
at each leaf, add one when this condition holds. Internal nodes are not counted
because only root-to-leaf paths are candidates.

For every stack entry, the incoming mask records the parities from the root
through the node's parent. Toggling the node's bit makes it the exact parity
mask from the root through that node. By induction, every child receives its
correct path state. Every leaf is reached once, and the one-bit test is
equivalent to palindrome feasibility, so the final total counts exactly all
and only pseudo-palindromic root-to-leaf paths.

## Complexity detail
Each of the $n$ nodes is pushed, popped, and processed once. Bit toggling and
the leaf test are constant-time operations over a fixed nine-digit domain, so
the running time is $O(n)$. A depth-first stack holds at most $O(h)$ pending
states, and each state contains only a node reference and one integer mask.

## Alternatives and edge cases
- **Frequency array with backtracking:** Maintain nine counters, increment on
  entry, test at a leaf, and decrement on exit. This is also $O(n)$ time and
  $O(h)$ call-stack space, but mutation makes correct backtracking essential.
- **Breadth-first traversal:** Carry a parity mask with every queued node. It
  remains $O(n)$ time but can require $O(w)$ space for maximum tree width $w$,
  which may be much larger than the height of a balanced tree.
- **Materialize every path:** Copying the values accumulated so far at every
  node and recounting at leaves is correct but can take $O(nh)$ time on deep
  trees and stores substantially more data than parity requires.
- **Single node:** Its one-bit mask is valid, so the only path contributes one.
- **Even path length:** A valid path must have zero odd-frequency digits.
- **Odd path length:** A valid path must have exactly one odd-frequency digit;
  two or more make a palindromic permutation impossible.
- **Identical path sequences at different leaves:** Count both paths because
  the requested quantity is rooted paths, not unique sequences.
- **Skewed maximum-depth tree:** Use the explicit stack to avoid recursion
  overflow while still processing every node once.
