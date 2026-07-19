## General
**Selecting values without losing identity**

The maximum possible sum comes from choosing the `k` largest values. Values alone are not enough to reconstruct a subsequence when duplicates occur, so associate every value with its original index.

Sort the indices by their corresponding values in descending order and retain the first `k`. This chooses `k` actual array positions whose values have the maximum total. Stable tie handling may favor earlier equal values, but any choice among equal boundary values has the same sum.

**Restoring subsequence order**

The value-ranking order generally differs from the original array order. Sort the selected indices numerically, then read `nums` at those positions. Increasing indices ensure that the returned values occur in precisely the same relative order as in the input.

**Why the sum is optimal**

Suppose another size-$k$ selection had a larger sum. It would have to include some unselected value greater than a selected value; otherwise its `k` values could not exceed the chosen top `k`. But the descending ranking would have selected that greater value first, which is a contradiction.

Reordering the selected indices does not change which values were chosen or their sum. It only converts the maximum-sum selection into the required subsequence representation.

## Complexity detail
Sorting all $n$ indices by value takes $O(n \log n)$ time. Sorting the $k$ chosen indices takes $O(k \log k)$ time, which is bounded by $O(n \log n)$. The index lists and returned subsequence use $O(n)$ space in the worst case.

## Alternatives and edge cases
- **Minimum heap of selected indices:** Keep the best `k` value-index pairs in $O(n \log k)$ time, then sort their indices. This is useful when $k$ is much smaller than $n$.
- **Sort value-index pairs:** Sorting `(value, index)` records is equivalent to sorting indices by their referenced values and has the same complexity.
- **Repeated maximum extraction:** Selecting one current maximum at a time is correct, but repeated linear searches require $O(nk)$ time and become quadratic when $k$ grows with $n$.
- When `k = n`, every value must be returned in its original order.
- Negative values are still ranked normally; the least negative values maximize the sum.
- Equal values at the selection boundary may lead to several different valid subsequences.
- Returning the chosen values in descending value order is invalid unless that order also follows their original indices.
