## General

**Turn the index constraint into an activation boundary**

Because the pair is symmetric, consider the later index `right`. Its earlier partner may be any index from `0` through `right - x`. While sweeping `right` from left to right, insert `nums[right - x]` into an ordered multiset just before answering the query for `nums[right]`. The multiset then contains exactly the values whose indices are far enough to the left.

**Only the immediate value neighbors can be optimal**

For a current value `v`, any eligible stored value below `v` is no closer than the greatest stored predecessor, and any stored value at least `v` is no closer than the least stored successor. It is therefore sufficient to inspect those two ordered neighbors rather than every active value.

Coordinate-compress all distinct array values into sorted ranks. A Fenwick tree stores how many active values occupy each rank. A prefix count gives the number of active values below `v`. Fenwick binary lifting then finds the rank of the last such value and the first active value at or above `v` by their multiset orders.

At each iteration, every queried rank came from an index at distance at least `x`, so all candidates are legal. Conversely, orient any legal pair so its later endpoint is `right`; its earlier value has already been activated at that iteration. One of the predecessor or successor inspected for `right` is at least as close as that earlier value. Taking the minimum across the sweep therefore yields the global optimum.

When `x = 0`, the current value is activated before its own query. The successor lookup finds the same value immediately and produces the required answer zero.

## Complexity detail

Let $n$ be the array length. Sorting the distinct values costs $O(n\log n)$. Each of the $n$ sweep iterations performs a constant number of binary searches, Fenwick updates, prefix queries, and order-statistic searches, each in $O(\log n)$ time. Total time is $O(n\log n)$, and the compressed values plus Fenwick tree use $O(n)$ space.

## Alternatives and edge cases

- **Balanced ordered multiset:** A tree set or sorted multiset directly supports insertion, predecessor, and successor in $O(\log n)$ time, but Python's standard library has no such container.
- **Check every legal pair:** Direct enumeration is simple and correct but takes $O(n^2)$ time when `x` is small.
- **Maintain a sorted Python list:** Binary search finds neighbors quickly, but inserting into the middle shifts $O(n)$ elements and makes the full sweep quadratic.
- `x = 0` permits choosing the same index twice, so the answer is always `0`, including for a one-element array.
- Duplicate active values must retain multiplicity in the Fenwick counts; encountering the same value yields difference zero.
- A predecessor, a successor, or both may be absent near the minimum and maximum value ranks.
- The value range reaches $10^9$, so a Fenwick tree over raw values would be wasteful; coordinate compression is essential.
