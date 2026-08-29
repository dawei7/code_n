## General

**Count missing values without listing them**

The requested sequence begins strictly after `nums[0]`. Missing values can occur inside gaps between stored numbers, and if `k` is large enough, the sequence continues beyond the last array value.

Generating missing integers one by one is too slow because `k` can be as large as `10^8`. The sorted, unique array lets us count how many values are missing up to any index in constant time. That count is monotonic, so binary search can locate the gap containing the answer.

**Derive the cumulative missing-count formula**

The helper is:

```python
def missing(i: int) -> int:
    return nums[i] - nums[0] - i
```

Consider the inclusive integer interval from `nums[0]` through `nums[i]`. If no values were missing, moving from the first value to the value at index `i` would take `nums[i] - nums[0]` unit steps.

The array has already supplied exactly `i` of those steps through the `i` stored transitions after index zero. Every additional unit step represents an absent integer. Therefore:

```text
missing(i) = nums[i] - nums[0] - i
```

The same result follows by counting interval elements. The inclusive interval contains `nums[i] - nums[0] + 1` integers, while the array contains `i + 1` values in that interval. Subtracting gives `nums[i] - nums[0] - i`.

For `nums = [4, 7, 9, 10]`:

- `missing(0) = 4 - 4 - 0 = 0`.
- `missing(1) = 7 - 4 - 1 = 2`, representing five and six.
- `missing(2) = 9 - 4 - 2 = 3`, adding eight.
- `missing(3) = 10 - 4 - 3 = 3`.

Because `nums` is strictly increasing, this cumulative count never decreases. Advancing one array index adds the size of the next gap, which is always non-negative. That monotonicity is the property binary search needs.

**Handle an answer beyond the final stored value**

Before searching, the code checks:

```python
n = len(nums)
if k > missing(n - 1):
    return nums[n - 1] + k - missing(n - 1)
```

`missing(n - 1)` is the total number of missing values strictly after `nums[0]` and no later than the last stored value.

If `k` exceeds that count, all internal missing values come before the answer. After consuming them, `k - missing(n - 1)` missing positions remain. Beyond the final array value, every successive integer is missing, so adding that remainder to `nums[n - 1]` gives the answer directly.

For `nums = [1, 2, 4]`, the cumulative missing count at four is one, representing three. If `k = 3`, two more missing positions remain beyond four, so the result is six.

The comparison is strictly greater. If `k` equals the final cumulative count, the requested value is an internal missing number no later than `nums[n - 1]`, so binary search should locate its containing gap.

This preliminary case also handles a one-element array. `missing(0)` is zero, and every positive `k` is beyond the last element, so the answer is `nums[0] + k`.

**Binary-search the first prefix containing at least k missing values**

When the answer lies inside the covered range, the code initializes:

```python
l, r = 0, n - 1
```

It seeks the smallest index `l` such that `missing(l) >= k`. At that index, the cumulative count has reached or passed the requested rank. The previous index still has fewer than `k` missing values, so the answer lies in the open gap between those two stored values.

The loop is a lower-bound search:

```python
while l < r:
    mid = (l + r) >> 1
    if missing(mid) >= k:
        r = mid
    else:
        l = mid + 1
```

The right shift by one performs integer division by two for non-negative indices, so `mid` is the floor of their average.

If `missing(mid) >= k`, index `mid` may be the first sufficient index, but an earlier one may also be sufficient. The search keeps `mid` by setting `r = mid`.

If `missing(mid) < k`, neither `mid` nor any earlier index can be sufficient because the count is non-decreasing. The search discards them with `l = mid + 1`.

Every iteration preserves the first sufficient index inside the closed search interval. The interval shrinks until `l == r`, at which point `l` is exactly that first index.

Since `missing(0)` is zero and `k >= 1`, `l` cannot be zero in this branch. Accessing `l - 1` is therefore safe.

**Move the remaining number of missing steps into the identified gap**

At the end of binary search:

- `missing(l - 1) < k`.
- `missing(l) >= k`.

Thus the requested value is after `nums[l - 1]` but before `nums[l]`. The number of missing values already counted through `nums[l - 1]` is `missing(l - 1)`. The desired value is the next:

```text
k - missing(l - 1)
```

missing positions after `nums[l - 1]`. The exact return is:

```python
return nums[l - 1] + k - missing(l - 1)
```

For `nums = [4, 7, 9, 10]` and `k = 3`, binary search finds `l = 2` because the cumulative count is two at index one and three at index two. One more missing position is required after seven, so the answer is eight.

**Why the algorithm is correct**

The helper exactly counts missing integers through any stored index, and those counts are monotonic. The preliminary branch correctly handles ranks larger than the complete internal count by continuing consecutively after the last value.

Otherwise, lower-bound binary search finds the first stored index whose prefix contains at least `k` missing values. The previous prefix contains fewer, so the answer must lie in that one gap. Adding the remaining rank to the previous stored value selects precisely the `k`th missing integer. These cases cover every valid input and are disjoint.

## Complexity detail

Let `N` be the length of `nums`.

Each `missing` call performs a constant number of array reads and arithmetic operations. The binary-search interval is halved on every iteration, so it performs `O(log N)` iterations. The preliminary boundary check and final arithmetic take constant time. Total time is `O(log N)`.

The helper, indices, and local numeric variables use a constant amount of storage. No list, recursion stack, or generated missing sequence is created, so auxiliary space is `O(1)`.

These are the exact bounds stated in the manifest.

## Alternatives and edge cases

- **Linear gap scan:** Visit adjacent array pairs, subtract each gap size from `k`, and stop in the containing gap. This takes `O(N)` time and `O(1)` space and is simpler, but it does not meet the logarithmic follow-up.
- **Enumerate every integer:** Testing consecutive values after `nums[0]` can require work proportional to `k` or the numeric range, which is far too large.
- **Equivalent answer formula:** After finding the first sufficient index `l`, algebra can express the answer as `nums[0] + k + l - 1`. The exact code's previous-gap formula makes the remaining-rank reasoning more explicit.
- **One array element:** There are no internal gaps. The boundary branch returns `nums[0] + k`.
- **Consecutive array:** Every cumulative missing count is zero, so every positive `k` lies beyond the last value.
- **Answer is the first missing value:** Binary search finds the first index after the first nonempty gap, and the remaining offset is one.
- **Answer is the last value inside a gap:** Equality `missing(l) == k` is handled by the internal branch, and the formula lands immediately before `nums[l]`.
- **Answer beyond the array:** The remaining rank is added to the last stored value because all later integers are missing.
- **Very large k:** The algorithm performs arithmetic on `k` rather than iterating `k` times, so its running time is unaffected by the rank's magnitude.
- **Unique ascending values:** The formula relies on strict increase. Duplicates or unsorted input would destroy the cumulative-count interpretation, but the contract excludes them.
- **Starting boundary:** Missing values smaller than or equal to `nums[0]` are not counted. `missing(0) = 0` encodes that rule.
- **Input preservation:** The array is read only and remains in its original sorted order.
