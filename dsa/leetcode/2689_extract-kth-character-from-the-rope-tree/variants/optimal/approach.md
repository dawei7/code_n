## General

**Translate the global position at each node**

At an internal node, determine how many characters its left child represents. An internal left child stores this length in `len`; a leaf uses `len(val)` because every leaf has `len = 0`. A missing left child contributes zero.

If the one-based position `k` is at most that left length, the desired character lies in the left subtree and `k` remains unchanged. Otherwise it lies in the right subtree; subtract the complete left length before moving right so `k` becomes relative to that subtree. Repeat until reaching a leaf, then return `val[k - 1]`.

The two cases partition every valid position in the current rope string. After either move, `k` denotes the same original character within the selected child. Maintaining that interpretation at every level proves that the final leaf indexing returns exactly the requested character, without constructing unrelated portions of the rope.

## Complexity detail

Let $h$ be the number of nodes on the root-to-target-leaf path. The algorithm visits only that path, taking $O(h)$ time. The iterative descent stores only the current node, position, and left length, so it uses $O(1)$ additional space. The benchmark uses `size` as $h$ and contrasts descent with materializing an entire balanced rope whose node count and represented length grow exponentially with height.

## Alternatives and edge cases

- **Materialize the complete rope:** Recursively concatenate all leaf strings and index the result. This is simple but does work proportional to the represented string and allocates that full string.
- **Recursive targeted descent:** The same length-guided decisions can be written recursively, but then consume $O(h)$ call-stack space.
- A root leaf requires no descent; index its non-empty `val` directly.
- The boundary `k == left_length` still belongs to the left subtree.
- On a right move, subtract the entire left length before continuing.
- A missing left child has length zero, so every valid position proceeds right.
- Leaf nodes signal their length through `val`, because their stored `len` is always zero.
