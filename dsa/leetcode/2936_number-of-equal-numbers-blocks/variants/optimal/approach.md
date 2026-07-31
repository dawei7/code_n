## General

**Jump instead of walking through a block.** At the first index of a block,
read its value. Probe offsets $1,2,4,8,\ldots$ from that start while the probes
remain inside the array and return the same value. The first unequal probe, or
the end-of-array sentinel, brackets the block boundary with the last known
equal index.

**Binary-search the first different position.** Within that bracket, the
predicate “the value equals the block's starting value” is monotone: it is true
through the current block and false afterward. This monotonicity relies on the
contract that a value's occurrences are all adjacent; the same value cannot
appear in a later block. Binary search therefore finds the first unequal index,
which is the next block start. Increment the block count and repeat there.

If a block has length $L$, exponential bracketing and binary search each use
$O(\log L)$ calls to `at`. Every iteration advances to a genuine new block,
and reaching `size()` finishes the final block. Hence every maximal block is
counted exactly once without reading its individual elements.

## Complexity detail

Let $n$ be the hidden array length and $b$ its number of blocks. The total
number of reader calls is
$O\left(\sum_{i=1}^{b}(1+\log L_i)\right)$ for block lengths $L_i$, which is
$O(b\log n)$. The algorithm stores only indices, one value, and counters, so
auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Linear scan:** Compare every adjacent pair and count changes in $O(n)$ reader calls, which is infeasible when $n$ reaches $10^{15}$ and blocks are long.
- **Binary search without bracketing:** Searching the entire remaining suffix still works because equality never recurs, but costs $O(\log n)$ per block even when a block is short; exponential bracketing adapts to its length.
- **One block:** Equal probes eventually reach the array-end sentinel, producing count one without an out-of-range call.
- **Single-element array:** The first block starts at index zero and ends immediately at `size()`.
- **Adjacent singleton blocks:** The first offset probe is already different, so the boundary advances by one.
- **Repeated value later:** Such input is excluded; the binary-search predicate depends on the adjacency guarantee.
