## General
Let $B$ be the number of births, $D$ the number of deaths, $G$ the number of order queries, and $P$ the number of people present when a query runs.

**Store the permanent family tree.** Map every parent name to a list of children appended in birth order. A birth is one list append. Maintain dead names in a hash set, so death is a membership-state update rather than a structural deletion. This distinction is essential because a dead person's descendants keep their inherited location.

**Generate succession as a preorder traversal.** Start at the king, visit the person, and then traverse each child subtree from oldest to youngest. Append a visited name only if it is not dead, but always traverse its children. An explicit stack avoids recursion-depth failure for a family chain approaching $10^5$ people. Push children in reverse order so the oldest is popped first.

The family adjacency lists contain every birth edge exactly once and preserve sibling age order. Preorder therefore implements the recursive successor rule: a person is followed by their oldest unvisited descendant branch before any younger sibling branch. Filtering a dead person's name without pruning that node leaves every descendant in precisely the position the unchanged family tree assigns. Hence each query returns all and only living people in the unique required order.

**Adapting the object trace locally.** The `solve` adapter constructs one object, dispatches calls sequentially, emits `None` for void mutations, and records each query result. This preserves state across the complete authored operation trace.

## Complexity detail
Each birth appends once and each death inserts once, for $O(B+D)$ expected mutation time. Every query visits each of the $P$ people once, for $O(P)$ time per query and $O(B+D+GP)$ total. The child lists, dead set, and traversal stack store $O(P)$ names. The returned order itself is required output.

## Alternatives and edge cases
- **Rebuild the full order after every birth:** This remains correct but repeats preorder work even when no query occurs, producing quadratic behavior over a long birth sequence.
- **Remove dead nodes from the tree:** This is incorrect because it can also disconnect or reorder their descendants; death is only a filter on query output.
- **Recursive DFS:** It expresses preorder directly but can exceed the language recursion limit on a deep lineage.
- Several children of one parent must remain in birth order, not alphabetical order.
- The king may die; an order query then begins with the first living person in the king's descendant preorder.
- A dead person may have living descendants, all of whom remain eligible.
- Repeated order queries without intervening mutations return equal lists.
