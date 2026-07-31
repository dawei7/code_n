## General

Let `prefix[j]` be the sum of the first `j` values, with `prefix[0] = 0`. Then the sum of `nums[l..r]` is `prefix[r + 1] - prefix[l]`. Because every array value is positive, the prefix sums are strictly increasing. That order makes it possible to maintain numeric ranges with forward-only pointers.

A positive integer has leading digit `x` exactly when it belongs to one of the disjoint ranges

$$
[x \cdot 10^p,\ (x+1)\cdot 10^p-1]
$$

for an integer $p \ge 0$. Process every such range whose lower endpoint does not exceed the total sum $S$. For one range `[lower, upper]` and a fixed right prefix `R`, a prior prefix `L` produces an in-range subarray sum precisely when

$$
R-\texttt{upper} \le L \le R-\texttt{lower}.
$$

Scan right prefixes in increasing order. An `add` pointer inserts prior prefixes once they are at most `R - lower`; a `remove` pointer erases them once they fall below `R - upper`. Both bounds rise with `R`, so neither pointer ever moves backward. Since `lower` is positive, the current right prefix is never inserted into its own window.

The remaining last-digit condition is a residue equation. The difference `R - L` ends in `x` exactly when

$$
L \bmod 10 = (R-x) \bmod 10.
$$

Maintain ten counts for the residues of prefixes in the active range and add the required residue count for each right endpoint. Every valid sum lies in exactly one leading-digit range, so it is counted once. Every counted pair satisfies both the numeric range and residue equation, proving that no invalid subarray is included.

## Complexity detail

Let $S$ be the total array sum. There are $O(\log S)$ relevant powers of ten. For each one, the right scan and both window pointers traverse the $n+1$ prefix sums at most once. The running time is $O(n\log S)$ and the prefix array uses $O(n)$ space. Under the source constraints, $S \le 10^{14}$, so at most 15 decimal scales are processed.

## Alternatives and edge cases

- **Enumerate all intervals with running sums:** Updating each sum incrementally avoids repeated addition but still examines $O(n^2)$ subarrays, which is too slow for $n = 10^5$.
- **Binary search residue buckets:** Store prefix sums separately by residue and perform two binary searches for every right endpoint and scale. This is correct but adds an avoidable $\log n$ factor.
- **Fenwick tree with coordinate compression:** Range-count queries can enforce the numeric bounds, but separate residue structures and logarithmic updates are more complicated than monotone windows.
- **Positive values:** Strictly increasing prefix sums are essential to the forward-only pointers. Zero or negative values would invalidate this ordering argument, but they are excluded by the contract.
- **One-digit sums:** At scale $p=0$, the leading-digit range is the singleton `[x, x]`; the residue test remains consistent and counts that sum once.
- **No leading zero:** The requested digit ranges from `1` through `9`, matching the fact that a positive decimal representation never begins with zero.
- **Overlapping intervals:** Each distinct prefix pair represents a distinct subarray and must be counted even when another interval overlaps it or has the same sum.
- **Large answer:** The count can reach $n(n+1)/2$, which exceeds a 32-bit signed integer at the maximum length; fixed-width implementations should use 64-bit counting.
