## General

**For one window, an optimal common value is a median.** If all values in a length-$k$ window are changed to $t$, the number of unit operations is

$$
\sum_i\lvert x_i-t\rvert.
$$

This sum is minimized by any median. For odd $k$, the median is the single middle sorted value. For even $k$, every integer between the two middle values is optimal. The source consistently uses the upper median.

The challenge is to obtain each sliding window's median and absolute-deviation sum without sorting all $k$ elements again.

**Split the current multiset around the upper median.** The source maintains two `SortedList` instances:

- `l` holds the lower half;
- `r` holds the upper half, including the chosen median `r[0]`.

Their invariants after rebalancing are:

1. every value in `l` is at most every value in `r`;
2. `len(r)` equals `len(l)` or exceeds it by one.

Therefore, the smallest value in `r` is the upper median. `s1` is the sum of values in `l`, and `s2` is the sum in `r`.

**Insert one value while restoring order and size.** Every new value `x` is first added to `l` and to `s1`. The source immediately removes the largest value from `l` with `l.pop()` and inserts it into `r`. This transfer guarantees that any newly inserted large value cannot remain on the lower side and that the maximum lower value does not exceed the upper partition.

If `r` is now more than one element larger than `l`, its smallest value is moved back to `l`. After this step, the size difference is at most one and `r` is the larger side when the total size is odd.

The structure may temporarily contain fewer than $k$ elements while the first window is being built. The same invariants work for every prefix size.

**Calculate the exact cost from the median and the two sums.** Once `i >= k - 1`, the structure contains one complete length-$k$ window. Let

`median = r[0]`.

Every `r` value is at least the median, so its total cost to decrease to the median is

$$
\texttt{s2}-\textit{median}\cdot\lvert r\rvert.
$$

Every `l` value is at most the median, so its total cost to increase is

$$
\textit{median}\cdot\lvert l\rvert-\texttt{s1}.
$$

Adding these expressions gives the source's formula:

`s2 - r[0] * len(r) + r[0] * len(l) - s1`.

The minimum over all complete windows is stored in `ans`.

For `[-2,-2]`, the upper median is $-2$ and both deviation terms are zero, so the answer can become zero. For `[-3,2,1]`, the sorted values are $[-3,1,2]$, the median is $1$, and the cost is $4+0+1=5$.

**Remove the outgoing value after evaluating the window.** The outgoing index is `j = i - k + 1`. If its value occurs in `r`, the source removes one copy there and adjusts `s2`; otherwise, it removes one copy from `l` and adjusts `s1`.

With duplicate values at the partition boundary, an equal value may exist in both lists. Removing either indistinguishable copy preserves the combined multiset. Choosing `r` first is therefore safe.

The code does not rebalance immediately after removal. The next iteration's insertion procedure repairs the possible size difference: adding to `l`, moving its maximum to `r`, and, if needed, moving `r`'s minimum back. Before every cost calculation, the two invariants are restored.

**Why every window obtains its minimum.** The data structures contain exactly the previous window minus its outgoing occurrence plus the newly inserted occurrence. Sorted transfers preserve a valid lower/upper partition. The derived formula is the sum of distances to an actual median, and the median minimizes total absolute distance. Hence the calculated number is the fewest operations for that window. Taking the minimum across every length-$k$ window gives the least cost required to make at least one such subarray equal.

The manifest summary mentions balanced heaps with lazy deletion. The protected source uses two `SortedList` objects and eagerly removes outgoing values. There are no heaps, delayed-count map, or stale entries. The high-level median idea and asymptotic bounds agree, but the operational explanation must follow these ordered multisets.

## Complexity detail

Each element is inserted once and an outgoing occurrence is removed once after its window is evaluated. `SortedList` insertion, removal, membership search, and endpoint pop are treated as $O(\log k)$ ordered-multiset operations in the standard problem-level analysis. Constantly many occur per array element, so total time is $O(n\log k)$.

At most $k$ values are stored across `l` and `r` before a completed window is evaluated, and then one is removed. The two lists therefore use $O(k)$ space. Sums, indices, and the answer use $O(1)$ additional space, matching the manifest's $O(k)$ bound.

## Alternatives and edge cases

- **Sort every window:** Sorting $k$ values for each of $n-k+1$ windows costs $O(nk\log k)$ time and repeats nearly all work.
- **Two heaps with lazy deletion:** A max-heap and min-heap can maintain the median in $O(\log k)$ per slide, but arbitrary outgoing elements require delayed-deletion counts. That is not the data structure used here.
- **Fenwick tree over values:** Coordinate compression plus frequency and sum trees can find medians and costs in $O(\log U)$, where $U$ is the number of distinct values, but it adds indexing machinery.
- **Even \(k\):** The upper median `r[0]` is optimal even though the lower median would also minimize the cost. The formula remains exact.
- **Duplicate medians:** Removing an equal outgoing value from `r` even when another conceptual copy was in `l` is harmless because multiset copies have no identity.
- **Negative values:** Sorted order and absolute deviations work unchanged. The sum formula does not assume nonnegative elements.
- **Already equal window:** Both deviation terms are zero, and zero is the globally smallest possible answer.
- **Window equals the whole array:** The structure builds once, evaluates one median cost, removes the outgoing value afterward, and returns that single cost.
- **Balance after removal:** The source intentionally repairs balance during the next insertion. Reading `r[0]` between removal and the next insertion would be unsafe, but no cost is evaluated in that interval.
- **Input remains unchanged:** All operations affect ordered-list copies of values; `nums` itself is only read.
