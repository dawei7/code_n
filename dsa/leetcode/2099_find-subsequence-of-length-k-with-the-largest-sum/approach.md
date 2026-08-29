## General

**Select positions, not just values**

The maximum sum comes from choosing the $k$ largest array values. However, a subsequence must preserve original order. Sorting values alone would lose the positions needed to restore that order.

The source sorts the index range `0..n-1` with key `nums[i]`:

`sorted(range(len(nums)), key=lambda i: nums[i])`.

The final `[-k:]` takes indices belonging to the $k$ largest values.

**Restore original order after choosing the elements**

The selected indices are sorted numerically. Increasing indices are exactly the order required for a subsequence.

The final comprehension returns `nums[i]` for those ordered positions. It does not sort the selected values, which could produce a sequence not obtainable from the original array.

For `nums = [-1, -2, 3, 4]` and `k = 3`, the chosen values are -1, 3, and 4 at indices 0, 2, and 3. Sorting those indices returns `[-1, 3, 4]`.

**Why ties are safe**

When several equal values compete at the selection boundary, choosing any required number of their indices gives the same sum. Python's sort is stable, but correctness does not rely on a unique tie choice because the problem accepts any maximum-sum subsequence.

After selection, sorting indices always creates a valid order.

**Why the chosen sum is maximum**

Suppose a size-$k$ selection omits a value larger than one it includes. Swapping the smaller selected value for the larger omitted value increases the sum. Therefore, no optimum can omit a strictly larger value in favor of a smaller one.

The last $k$ indices in value-sorted order satisfy exactly this property. They represent the $k$ largest values, with arbitrary harmless choices among equal values. Reordering their indices does not change which values were selected or their sum, so it preserves optimality while satisfying the subsequence constraint.

The method never mutates `nums`; it sorts a newly created range of indices.

**Trace selection separately from ordering**

For `nums = [3, 4, 3, 3]` and `k = 2`, sorting indices by their values puts the index of 4 at the high end and places the indices of 3 around it. Taking the final two indices selects value 4 and one value 3, which is the maximum possible sum 7.

Those selected indices may appear in value-sorted order rather than position order. Sorting the two indices afterward determines whether the returned valid answer is `[3, 4]` or `[4, 3]`. Both can be optimal if their chosen positions allow them, and the source returns the one corresponding to its selected positions.

For `nums = [2, 1, 3, 3]` and `k = 2`, both largest values are 3. Their original indices are 2 and 3. Reordering indices increasingly keeps them in the source sequence and returns `[3, 3]`.

**Why reordering selected indices does not change the objective**

The sum of selected values is independent of the order in which those selected positions are listed. Sorting indices does not replace any selected element; it merely presents them in the only order that makes them a subsequence.

This separation is the core design:

- value ordering decides which positions maximize the objective;
- index ordering decides how those positions must appear in the returned sequence.

Trying to satisfy both goals with one sort key can be misleading. Sorting solely by index never discovers the largest values, while sorting solely by value does not produce a subsequence.

**Why exactly $k$ positions are retained**

The slice `[-k:]` contains exactly $k$ indices because the constraints guarantee `1 <= k <= len(nums)`. It never needs padding and never returns too many values.

Even with ties, every index is a distinct selectable occurrence. Selecting one occurrence does not consume or collapse another equal-valued occurrence, so an index list is the right representation.

## Complexity detail

Let $n$ be the length of `nums`.

Sorting all $n$ indices by value costs $O(n\log n)$. Sorting the selected $k$ indices costs $O(k\log k)$, which is within $O(n\log n)$. Building the result costs $O(k)$.

The full sorted index list uses $O(n)$ space, and selected-index and result lists use $O(k)$. Auxiliary space is $O(n)$, with $O(k)$ required output.

## Alternatives and edge cases

- **Sort values directly:** This finds the maximum multiset but loses original indices and cannot reliably reconstruct a subsequence.
- **Heap of size `k`:** Tracking the top $k$ value-index pairs can reduce selection time to $O(n\log k)$, followed by index sorting.
- **Quickselect:** It can find a threshold in expected linear time, but ties at the boundary require careful index selection.
- **`k == 1`:** Any index containing a maximum value is valid.
- **`k == n`:** Every index is selected, and sorting indices returns the original array unchanged.
- **All values equal:** Any $k$ indices give the same sum; the chosen stable-sort suffix is valid.
- **Negative values:** The $k$ numerically largest values still maximize the sum, even if all are negative.
- **Duplicate boundary values:** Any subset of tied occurrences is acceptable as long as exactly $k$ total indices are selected.
- **Original order:** The second index sort is essential; value order is not subsequence order.
- **Input preservation:** Sorting indices leaves `nums` unchanged.
- **Required output length:** The final comprehension iterates over exactly the selected $k$ indices, so its result always has length $k$.
- **Stable sorting:** Python stability determines a consistent choice among equal values, but any tied choice has the same sum and is accepted.
