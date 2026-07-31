## General

**Treat bit positions independently.** Whether one result bit qualifies does
not affect any other bit. Because every input is less than $2^{31}$, only
positions 0 through 30 can be set. For each position, scan the array and count
the values whose binary representation contains that bit.

**Apply the threshold definition directly.** When the count for a position is
at least `k`, combine its one-bit mask into the answer with bitwise OR.
Otherwise leave that result position unset. Each scan counts array elements,
not distinct numeric values, so duplicates correctly contribute once per
occurrence. After all 31 positions are considered, every result bit agrees
with the K-or definition; therefore the assembled integer is exactly the
required answer.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The algorithm scans $n$ values for each
of the fixed 31 legal bit positions, taking $O(31n)=O(n)$ time. It keeps only
the answer, a mask, and a counter, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Count all positions in one pass:** An array of 31 counters can be updated from each number and also takes $O(n)$ time, but uses $O(31)$ explicit storage instead of one counter.
- **Repeated full-prefix rescans:** Recomputing counts for every growing prefix eventually obtains the final frequencies but wastes $O(n^2)$ work.
- **Threshold one:** Every bit appearing in any element qualifies, so the K-or equals the ordinary bitwise OR.
- **Threshold equal to array length:** Only bits shared by every element qualify, matching the ordinary bitwise AND.
- **Zero values:** Zero contributes to no bit count but still counts as an array element when `k` is bounded by the array length.
- **Duplicate values:** Equal entries are separate numbers and each contributes independently toward the threshold.
- **Highest legal position:** Values may set bit 30; scanning only 30 positions would incorrectly omit it, while bit 31 can never be set.

