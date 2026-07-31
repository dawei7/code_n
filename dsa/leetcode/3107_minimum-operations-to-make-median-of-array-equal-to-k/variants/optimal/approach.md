## General

**Sorting exposes the chosen median.** Let $n$ be the length of `nums`, sort the values in non-decreasing order, and set $m=\lfloor n/2\rfloor$. The problem's median is exactly the value at index $m$, including for even $n$, when this index selects the larger of the two middle values.

**Only values crossing `k` can force work.** For the final median to be `k`, all positions before $m$ may be at most `k`, position $m$ must be `k`, and all positions after $m$ may be at least `k`. Therefore, any value at an index from $0$ through $m$ that is greater than `k` must be decreased by at least its gap to `k`. Symmetrically, any value from $m$ through $n-1$ that is less than `k` must be increased by at least its gap to `k`.

Pay exactly those gaps and leave every other value unchanged. Afterward, at least $m+1$ values are at most `k`, at least $n-m$ values are at least `k`, and the value occupying index $m$ is `k`. Thus the target is a valid median. Each charged gap was individually unavoidable, while no uncharged change is needed, so their sum is the minimum possible number of operations.

The middle position appears in both scans, but it contributes to at most one: its value cannot be both greater than and less than `k`.

## Complexity detail

Let $n$ be the length of `nums` as defined in the function contract. Sorting takes $O(n \log n)$ time, and the two scans together take $O(n)$ time. The app-local implementation creates a sorted copy, which uses $O(n)$ auxiliary space. The native submission sorts its input list in place; Python's sorting implementation may still use up to $O(n)$ temporary space.

## Alternatives and edge cases

- **Quickselect plus partitioning:** Find the element at index $m$ in expected $O(n)$ time, then scan the appropriate sides. This can improve expected time, but its implementation and worst-case guarantees are more involved than sorting.
- **Repeated unit operations:** Incrementing or decrementing one unit at a time simulates the statement directly but can take up to $O(n \cdot 10^9)$ steps; summing each required gap computes the same cost immediately.
- **Change only the current median:** Moving the value at index $m$ alone is insufficient when other values cross `k`; those values can displace the target from the median position after reordering.
- **Even length:** The required median is the value at sorted index $n/2$, not the average of the two middle values and not the smaller middle value.
- **Duplicates:** Several elements may already equal `k`; they contribute zero and naturally satisfy either side of the sorted partition.
- **Large answer:** Individual values and `k` can differ by nearly $10^9$, and many elements can contribute, so the total can exceed a 32-bit signed integer.
