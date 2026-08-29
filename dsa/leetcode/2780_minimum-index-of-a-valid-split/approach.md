## General

**Only the whole-array dominant value can dominate both halves**

Suppose a valid split has left length `L` and right length `R`, and value `x` is dominant in both. It occurs more than `L / 2` times on the left and more than `R / 2` times on the right. Adding those counts shows it occurs more than

$$
\frac{L+R}{2} = \frac{n}{2}
$$

times overall. Therefore `x` must be the unique dominant element already guaranteed for `nums`.

This reduces the task from tracking every value on both sides to tracking one value and its counts.

**Find that value and its total frequency**

The exact solution constructs `Counter(nums)` and calls `most_common(1)[0]`. This returns a pair:

- `x`, the most frequent value;
- `cnt`, its total number of occurrences.

Because the contract guarantees exactly one dominant value, the most frequent key is unambiguous and is the only candidate that can satisfy a valid split.

This differs from the manifest description, which names Boyer–Moore voting and constant auxiliary space. The exact source uses a full frequency table.

**Scan split boundaries from left to right**

`enumerate(nums, 1)` gives `i` as the current prefix length rather than a zero-based index. After consuming that element:

- the left side has length `i`;
- the right side has length `len(nums) - i`;
- `cur` is the number of `x` values in the left side;
- `cnt - cur` is the number in the right side.

The strict dominance tests are:

`cur * 2 > i`

and

`(cnt - cur) * 2 > len(nums) - i`.

Multiplying by two keeps the comparison integral and exactly expresses “more than half.” Equality is not enough.

When both hold, the split after a prefix of length `i` has zero-based split index `i - 1`, which the code returns. Because boundaries are scanned in increasing order, the first returned index is the minimum.

**Why the condition appears only after encountering `x`**

The exact code places the dominance check inside `if v == x`. It does not test a boundary whose newest prefix element is not dominant.

One way to understand why this does not lose the minimum is through majority surplus. Define the left surplus after a prefix of length `i` as

$$
A = 2\cdot\text{cur} - i,
$$

and the right surplus as

$$
B = 2(\text{cnt}-\text{cur}) - (n-i).
$$

A split is valid exactly when both `A > 0` and `B > 0`. Their sum is constant:

$$
A+B = 2\cdot\text{cnt}-n > 0.
$$

Passing an `x` increases `A` by one and decreases `B` by one. Passing a non-`x` decreases `A` by one and increases `B` by one. If the path of `A` first entered the valid interval `0 < A < A+B` on a downward non-`x` step, it would have been at the upper boundary `A+B` immediately before. To reach that upper boundary from the initial surplus, it must previously have crossed the interior on an upward `x` step, yielding an earlier valid split. Therefore the earliest valid boundary can be found immediately after an occurrence of `x`.

The guarded check is thus consistent with searching for the minimum, although checking every boundary would also be linear and easier to recognize.

**The final array position cannot become an invalid empty-side answer**

The loop includes `i = n`, which would place an empty suffix after the last element. However, the right dominance condition becomes

`0 > 0`,

which is false. The code cannot return `n - 1`, so it respects the required `i < n - 1` split range without a separate loop bound.

**A walkthrough**

For `nums = [1, 2, 2, 2]`, the counter chooses `x = 2` with `cnt = 3`.

- Prefix length one contains zero copies, so no check succeeds.
- At prefix length two, `cur = 1`. The left has one 2 out of two, which is not more than half.
- At prefix length three, `cur = 2`. The left test is `4 > 3` and the right test is `2 > 1`, so both halves are dominated by 2.

The method returns `3 - 1 = 2`.

**Why the result is correct**

The initial argument proves no value other than `x` can dominate both halves. At each examined boundary, `cur` and `cnt - cur` are exact counts of `x` on the two sides, and the doubled inequalities are exactly the definition of dominance. Any returned split is therefore valid.

The scan proceeds in boundary order, and the surplus argument shows the earliest valid split is among the boundaries checked after `x`. Hence the first return is the minimum valid index. If none passes, no valid split exists and `-1` is correct.

## Complexity detail

Let `n` be the array length and `u` the number of distinct values. Building the Counter takes `O(n)` expected time and stores `u` entries. Finding its most common entry costs `O(u)` for one requested item. The boundary scan is another `O(n)` pass. Total expected time is `O(n)`.

The Counter uses `O(u)` auxiliary space, which is `O(n)` in the worst case. All scan variables are constant-sized. This contradicts the manifest's `O(1)` space and Boyer–Moore summary; those describe the editorial optimization, not the exact solution.

## Alternatives and edge cases

- **Boyer–Moore majority vote:** It identifies the guaranteed dominant value in `O(n)` time and `O(1)` space, followed by a count and split scan. This matches the manifest but is not the exact code.
- **Two frequency maps:** Moving values from a suffix map to a prefix map works but tracks far more information than the single dominant candidate needs.
- **Check every boundary:** It is still `O(n)` and avoids the surplus proof for guarded checking. The exact code tests only after occurrences of `x`.
- **Strict majority:** Counts exactly equal to half fail because both comparisons use `>` rather than `>=`.
- **One-element array:** No nonempty two-way split exists. The final empty-suffix test fails and the method returns `-1`.
- **Dominant value at the first position:** Index zero is returned only if the remaining suffix also keeps that value dominant.
- **Valid split near the end:** The suffix may contain one dominant value, which is automatically a strict majority of a one-element side.
- **Empty suffix after the final element:** Its `0 > 0` test is false, preventing an out-of-range split.
- **Large element values:** Counter keys handle them directly; no value-indexed array is allocated.
- **Unique dominant guarantee:** The code does not need to verify the Counter winner exceeds half, because the contract proves it.
- **No valid split:** The total array can have a dominant element while every proper boundary fails on at least one side, producing `-1`.
- **Manifest mismatch:** Actual storage is linear in distinct values, not constant, because `Counter(nums)` is part of the exact source.
