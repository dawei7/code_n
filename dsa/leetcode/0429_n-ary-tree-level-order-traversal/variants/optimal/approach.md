## General
**Keep exactly the pending frontier in a queue**

Begin with the root. At the start of each outer iteration, the queue contains precisely one depth level. Record its current length, remove exactly that many nodes from the front, append their values to one level list, and add their children to the back in stored order.

**Use the level size as a boundary marker**

Children appended while processing a level must not be included in that same output group. Capturing the queue length before removals separates the current frontier from the next one without sentinels or per-node depth fields.

**Why grouping and order are preserved**

Initially the queue contains only depth zero. If it contains one level in left-to-right order, processing those nodes in queue order outputs that level correctly, and appending each node's children in order produces the complete next level in left-to-right order. Induction over the depths proves every node appears in exactly its proper group.

## Complexity detail
Every node enters and leaves the deque once, so time is $O(n)$. The queue contains at most the tree's maximum width `w`, giving $O(w)$ auxiliary space; the returned levels are excluded.

## Alternatives and edge cases
- **Depth-first grouping:** pass a depth through recursion and append into a per-depth list; this also takes $O(n)$ time with $O(h)$ call-stack space.
- **Rebuild the queue after every front removal:** remains correct but copying all remaining nodes can take $O(n^2)$ on a wide level.
- **Sentinel markers:** can delimit levels but require careful handling to avoid an extra empty level.
- **Empty tree:** return an empty outer list.
- **Single node:** return one level containing one value.
- **Uneven branching:** the saved frontier length keeps children of different parents in the next level.
