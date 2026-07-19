## General
**Compute the total once**

Let `total` be the sum of the complete array. During a left-to-right scan,
maintain `left_sum`, the sum of values strictly before the current index. At a
candidate containing `value`, the right-side sum is then
`total - left_sum - value`.

**Test before adding the current value**

Compare `left_sum` with that derived right sum. If they are equal, immediately
return the current index. Testing before updating is essential because the
candidate value must not belong to either side.

Only after a failed comparison, add `value` to `left_sum` so it becomes part of
the left side for the next index.

**Why the first match is the required answer**

The maintained prefix is exact by induction: it begins as the empty sum `0`
and gains precisely each index after that index has been tested. The total-sum
identity therefore computes the exact complementary suffix at every position.
Scanning in increasing index order makes the first equality the leftmost valid
middle index. If none matches, returning `-1` is correct.

## Complexity detail
Computing `total` takes one pass and checking candidates takes another, for
$O(N)$ total time. The total, running left sum, index, and current value use
$O(1)$ additional space.

## Alternatives and edge cases
- **Prefix and suffix arrays:** Precompute both side sums for every index. This
  is correct and linear-time but uses $O(N)$ extra space unnecessarily.
- **Resum each side at every index:** Directly compute
  `sum(nums[:i])` and `sum(nums[i + 1:])` for each candidate. This is simple
  but takes $O(N^2)$ time.
- A one-element array always returns index `0` because both sides are empty.
- Index `0` qualifies when the suffix after it sums to zero; index `N - 1`
  qualifies when the preceding prefix sums to zero.
- Negative values can make running sums decrease, so monotonic-search reasoning
  does not apply.
- If several indices qualify, such as in an all-zero array, only the smallest
  index is returned.
- The current element is excluded from both compared sums.
