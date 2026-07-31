## General

**Use each separator to finish one group**

Skip the leading zero and scan the remaining nodes from left to right. Add
every positive value to a running group sum. Encountering a zero means the
current group is complete, so write its sum into the next output position,
reset the accumulator, and continue with the following group.

**Emit one compact value per group**

The app adapter appends each completed sum to the serialized result list. The
native linked-list source applies the same scan while reusing early input
nodes: sums overwrite nodes whose original values have already been consumed,
and the final output node is disconnected from the unused suffix.

Every positive node belongs to exactly one interval between consecutive
zeros, and its value is added once before that interval's closing separator.
Exactly one output node is written at each closing separator. The algorithm
therefore produces every required group sum once, in its original order, and
does not retain a separator.

## Complexity detail

Let $n$ be the number of input nodes. The read pointer visits each node once,
so the time complexity is $O(n)$. The serialized app result can contain
$O(n)$ group sums, giving an $O(n)$ space bound. The native linked-list source
instead reuses input nodes and needs only $O(1)$ auxiliary space.

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
