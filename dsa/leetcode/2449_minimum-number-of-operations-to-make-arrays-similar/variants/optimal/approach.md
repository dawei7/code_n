## General

Adding or subtracting 2 never changes a value's parity. Therefore, an even source value can only become an even target value, and an odd source value can only become an odd target value. The feasibility guarantee implies that the corresponding parity groups have equal sizes and that total increases can be balanced by total decreases.

Partition both arrays into even and odd groups, then sort each group. Within one parity, match the smallest source with the smallest target, the next-smallest with the next-smallest, and so on. This order-preserving matching minimizes total displacement: if $a\le b$ are matched to $y\le x$, replacing the crossed matches $(a,x),(b,y)$ with $(a,y),(b,x)$ cannot increase the sum of absolute differences. Repeatedly uncrossing establishes the sorted pairing.

For every aligned pair where the source exceeds its destination, the excess must be donated in units of 2. Add `(source - destination) // 2` to the answer. Deficits need not be counted separately: every operation simultaneously supplies one deficit and consumes one surplus, and equality of the total sums makes the two amounts equal.

The accumulated surplus units are attainable by pairing each required increase with one required decrease. They are also a lower bound because no operation can remove more than one unit of 2 from the surplus. Consequently, their sum is exactly the minimum number of operations.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Partitioning and scanning take $O(n)$ time. Sorting all parity groups takes $O(n\log n)$ time in total, which dominates the running time.

The four partitioned lists hold $O(n)$ values altogether, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Sort by `(parity, value)`:** A single decorated sort for each input also aligns corresponding parity groups in $O(n\log n)$ time.
- **Repeatedly select the next minimum:** Removing the smallest remaining value from each parity group produces the same matching but takes $O(n^2)$ time with ordinary arrays.
- **Count total absolute displacement:** After optimal alignment, summing absolute differences and dividing by 4 is equivalent because each operation changes two aligned displacements by 2.
- **Arrays already similar:** Their sorted parity groups match exactly, so the answer is zero even if their original orders differ.
- **Mixed parity:** Even and odd values must be matched independently; globally sorting without respecting parity can propose impossible conversions.
- **Duplicate values:** Equal occurrences remain distinct matching slots, but their sorted order does not affect the result.
- **Single element:** Feasibility forces the two singleton values to be equal, yielding zero operations.
- **Large transfer:** Differences can be close to $10^6$ across many indices, so the operation count should use wide integer arithmetic.
