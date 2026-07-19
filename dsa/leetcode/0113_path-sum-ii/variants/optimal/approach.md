## General
**Reuse one path buffer across sibling branches**

Depth-first search appends the current node before descending and removes it after both children return. The same mutable list therefore always represents the active root-to-current path, avoiding a path copy at every recursive edge.

When a qualifying leaf is found, append a copy of the path to the result. Appending the mutable buffer itself would make all saved answers change as backtracking pops and appends later values.

**Remaining sum and leaf status jointly define acceptance**

Pass `remaining - node.val` to the node's children. At a node with neither child, copy the path only when that new remainder is zero. An internal prefix reaching zero is not accepted because the required path must terminate at a leaf.

Node values may be negative, so a positive or negative remainder cannot safely prune a branch before its leaf.

**Entry and exit states make backtracking verifiable**

On entry to a recursive call, the path contains precisely the node's ancestors and `remaining` equals the target minus their sum. After appending the node and subtracting its value, both represent the complete root-to-node state. Popping before return restores the exact entry state for the caller's next child.

**Trace a saved path and subsequent restoration**

Following `5 -> 4 -> 11 -> 2` reduces `22` to zero at a leaf, so that path is copied. Backtracking then removes `2` and explores other branches without retaining stale values, eventually finding `5 -> 8 -> 4 -> 5`.

**The mutable buffer represents exactly one active root path**

Pushing a node extends the buffer and subtracts its value from the remaining target, so at a leaf the remainder is zero exactly when the buffered root-to-leaf path has the required sum. Only then is a copy emitted.

Popping on return restores the parent path before a sibling is explored, preventing values from different branches from mixing. DFS visits each root-to-leaf path once, so every valid path is copied once and no invalid sequence appears.

## Complexity detail
Traversal touches `n` nodes, and copying accepted paths writes `L` total returned values, giving $O(n + L)$ time. The recursion and mutable path use $O(h)$ auxiliary space; returned path copies are output.

## Alternatives and edge cases
- **Copy the path at every recursive edge:** is correct but can take $O(nh)$ work even when no path qualifies.
- **Store parent pointers then reconstruct:** avoids path buffers but adds per-node state.
- **Accept an internal matching prefix:** is invalid because every returned path must end at a leaf.
- Empty input returns an empty result, even for target zero. A one-node tree returns its singleton path only when the root value equals the target.
- Equal value sequences reached through different tree branches are distinct root-to-leaf paths and should both be returned if both qualify.
