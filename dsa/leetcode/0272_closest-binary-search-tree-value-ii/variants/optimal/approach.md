## General
**Initialize lazy predecessor and successor iterators**

Follow BST search paths to initialize a predecessor stack containing values at most the target and a successor stack containing values greater than it. Each stack can advance to its next ordered value by exploring one subtree spine.

**Merge the two ordered sides by distance**

For each of `k` selections, compare the current predecessor and successor distances. Pop the nearer value, then advance only that iterator.

The stack tops are respectively the largest unchosen value at most the target and the smallest unchosen value above it. All other unchosen values on either side are no closer than that side's top.

**One of the two stack tops is always globally closest**

Within the predecessor side, values become no closer as they decrease away from the target; within the successor side, they become no closer as they increase. Each side's top is therefore its best remaining candidate, and the globally closest unchosen value must be one of those two. Selecting the nearer top and advancing only that iterator restores the same condition for the next choice.

## Complexity detail

Initializing both stacks follows two root-to-leaf paths in $O(h)$ time. Across all $k$ selections, each node entered by
an iterator is pushed and popped at most once, so advancement costs $O(k)$ amortized time. The total is $O(h + k)$.
The two stacks contain $O(h)$ nodes; excluding the returned $k$ values, auxiliary space is $O(h)$.

## Alternatives and edge cases

- **Traverse and sort all nodes:** costs $O(n \log n)$ and ignores BST ordering.
- **Keep a size-`k` heap during full traversal:** costs $O(n \log k)$.
- **Exhausted iterator:** if one stack empties, every remaining selection must come from the other ordered side.
- **All nodes requested:** `k = n` drains both iterators and returns the whole tree in distance-selection order.
