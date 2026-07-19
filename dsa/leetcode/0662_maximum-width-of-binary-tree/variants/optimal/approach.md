## General
**Give real nodes their complete-tree positions**

Label the root position zero. If a node has position `p`, label its left child `2p` and right child $2p + 1$ after normalizing the current level. These labels preserve exactly how many complete-tree slots separate any two real nodes, without enqueuing missing nodes.

**Measure each level by its endpoints**

Process nodes level by level. Subtract the first position on the level from every position before creating child labels. This keeps numbers small while preserving all within-level differences. The level width is `last_position - first_position + 1`; after normalization the first position is zero, so it is simply the final normalized position plus one.

**Why indices count internal gaps correctly**

Complete-tree indexing assigns consecutive positions to every conceptual slot on a level. Real nodes retain the same positions they would have if every missing ancestor slot were explicitly expanded. Therefore the inclusive difference between the outer real-node indices counts both endpoints and every internal null position required by the definition. Taking the maximum over all levels returns the desired width.

## Complexity detail
Each of the `N` real nodes enters and leaves the queue once, so time is $O(N)$. The queue stores at most one level of real nodes and can contain $O(N)$ entries, giving $O(N)$ space.

## Alternatives and edge cases
- **Depth-first search with the first index at each depth:** also runs in $O(N)$ time and uses $O(H)$ traversal state, but recursive depth may be a concern for skewed trees.
- **Materialize null placeholders:** mirrors the definition visually, but a sparse tree can create exponentially many conceptual slots relative to its real-node count.
- **Count only real nodes per level:** misses internal gaps and therefore does not implement positional width.
- A single-node tree has width one.
- A level with one real node has width one regardless of its conceptual position.
- Normalizing indices per level preserves widths and avoids unnecessarily large integers on deep trees.
