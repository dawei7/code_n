## General
**Separate values by parity.** Start with the beautiful array `[1]`. From a beautiful permutation of $1$ through $m$, transform every value $x$ into the odd value $2x-1$ and, separately, into the even value $2x$. Keep only transformed values at most $n$, then concatenate all odd results before all even results. The two groups together are exactly the integers from $1$ through $\min(2m,n)$, each appearing once.

**Why each transformed group remains beautiful.** An affine transformation preserves the midpoint relation: if three transformed odd values, or three transformed even values, satisfied $2a_k=a_i+a_j$, their original values would satisfy the same relation. That would contradict the beauty of the array from the preceding round. Filtering only values greater than $n$ cannot create a forbidden triple among the values that remain.

**Why no triple crosses the parity boundary.** Any pair with one odd endpoint and one even endpoint has an odd sum, whereas $2a_k$ is even. Such endpoints can therefore never have an integer midpoint value. Because all odd positions precede all even positions, every possible forbidden triple is either wholly inside one transformed group or has endpoints of opposite parity; both cases have been ruled out.

Repeat the transformation until the array contains $n$ values. The permutation argument establishes the required range, and the two parity arguments establish the forbidden-midpoint condition, so the returned array is valid.

## Complexity detail
Before the last round, the constructed length doubles each time. The total number of values read and written across this geometric sequence is $O(n)$, so the construction takes $O(n)$ time. The current and next arrays together contain $O(n)$ values, giving $O(n)$ space including the returned permutation.

## Alternatives and edge cases
- **Recursive odd/even construction:** Recursively build the odd and even subproblem sizes and map their results into the two parity groups. It mirrors the proof directly, but without memoization it repeats work across recursion levels and takes $O(n\log n)$ time.
- **Random permutation search:** Shuffle and test candidates until one is beautiful. It provides no useful worst-case guarantee, and checking all index triples naively is expensive.
- **Ascending permutation:** Returning `[1,2,...,n]` fails once $n \ge 3$ because consecutive values can place their arithmetic mean between them.
- **Single value:** For `n = 1`, `[1]` is already a valid permutation and no index triple exists.
- **Alternative valid outputs:** The judge must check the permutation and midpoint properties rather than compare against one fixed example.
