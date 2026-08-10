## General

**Use the empty capacity from right to left**

The first `m` positions of `nums1` contain meaningful sorted values, while its final `n` positions are capacity for the result. Writing the merged sequence from left to right would risk overwriting a meaningful `nums1` value before it had been compared. Writing from the right solves that problem because the destination begins in unused capacity.

`i = m - 1` points to the largest unread meaningful value in `nums1`. `j = n - 1` points to the largest unread value in `nums2`. `k = m + n - 1` points to the final unfilled result position in `nums1`.

At each step, the larger of the two readable values must be the largest value not yet placed, so it belongs at `nums1[k]`.

**Compare only when `nums1` still has a candidate**

The condition `i >= 0 and nums1[i] > nums2[j]` first checks that an unread first-array value exists. Short-circuit evaluation prevents `nums1[-1]` from being treated as a legitimate candidate after the meaningful prefix is exhausted.

If that condition is true, `nums1[i]` is strictly larger and is copied to `nums1[k]`; `i` then moves left. Otherwise, `nums2[j]` is selected and `j` moves left. The otherwise case covers both a smaller-or-equal second-array value and exhaustion of the first array.

On equal values, the source chooses from `nums2`. The contract requires sorted values but does not attach identities that require stable ordering between the two input arrays, so either equal copy could be placed first from the right.

After either choice, `k` decreases because exactly one final position has been filled.

**Why overwriting `nums1[k]` is safe**

Initially `k - i = n`, so the write pointer is separated from the unread first-array pointer by the entire extra capacity. Every iteration decrements `k` and decrements either `i` or `j`.

When `i` decreases, the gap between `k` and `i` stays unchanged. When `j` decreases, the gap shrinks, but this can happen only `n` times because `nums2` has `n` values. The write pointer cannot move ahead of an unread `nums1` value while any second-array value still needs placement.

Another way to see it is by counting: before writing a position, there are exactly `k + 1` total unread values across both arrays. There is enough space through index `k` for all of them, and the largest belongs at the boundary. A meaningful first-array cell is overwritten only after its original value has already been moved or when the same position is its final position.

**Why the loop condition mentions only `j`**

The loop runs while `j >= 0`, meaning some `nums2` value is still unmerged. If `i` becomes negative first, the condition inside always falls to the else branch and copies all remaining `nums2` values into the leading positions.

If `j` becomes negative, every second-array value has been placed. Any unread `nums1[0:i + 1]` values are already in the correct leading positions. Moving them onto themselves would change nothing, so the method stops immediately. This removes the need for a second cleanup loop for `nums1`.

**Trace the standard example**

For `nums1 = [1,2,3,0,0,0]` and `nums2 = [2,5,6]`, the first comparisons place 6 and 5 into the last two slots. Then 3 is larger than the remaining 2 and moves to index three. The equal-or-smaller choice places the second-array 2 at index two.

At that point `j` is negative. The original values 1 and 2 remain at indices zero and one, already preceding the placed suffix. The final array is `[1,2,2,3,5,6]`.

**A suffix invariant**

Before each iteration, `nums1[k + 1:]` contains the largest already placed values from both inputs in correct non-decreasing order, and the unread values are `nums1[:i + 1]` plus `nums2[:j + 1]`.

The largest unread value is at one of the two readable ends because both unread prefixes are sorted. Placing their maximum at `k` extends the correct suffix one position left and removes exactly that value from the unread set. The invariant is preserved.

When `j < 0`, the second unread prefix is empty and the first unread prefix is already sorted in the only remaining positions. Together with the finalized suffix, all `m + n` positions are correct.

**Mutation and return behavior**

Assignments are made directly into `nums1`. The method has no explicit return statement, so it returns `None`, as required. The placeholder zeroes have no value meaning and are never compared as part of the first sorted input because `i` begins at `m - 1`.

## Complexity detail

Each iteration places one value from `nums2` or moves one meaningful value from `nums1`. No value is processed more than once, so time is $O(m+n)$ in the worst case, matching the manifest. It may stop earlier when `nums2` is exhausted, but the upper bound remains linear in both inputs.

Only three indices are stored. The merge uses the supplied trailing capacity and allocates no copy, so auxiliary space is $O(1)$, also matching the manifest.

## Alternatives and edge cases

- **Forward merge with a copy:** Copy the first `m` values, then merge from the beginning. It is linear time but uses $O(m)$ extra space.
- **Append and sort:** Copy `nums2` into the placeholders and sort all values. It ignores existing order and costs $O((m+n)\log(m+n))$ time.
- **Repeated insertion:** Insert second-array values into the meaningful prefix. Array shifting can make this quadratic.
- **`n == 0`:** `j` starts negative, the loop is skipped, and `nums1` remains unchanged.
- **`m == 0`:** `i` starts negative, so every iteration copies from `nums2` into `nums1`.
- **All first-array values larger:** They move to the far-right positions before second-array values fill the front.
- **All second-array values larger:** They fill the trailing capacity, and the first prefix remains in place.
- **Equal values:** The source chooses `nums2` on ties, which preserves sortedness.
- **Placeholder zeroes:** They are capacity only and may not be treated as meaningful values when `m` is smaller than the physical length.
- **Negative input values:** Backward maximum comparison works regardless of sign.
- **No return value:** Correctness is observed through the mutated `nums1` list.
- **Input preservation:** `nums2` is read only; `nums1` is intentionally overwritten.
