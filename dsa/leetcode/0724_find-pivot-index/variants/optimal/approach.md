## General
**Express the right sum from the total**

Compute the sum of the entire array once. Before processing an index `i`, keep `left_sum` equal to the sum of `nums[0:i]`. The elements strictly to the right then sum to `total - left_sum - nums[i]`; subtracting the current value matters because a pivot belongs to neither side.

**Check before extending the left side**

Compare `left_sum` with the derived right sum, then add `nums[i]` to `left_sum` for the next iteration. At the first index, the maintained left sum is zero, correctly representing an empty left side. After the comparison at the last index, the derived right sum is zero, correctly representing an empty right side.

**Why the first match is the required answer**

The scan visits indices from left to right, and the maintained and derived sums exactly represent the two sides of each visited index. Therefore every returned index satisfies the pivot condition. Returning immediately on the first equality makes it the leftmost valid pivot; reaching the end proves that no pivot exists.

## Complexity detail
The initial total and the left-to-right scan each process `n` values, so the time complexity is $O(n)$. The algorithm stores only the total, the running left sum, and loop state, for $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Prefix-sum array:** precompute a sum for every prefix and query both sides in constant time per index; it remains $O(n)$ time but uses $O(n)$ extra space unnecessarily.
- **Re-sum both sides at every index:** directly compute `sum(nums[:i])` and `sum(nums[i + 1:])`; it is straightforward but takes $O(n^2)$ time in the worst case.
- **Single element:** both sides are empty, so index `0` is the pivot.
- **Negative values:** totals and running sums remain valid without any monotonicity assumption.
- **Multiple pivots:** the left-to-right scan must return the smallest one.
- **No pivot:** return `-1` only after every index has been checked.
