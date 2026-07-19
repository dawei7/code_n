## General
**Count valid fixed-length bit suffixes**

Let `ways[length]` be the number of binary strings of that length with no consecutive ones. A valid string either begins with `0` followed by any valid string of length one less, or begins with `10` followed by any valid string of length two less. Thus `ways[length] = ways[length - 1] + ways[length - 2]`, with `ways[0] = 1` and `ways[1] = 2`.

**Follow the upper bound from its highest bit**

Scan the bits of `n` from most significant to least. Whenever the current bit of `n` is one, count all smaller numbers that match the earlier prefix, put zero at this bit, and use any valid assignment for the remaining lower bits. That contributes `ways[bitIndex]`.

**Stop when the bound itself becomes invalid**

Track whether the previous bit of `n` was one. If another one follows, the matching prefix already contains `11`; no valid number can continue matching it, so the accumulated smaller-prefix count is final.

**Include the bound when it is valid**

If the scan finishes without consecutive ones, `n` itself has not yet been counted because every contribution took a smaller zero branch. Add one for `n`.

**Why every valid integer is counted once**

Compare any valid $x \le n$ with `n` at their first differing bit. If they differ, `n` has one and `x` has zero there; the algorithm counts `x` in exactly that bit's suffix block. If they never differ, then $x = n$, which is included only after confirming the bound is valid. These disjoint cases cover all valid integers and exclude every value above `n`.

## Complexity detail
The number of relevant bits is $O(\log n)$. Building the Fibonacci-style counts and scanning the bits each take linear time in that bit count, so total time is $O(\log n)$. The count array stores $O(\log n)$ integers.

## Alternatives and edge cases
- **Digit DP with position, previous bit, and tight flag:** has the same $O(\log n)$ state count and generalizes to other bit constraints.
- **Enumerate every integer:** checking $x \mathbin{\&} (x \gg 1)$ is simple but takes $O(n)$ candidate iterations.
- **Generate valid binary strings:** avoids invalid candidates but needs careful comparison with `n`.
- **$n = 0$:** counts zero itself and returns one.
- **Bound contains `11`:** stop at the first such prefix and do not include `n`.
- **Bound is valid:** add the final one for the bound.
- **Leading zeros:** are naturally represented by shorter numbers within the fixed bit width.
- **Alternating-bit bound:** can itself be the largest valid pattern of its width.
