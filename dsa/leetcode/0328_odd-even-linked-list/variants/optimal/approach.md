## General
**Grow two chains through alternating nodes**

The first node begins the odd-position chain and the second begins the even-position chain. Save the even head because it must be attached after the completed odd chain. Maintain `odd` and `even` as the tails of their respective chains.

While an odd successor remains after the current even node, link `odd.next` to that successor and advance `odd`. Then link `even.next` to the following node and advance `even`. Each iteration transfers one original odd-position node and, when present, one original even-position node into their final chains.

**Save the even head before any links change**

For `[1,2,3,4,5]`, the odd tail moves through `1 -> 3 -> 5`, while the even tail moves through `2 -> 4`. The pointer to node two would be difficult to recover after rewiring, so retain it from the beginning. Once no further pair exists, set the odd tail's next pointer to that saved even head.

The loop condition checks both `even` and `even.next`, covering odd and even list lengths without dereferencing a missing node. Empty and one-node lists can return immediately.

**Each node enters exactly its position-parity chain**

Before each iteration, the odd chain contains all processed odd-position nodes in original order, and the even chain contains all processed even-position nodes in original order. The next two pointer assignments append precisely the next node of each parity, so this statement remains true.

When the loop ends, every original node belongs to exactly one of the two chains. Connecting the odd tail to the saved even head produces the required concatenation, preserves both internal orders, and terminates at the original even tail without losing or duplicating nodes.

## Complexity detail
Each node is advanced through at most once, giving $O(n)$ time. The algorithm stores only three node references beyond the input structure, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Collect odd and even nodes in arrays:** is linear time but uses $O(n)$ extra space.
- **Repeatedly traverse from the head to find the next positional node:** preserves order but can take $O(n^2)$ time.
- The grouping uses one-based positions, not node values. Duplicate values therefore need no special treatment.
- Empty, one-node, and two-node lists already satisfy the required grouping. Odd-length lists leave one extra node in the odd chain.
