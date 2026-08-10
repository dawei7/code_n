## General

In an arbitrary binary tree, counting frequencies usually requires a dictionary. A binary search tree provides extra structure: inorder traversal visits values in non-decreasing order. All occurrences of one value therefore appear consecutively, so the solution can count one run at a time without storing a frequency entry for every distinct value.

The recursive order is exactly:

1. traverse the left subtree;
2. process the current node;
3. traverse the right subtree.

The BST permits duplicate values on either side under the stated `<=` and `>=` rules, but inorder output is still non-decreasing. A duplicate placed in a left subtree cannot appear after a larger value, and a duplicate in a right subtree cannot appear before a smaller value. All equal values remain one contiguous run in the complete sorted traversal.

**State carried between consecutive inorder values.**

- `prev` is the value processed immediately before the current node;
- `cnt` is the length of the current run of `prev`;
- `mx` is the largest completed or current run length seen so far;
- `ans` contains every value whose run has reached the current maximum frequency.

Initially `prev = None` and `cnt = mx = 0`. Node values are integers, so `None` cannot accidentally equal the first value. The first processed node starts a new run of length one.

At each node, the code evaluates

`cnt = cnt + 1 if prev == root.val else 1`.

If the sorted traversal is still on the same value, its run grows by one. If the value changed, the previous run has ended and the new value begins with count one.

**Update the modes while the run grows.** If `cnt > mx`, the current value has established a frequency greater than every value seen earlier. Every old answer is no longer a mode, so the code replaces the entire list with `[root.val]` and sets `mx = cnt`.

If `cnt == mx`, the current value ties the greatest frequency and is appended. Because equal values are contiguous, a particular value reaches a given positive count only once while its single run grows. It will not be appended multiple times for the same maximum.

When `cnt < mx`, the current run has not caught the leaders, so `ans` is unchanged.

After processing the count, `prev = root.val` prepares for the next node in inorder order. Updating `prev` before traversing the right subtree is essential because the first value in that subtree is the next value in the global traversal.

Consider inorder values `[1, 2, 2, 3, 3]`. Value one sets `mx = 1` and `ans = [1]`. The first two ties that maximum and appends, but the second two reaches count two, exceeds `mx`, and resets the answer to `[2]`. The first three has count one and changes nothing; the second reaches two and appends three. The final answer is `[2, 3]`.

This example also explains why temporarily appending a value at count one is harmless. If its run later exceeds the old maximum, the `cnt > mx` branch resets the answer and removes all obsolete entries, including earlier temporary ties.

**Why no end-of-run action is needed.** Some run-length algorithms wait until a value changes before comparing its completed count. This source compares after every occurrence. The last run is therefore fully handled at its last node even though no following different value arrives to close it. There is no special cleanup after DFS.

Correctness follows from the inorder and run invariants. Inorder traversal places all equal values contiguously, so `cnt` equals the exact frequency-so-far of the current value and reaches its total frequency at the run's final node. `mx` and `ans` are updated for every increase and tie. Once all nodes have been visited, every distinct value's total run length has been compared, `mx` is the global maximum frequency, and `ans` contains exactly all values attaining it.

The tree is guaranteed to contain at least one node, so the result cannot remain empty. The recursive null check is still necessary for missing children.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Inorder DFS visits each node exactly once and performs constant work there, so time is $O(n)$.

The traversal uses $O(h)$ recursion-stack space. In a balanced BST, $h = O(\log n)$; in a completely skewed tree, $h = O(n)$. The answer can itself contain $O(n)$ modes when every value occurs once. Including output and worst-case stack, the manifest's space bound is $O(n)$.

Under the follow-up convention that implicit recursion space and required output are excluded, the frequency-tracking state is only `prev`, `cnt`, and `mx`, which is $O(1)$. A Morris inorder traversal can also eliminate the call stack if true constant traversal space is required.

## Alternatives and edge cases

- **Frequency dictionary:** Traverse any binary tree, count each value, find the maximum, and collect matching keys. It is straightforward but uses $O(n)$ map space and ignores BST ordering.
- **Materialize inorder values:** Store the sorted traversal in a list and scan runs afterward. It is easy to visualize but duplicates the node values in memory.
- **Morris traversal:** Temporarily thread the tree to perform inorder traversal with $O(1)$ auxiliary traversal space. It is more intricate and must restore tree links carefully.
- **One node:** The first run reaches count one, becomes the maximum, and that value is returned.
- **All values equal:** `cnt` grows at every node; each new maximum resets `ans` to the same single value, so the final answer contains it once.
- **All values distinct:** Every run has length one. The first establishes `mx = 1` and every later value ties, so all values are returned.
- **Several modes:** Separate runs that finish at the same maximum are appended in inorder order, which is allowed because any answer order is accepted.
- **Recursion depth:** A skewed tree with up to ten thousand nodes may approach Python's recursion limit; iterative or Morris traversal avoids that runtime concern.
