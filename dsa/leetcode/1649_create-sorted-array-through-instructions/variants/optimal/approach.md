## General
**Store frequencies by value.** The physical positions of the growing sorted array are unnecessary. For a value $x$, the insertion cost depends only on the number of previously processed values in the ranges $[1,x-1]$ and $[x+1,M]$. A Fenwick tree stores the frequency at each value and returns any prefix frequency in logarithmic time.

**Translate strict comparisons into prefix queries.** Before processing the instruction at zero-based position `inserted`, exactly `inserted` values are present. Querying the prefix through `value - 1` gives the strictly smaller count. Querying through `value` includes all earlier duplicates, so subtracting that prefix from `inserted` gives the strictly greater count:

$$
L = \operatorname{prefix}(x-1),
\qquad
G = i-\operatorname{prefix}(x).
$$

Add $\min(L,G)$ to the running answer, then increment the frequency at $x$. Performing the update after both queries is essential: the current instruction must not count itself.

**Why the accumulated costs are exact.** After each update, the Fenwick tree contains precisely the frequency multiset of the processed prefix. Its prefix sums therefore partition every earlier value into strictly smaller, equal, or strictly greater groups for the next instruction. The two formulas recover exactly the counts named by the contract, and taking their minimum yields that insertion's required cost. Summing these independently correct costs produces the requested total.

## Complexity detail
Each of the $n$ instructions performs two Fenwick prefix queries and one point update, each in $O(\log M)$ time, for $O(n\log M)$ total time. The frequency tree has $M+1$ entries and uses $O(M)$ auxiliary space.

## Alternatives and edge cases
- **Sorted list with binary search:** Binary search finds the two strict insertion boundaries in $O(\log n)$ time, but inserting into the middle of an array-backed list shifts $O(n)$ elements, making the full process $O(n^2)$.
- **Segment tree:** Point updates and range-sum queries give the same $O(n\log M)$ time and $O(M)$ space, with a larger implementation and constant-factor footprint.
- **Coordinate-compressed Fenwick tree:** Compressing the distinct instruction values first changes the space bound to $O(k)$ for $k$ distinct values while preserving $O(n\log k)$ time. The fixed legal value bound makes direct indexing simpler here.
- **Balanced order-statistic tree:** Storing subtree sizes supports rank queries and duplicate counts in $O(\log n)$ expected or worst-case time, depending on the tree, but requires a more complex data structure.
- A single instruction has cost zero because the container is initially empty.
- Strict comparisons mean earlier duplicates of the current value belong to neither side.
- An increasing or decreasing instruction sequence costs zero at every step because one strict side is always empty.
- Fenwick indices must remain one-based; the legal minimum value 1 maps directly to the first tree index.
- The total may exceed the modulus even though every individual count fits in the input length, so reduce the final sum modulo $1{,}000{,}000{,}007$.
