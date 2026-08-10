## General

**Sort first so every later decision has direction**

The competitive implementation uses the classic $O(n^3)$ reduction: choose the first two elements of a quadruplet with nested loops, then solve the remaining sorted 2Sum problem with two pointers. It begins with `nums.sort()`, making larger indices hold values that are never smaller. That monotonic order supports both safe pointer movement and inexpensive duplicate removal.

Sorting also means every reported quadruplet is already in non-decreasing value order. The function mutates `nums`, but the contract asks only for the answer and does not require the input order to survive.

**The loop bounds reserve four distinct indices**

For each candidate, the indices obey

$$
i < j < left < right.
$$

The first loop uses `range(len(nums) - 3)`, leaving room for three more elements. The second begins at `i + 1` and stops before the final two positions. `left` begins at `j + 1`, while `right` begins at the final index. This construction makes index reuse impossible by design, even when several selected values are equal.

If the array has fewer than four items, one or both ranges are empty, and the function naturally returns `[]`. Unlike the optimal variant, this source does not need a separate early guard.

**Convert the remaining question into a residual target**

After choosing `nums[i]` and `nums[j]`, the source calculates

```python
total = target - nums[i] - nums[j]
```

Here `total` is not the sum accumulated so far; it is the exact sum that `nums[left] + nums[right]` must reach. This residual form avoids repeatedly adding all four values inside the pointer loop. It is algebraically equivalent because

$$
\texttt{nums[left]}+\texttt{nums[right]}=\texttt{target}-\texttt{nums[i]}-\texttt{nums[j]}
$$

if and only if the four chosen values sum to `target`.

**Move the only endpoint that can repair the comparison**

The pointer loop compares `nums[left] + nums[right]` with `total`.

- On equality, it records `[nums[i], nums[j], nums[left], nums[right]]`, then moves both endpoints inward.
- If the pair sum is greater than `total`, it decrements `right`. Keeping the same `right` while increasing `left` could only preserve or increase an already excessive sum.
- Otherwise the pair sum is less than `total`, so it increments `left`. Keeping the same `left` while decreasing `right` could only preserve or decrease an already insufficient sum.

This is more than a heuristic. When the current sum is too small, `right` already supplies the largest available partner. Therefore the current `left` cannot reach the residual target with any allowed partner and may be discarded safely. When the sum is too large, `left` is the smallest available partner, so the current `right` cannot work with any allowed left endpoint and may be discarded. Each iteration shrinks the interval and the loop must terminate.

**Skip duplicate values at all four logical positions**

The first-position guard

```python
if i and nums[i] == nums[i - 1]:
    continue
```

uses only the first occurrence of a value as `nums[i]`. The second-position guard is relative to the current first position:

```python
if j != i + 1 and nums[j] == nums[j - 1]:
    continue
```

The `j != i + 1` condition is essential. It permits the immediately following equal value to occupy a different index, while rejecting later copies that would recreate the same second value for the same `i`.

After a match, the source first executes `right -= 1` and `left += 1`. It then advances `left` while it equals the value just used at `left - 1`, and retreats `right` while it equals the value just used at `right + 1`. Those comparisons are valid specifically because the initial single-step moves leave the previous endpoints adjacent. As a result, the scan reaches the next genuinely different endpoint pair.

The source does not skip duplicate endpoint values after an unequal comparison. That is still correct: moving through those equal copies can perform extra constant-time iterations, but cannot append a duplicate because appending happens only on equality, after which duplicate runs are skipped.

**Why all and only unique answers are returned**

Take any valid quadruplet and arrange its values in non-decreasing order, as sorting does. The outer guards retain one canonical occurrence of its first value and one canonical occurrence of its second value. For that fixed pair, the remaining valid values lie somewhere in the suffix. The two-pointer proof above shows that comparisons discard only endpoints that cannot belong to a valid residual pair, so the scan cannot jump over that pair without recording an equal-valued representative.

Every appended row is valid because its four indices are strictly ordered and its endpoint sum equals the exact residual target. A duplicate result would need the same four sorted values. The `i` and `j` guards prevent duplication through the first two positions, and the post-match loops prevent duplication through the endpoint positions. Thus the method is complete, valid, and unique without a result set.

**Walk through the repeated-value example**

For `nums = [2, 2, 2, 2, 2]` and `target = 8`, sorting changes nothing. The first loop accepts only `i = 0`; later identical first values are skipped. For this `i`, the second loop accepts `j = 1`. The residual `total` is `4`, and the first endpoint pair is `2 + 2`, so `[2, 2, 2, 2]` is appended. Both pointers move and the scan ends. Later duplicate choices for `j` and `i` are rejected, leaving exactly one result even though five different index quadruples have the same values.

For the richer example `[1, 0, -1, 0, -2, 2]`, sorting produces `[-2, -1, 0, 0, 1, 2]`. With `i = -2` and `j = -1`, the residual is `3`, and the pointer scan finds `1 + 2`. With `i = -2` and `j = 0`, the residual is `2`, and it finds `0 + 2`. Later, `i = -1` and `j = 0` find `0 + 1`. The duplicate guards prevent a second traversal with the other indistinguishable zero as the same logical position.

## Complexity detail

Let $n$ be `len(nums)` and let $A$ be the number of unique returned quadruplets.

- **Time complexity: $O(n^3)$.** Sorting costs $O(n\log n)$. The nested `i` and `j` choices contribute $O(n^2)$ fixed pairs. For each, `left` only increases and `right` only decreases, so the entire while-loop is $O(n)$, including duplicate-skipping iterations. The resulting $O(n^3)$ term dominates sorting.
- **Auxiliary space: $O(n)$ in this Python implementation, excluding output.** The indices, residual sum, and other scan state use $O(1)$ space, which is why the source comment describes the pointer method as $O(1)$. However, Python's `list.sort()` may require $O(n)$ temporary storage, matching the variant manifest. `result` itself stores $A$ lists of four values and therefore occupies $O(A)$ additional output space.

Python evaluates the residual with arbitrary-precision integers, so values near the constraint limits do not overflow. A fixed-width implementation should compute `target - nums[i] - nums[j]` and the pair sum in a wide type.

## Alternatives and edge cases

- **Full-sum two-pointer form:** The optimal variant computes all four terms on each pointer iteration rather than a residual target. It has the same asymptotic behavior; the difference is chiefly expression style.
- **General recursive k-Sum:** Recursively fix values until reaching sorted 2Sum. This makes 5Sum or 6Sum natural, while the selected direct loops avoid recursion for the fixed four-element problem.
- **Stored pair sums (`Solution2` and `Solution3` in the source file):** Precompute index pairs and match complementary pair sums. These alternatives consume substantially more memory and need extra work to ensure indices do not overlap and values are unique; they are not the selected `Solution` entry point.
- **Four-loop enumeration:** It checks the definition directly but costs $O(n^4)$ before deduplication.
- **Fewer than four values:** Empty loop ranges return an empty result without a special branch.
- **Exactly four values:** There is one ordered index quadruple; the pointer comparison decides whether it is returned.
- **Many equal values:** Equal values may occupy multiple positions because indices, not values, must be distinct. The guards remove duplicate output rows only.
- **Zeros, negatives, and mixed signs:** Residual-target comparison remains monotonic after sorting regardless of sign.
- **Target outside all possible sums:** Pointer intervals eventually collapse for every fixed pair, and no row is appended.
- **Large magnitudes:** Python avoids overflow; other languages need wide arithmetic before subtraction or addition.
- **Output order:** The sorted traversal produces sorted rows in a deterministic discovery order, although the problem allows any order.
- **Input mutation:** The implementation sorts the provided list in place. Copy before calling if a surrounding application needs the original order retained.
