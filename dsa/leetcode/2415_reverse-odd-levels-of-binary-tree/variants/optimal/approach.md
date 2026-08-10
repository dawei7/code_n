## General

**Keep one whole level in breadth-first order**

Breadth-first traversal visits nodes level by level from left to right. At the start of each outer-loop iteration, deque `q` contains exactly all nodes of level `i` in their natural order.

If `i` is odd, reversing that level's values means swapping the first and last values, second and second-last values, and continuing inward. The tree nodes and links remain where they are; only `val` fields change.

**Reverse values with two indices**

For an odd level, `l` starts at zero and `r` at `len(q) - 1`. While `l < r`, the code exchanges:

```python
q[l].val, q[r].val = q[r].val, q[l].val
```

Then it moves both indices inward. A middle node on a level with odd width would remain unchanged, as a reversal requires. Perfect binary-tree levels have powers of two nodes, so every non-root level width is even, but the loop is correct generally.

Swapping values rather than node references preserves the perfect tree's topology and all parent-child relationships.

**Advance to the next level**

After optional reversal, the source snapshots current level size with `range(len(q))`. It pops exactly that many nodes from the left. For every non-leaf, it appends left child then right child.

Because the tree is perfect, a node with a left child also has a right child, so checking only `if node.left` is sufficient before appending both.

Children appended during this loop are not processed immediately because the range length was determined before appending. When the loop finishes, `q` contains precisely the next level in left-to-right order.

Finally, `i += 1` updates parity.

**Trace a three-level tree**

Initially, the queue contains only the root at level zero. Zero is even, so no swap occurs. Processing the root enqueues its left and right children.

At level one, the queue contains those two nodes in left-to-right order. Odd parity swaps their values. Their children are then appended in natural order.

Level two is even, so its values remain. This produces the first example's swap of three and five without moving their subtrees.

**Why level order is preserved**

Inductively assume `q` begins with one complete level ordered from left to right. Value swaps do not change node order. Popping parents left to right and appending each left child before right child produces the next level's standard left-to-right order.

Thus, when an odd level is reversed, symmetric deque positions correspond exactly to symmetric positions in that level.

**Why the transformation is correct**

At every even level, the algorithm performs no value assignment, so values remain unchanged. At every odd level, two-pointer swaps map original position `p` to position `width - 1 - p`, which is the definition of reversal.

Each node belongs to exactly one processed level, and tree links never change. After the queue empties, every required level has been reversed exactly once and every other level preserved. Returning the original root reference returns the modified tree.

**Exact source versus the manifest summary**

The manifest describes traversing mirrored node pairs recursively with $O(\log n)$ stack space. The source uses breadth-first traversal and stores an entire level. Both modify the same values, but their memory and Python operation costs differ.

There is also a Python-specific performance detail: `collections.deque` supports indexing, but arbitrary middle indexing is linear in distance from an end, not constant time. Repeated `q[l]` and `q[r]` accesses across a wide level can therefore cost more than a list-based two-pointer reversal.

## Complexity detail

Enqueueing and dequeueing every node takes $O(n)$ total time. If level storage offered constant-time random indexing, all swaps across levels would also total $O(n)$.

For the exact Python deque, indexing positions across a level of width $w$ can make its reversal cost $O(w^2)$ in the worst case. A wide odd level can therefore give a conservative operational worst-case time of $O(n^2)$, even though the intended BFS algorithm is linear.

The deque holds up to the maximum tree width, which is $O(n)$ for a perfect tree. Exact auxiliary space is $O(n)$, not the manifest's $O(\log n)$ mirrored-recursion bound.

## Alternatives and edge cases

- **Mirrored recursive DFS:** Recurse on `(left.left, right.right)` and `(left.right, right.left)`, swapping at odd depths. It achieves $O(n)$ time and $O(\log n)$ stack space in a perfect tree.
- **Convert each level deque to a list:** A list provides constant-time indexing, restoring $O(n)$ total BFS reversal time at the cost of level-sized copying.
- **Swap node references:** This is unnecessary and risks changing topology; only values should reverse.
- **Single-node tree:** Level zero is even, the queue empties, and root is unchanged.
- **Only level one below root:** The two child values swap.
- **Even levels:** They are traversed but never reversed.
- **Perfect-tree guarantee:** Checking only the left child safely implies a right child exists.
- **Duplicate values:** Position reversal remains well-defined even if the visible sequence looks unchanged.
- **Root identity:** The same root object is returned after in-place value updates.
