## General

**Track the best eligible box seen so far**

Scan the array from left to right. Ignore any capacity below `itemSize`. For an
eligible box, replace the saved choice only when its capacity is strictly less
than the best eligible capacity already seen.

After processing index `i`, the saved pair is the required choice among indices
`0` through `i`: every smaller capacity replaces the old choice, while an equal
capacity does not replace it and therefore preserves the earlier index. This
property holds initially when no box has been chosen and is maintained by each
scan step. At the end, the saved index is the minimum-capacity eligible box with
the prescribed tie-breaking. If no update ever occurred, no box could store the
item and the initial index `-1` is returned.

## Complexity detail

Let $N$ be the number of boxes. The algorithm examines each capacity once, so
its time complexity is $O(N)$. It stores only the best capacity and its index,
using $O(1)$ auxiliary space.

The benchmark defines size as $N$. All capacities are eligible and strictly
decrease, forcing the accepted scan to read the whole array before identifying
the final index. The correct slower control proves each candidate's optimality
with a second scan, producing quadratic work on the same tiers.

## Alternatives and edge cases

- **Sort eligible capacity-index pairs:** Lexicographic sorting gives the right
  capacity and tie-break but costs $O(N\log N)$ time and extra storage.
- **Pairwise optimality checks:** Testing every eligible candidate against all
  boxes is correct but takes $O(N^2)$ time.
- **Return the first fitting box:** An earlier box may fit while a later box has
  a smaller eligible capacity.
- **Update on equal capacity:** Using a non-strict comparison would overwrite
  the earliest minimum with a later tied index.
- **Exact fit:** A capacity equal to `itemSize` is eligible and is the smallest
  possible capacity for that item.
- **No eligible box:** Keeping the index sentinel at `-1` directly represents
  this required result.
