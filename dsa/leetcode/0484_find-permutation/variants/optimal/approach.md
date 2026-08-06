## General

**Begin with the smallest unconstrained permutation**

Let $n = \lvert \texttt{s} \rvert$. Initialize `permutation` to `[1, 2, ..., n + 1]`. This is lexicographically
smallest before enforcing any decreases, and every `I` already agrees with its ascending order. Only maximal runs of
`D` need to change the arrangement.

**Close and reverse each decrease run**

`run_start` is the first permutation position belonging to the current block. Scan `boundary` from `0` through $n$.
When `s[boundary]` is `D`, keep extending the block. An `I`, or the sentinel position `boundary == n`, closes it.
At that point, `s[run_start:boundary]` contains only `D`, so reverse the inclusive permutation block from
`run_start` through `boundary` with two pointers. Then set `run_start` to `boundary + 1` for the next block.

If there was no decrease since the preceding boundary, the block has one value and the reversal changes nothing.
The sentinel applies the same logic to a run that reaches the end of the pattern, without a separate cleanup loop.

**Why the construction is valid and lexicographically smallest**

A run of $k$ consecutive `D` characters requires its $k + 1$ adjacent permutation values to be strictly
decreasing. Reversing their initially consecutive ascending values creates exactly those $k$ decreases. Values in
the next block are all larger than values in the preceding block, so every `I` boundary is also satisfied.

For lexicographic minimality, consider blocks from left to right. The earliest position of a block must use the
smallest still-available group of values; choosing any larger value there would make the result lexicographically
larger immediately. Within a decrease block, strict descent uniquely forces those values into reverse order. The
algorithm makes exactly these forced smallest choices for every block, so no other valid permutation has a smaller
first differing value.

## Complexity detail

Creating the initial permutation takes $O(n)$ time. Every position participates in one block reversal and moves at
most once through its two-pointer swaps, so the scan and all reversals also take $O(n)$ total time.

The returned permutation occupies $O(n)$ space. Apart from that required output, the algorithm uses $O(1)$ auxiliary
space for the block and swap positions.

## Alternatives and edge cases

- **Stack flush at each increase:** push successive values and pop the stack whenever an `I` or the final sentinel
  closes a block. This is also $O(n)$ time but uses $O(n)$ auxiliary stack space.
- **Repeated adjacent swaps:** bubbling each new value left across its current decrease run is correct, but an all-`D`
  pattern requires $O(n^2)$ swaps.
- **Permutation enumeration:** can select the smallest valid permutation only after factorial work and is infeasible
  for the source bounds.
- **All increases:** every reversal is a one-value no-op, leaving `[1, 2, ..., n + 1]`.
- **All decreases:** the sentinel closes one run and reverses the entire permutation.
- **Separated decrease runs:** an intervening `I` closes the first block; combining blocks across it would destroy
  the required increase.
- **Single-character pattern:** `"I"` yields `[1,2]`, while `"D"` reverses that block to `[2,1]`.
