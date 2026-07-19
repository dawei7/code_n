## General
**Traverse one complete level at a time**

Initialize a queue with the root. Before processing a level, the queue contains exactly that level's nodes from left to right. Record the value of its first node, then remove all nodes in the current level and append each node's left child before its right child.

**Replace the candidate only at a new level**

Every time the outer loop begins, overwrite the answer with the new queue front. Shallower candidates are intentionally discarded because any node on the current level is deeper. When the queue becomes empty, the last recorded level was the deepest one.

**Why the queue front is the required node**

The root starts in correct left-to-right order. If one level is ordered, appending each parent's left child before its right child while visiting parents left to right produces the next level in the same order. By induction, the first queued node at every level is its leftmost node, so the final recorded value is the leftmost value at maximum depth.

## Complexity detail
Each of `n` nodes enters and leaves the queue once, giving $O(n)$ time. The queue holds at most one level and can contain $O(n)$ nodes in a wide tree, so space is $O(n)$.

## Alternatives and edge cases
- **Depth-first search:** record the first value seen at each new maximum depth by visiting left before right; it uses $O(h)$ stack space.
- **Right-to-left breadth-first search:** enqueue right before left and return the final node visited, also in $O(n)$ time.
- **Rescan separately for every depth:** is correct but can take $O(n^2)$ time on a skewed tree.
- **Single node:** is both the deepest and leftmost node.
- **Only right children:** each level still has one leftmost node.
- **Several deepest leaves:** select the first from the left, not the smallest value.
- **Negative values:** do not affect structural ordering.
