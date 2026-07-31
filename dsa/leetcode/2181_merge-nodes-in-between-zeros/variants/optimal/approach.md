## General

**Use each separator to finish one group**

Keep a read pointer at the first node after the leading zero and a write
pointer at that leading node. Starting from `read`, add values until reaching
the next zero. That separator finishes one group, so overwrite `write.val`
with the accumulated sum.

**Emit one compact value per group**

Advance `read` beyond the separator. If another group remains, advance
`write` once and repeat. After the final group, set `write.next = None` so the
last output node is disconnected from the consumed suffix. Return the original
head, which now begins the compact list of group sums.

Every positive node belongs to exactly one interval between consecutive
zeros, and its value is added once before that interval's closing separator.
Exactly one output node is written at each closing separator. The algorithm
therefore produces every required group sum once, in its original order, and
does not retain a separator.

## Complexity detail

Let $n$ be the number of input nodes. The read pointer visits each node once,
so the time complexity is $O(n)$. The algorithm reuses input nodes and stores
only pointers and one running sum, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Allocate a fresh output list:** Append each completed group sum to a new
  list. This remains $O(n)$ time but uses $O(g)$ additional storage for $g$
  groups instead of reusing nodes.
- **Recompute every partial group sum:** Rescan from the last separator to the
  current node after each step. It is correct but takes $O(n^2)$ time when one
  group contains most of the list.
- The minimum list `[0,x,0]` produces the single-node result `[x]`.
- A group may contain one value, which is copied unchanged into its result
  node.
- Group sums can exceed the per-node input bound of `1000`.
- The guaranteed leading and trailing zeros mean no unfinished group remains
  before or after the scan.
