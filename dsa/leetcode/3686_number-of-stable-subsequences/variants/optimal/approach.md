## General

**Compress the history to parity-run states.** The stability rule depends only on the parity of each selected element. Furthermore, when a new element is appended to a stable subsequence, the only relevant history is the parity at its end and whether its trailing run of that parity has length one or two. A longer run is forbidden.

**Append without creating a third equal parity.** Maintain four counts: stable subsequences ending in one odd, two consecutive odds, one even, or two consecutive evens. Existing subsequences remain counted when the current array element is skipped. For a new element of parity $p$, the new subsequences ending with a run of length one are:

- the singleton containing only this element; and
- every earlier stable subsequence ending in the opposite parity, regardless of whether that opposite-parity run has length one or two.

The new subsequences ending with a run of length two come from appending the element to every earlier subsequence whose final run consists of exactly one element of parity $p$. Nothing may be appended to a length-two run of the same parity, because that would create the forbidden third consecutive element. Add the new counts to the corresponding existing states and continue from left to right.

**Count each subsequence at its final index.** Every stable subsequence is counted at the moment its final position is processed. Removing that final element places it in exactly one of the predecessor categories above, so the transitions are exhaustive and disjoint. Summing the four states after the scan therefore counts every nonempty stable subsequence once.

## Complexity detail

Each of the $n$ input values performs a constant number of state additions, so the time complexity is $O(n)$. Only four dynamic-programming counts are retained, giving $O(1)$ auxiliary space. Every update is reduced modulo $10^9+7$ to keep the counts bounded.

## Alternatives and edge cases

- **Position-based dynamic programming:** Counts can be stored for every possible final position and obtained by scanning all earlier positions, but this repeats parity totals and costs $O(n^2)$ time and $O(n)$ space.
- **Enumerating subsequences:** Testing each chosen position set directly is exact only for tiny inputs and takes exponential time.
- **Single element:** Its singleton subsequence is stable, so the answer is one.
- **All values have one parity:** Only subsequences of lengths one and two qualify; the state transition naturally prevents extending a same-parity run of length two.
- **Equal values at different positions:** They still create distinct subsequences because the count is based on selected indices, while only their parity affects stability.
