## General

**Turn an unordered search into an ordered one**

The task asks for value quadruplets, but the four values must come from four distinct array indices. Trying every index quadruple would use four nested loops and take $O(n^4)$ time. The selected implementation removes one entire factor of $n$ by sorting `nums`, explicitly choosing the first two positions, and finding the remaining two positions with a two-pointer scan.

Sorting is the key that makes pointer movement meaningful. After `nums.sort()`, moving a pointer to the right cannot decrease its value, and moving a pointer to the left cannot increase its value. Equal values also become adjacent, which lets the code suppress duplicate value quadruplets without storing all answers in a set.

The sort changes the caller's list in place. That is acceptable for the problem contract because only the returned quadruplets are specified; preserving the original ordering of `nums` is not required.

**Give the four positions a permanent order**

The implementation always maintains indices

$$
i < j < k < l.
$$

The outer loop chooses `i`, the inner loop chooses `j`, and then `k = j + 1` and `l = n - 1` delimit the remaining suffix. Because each pointer occupies a different ordered position, a reported quadruplet can never reuse an index. No additional distinct-index check is needed.

The initial guard returns an empty list when `n < 4`. Four distinct indices cannot exist in that case. The loop bounds also reflect how many positions must remain: `i` stops before the last three indices, while `j` stops before the last two.

**Fix two values and reduce 4Sum to sorted 2Sum**

For one fixed pair `nums[i]` and `nums[j]`, the code starts `k` at the smallest available suffix value and `l` at the largest. It computes the complete candidate sum

```python
x = nums[i] + nums[j] + nums[k] + nums[l]
```

and compares it with `target`.

- If `x < target`, the sum is too small. Decreasing `l` would make the sum no larger, so that cannot help. The only useful move is `k += 1`, which tries a value that is at least as large.
- If `x > target`, the sum is too large. Increasing `k` would make it no smaller, so that cannot help. The only useful move is `l -= 1`, which tries a value that is at most as large.
- If `x == target`, the four sorted values form a valid answer. The code appends them, then moves both `k` and `l` inward because that exact endpoint pair has already been consumed.

These moves do not skip a possible solution. Suppose `x < target`. With the current `k`, every index between `k + 1` and `l` used as the right endpoint has value at most `nums[l]`, so every such pair sum is also too small. Thus no solution can still use that `k`. The argument is symmetric when `x > target`: no solution can still use the current `l`.

**Remove duplicates at the level where they arise**

The answer must contain unique value quadruplets even when the input contains repeated values. Sorting lets the implementation handle that locally.

At the `i` level, this condition skips every occurrence of a value except its first possible occurrence:

```python
if i and nums[i] == nums[i - 1]:
    continue
```

At the `j` level, the code similarly skips a repeated second value, but only relative to the current `i`:

```python
if j > i + 1 and nums[j] == nums[j - 1]:
    continue
```

The boundary `j > i + 1` matters. A value equal to `nums[i]` may legitimately be selected from a different index, as in `[2, 2, 2, 2]`; the test skips only a repeated candidate for the same logical second position.

After finding a valid pair, both endpoints move once. The following loops then pass over all adjacent copies of the just-used values at `k` and `l`. This prevents the same fixed `i`, fixed `j`, and endpoint values from producing the same quadruplet again. Duplicates are skipped only after recording the valid combination, so necessary repeated values are retained when enough distinct indices exist.

**Why the result is complete and unique**

Consider any valid value quadruplet written in non-decreasing order. There is a first usable occurrence of its first value for `i` and, after that, a first usable occurrence of its second value for `j`. The duplicate guards preserve those representatives. For that fixed pair, the two-pointer scan cannot step past the quadruplet's remaining pair: every step discards only an endpoint that the comparison proves cannot participate in a target pair. The scan therefore reaches and records the remaining two values.

Conversely, every appended row uses four ordered, distinct indices and is appended only when its sum equals `target`, so every reported row is valid. The three layers of duplicate suppression ensure that no identical sorted value quadruplet can be appended twice. Together, those facts establish completeness, validity, and uniqueness.

**Trace the central decisions on the first example**

Sorting `[1, 0, -1, 0, -2, 2]` gives `[-2, -1, 0, 0, 1, 2]`. With `i` at `-2` and `j` at `-1`, the endpoints begin at `0` and `2`; the sum is `-1`, so `k` moves right until the pair `1, 2` yields zero, producing `[-2, -1, 1, 2]`. With the same `i` and `j` moved to the first `0`, the endpoint pair `0, 2` produces `[-2, 0, 0, 2]`. Repeated second-position zeros are skipped. Later, `i = -1` leads to `[-1, 0, 0, 1]`. No other fixed pair can produce a new target quadruplet.

## Complexity detail

Let $n$ be `len(nums)` and let $A$ be the number of returned quadruplets.

- **Time complexity: $O(n^3)$.** Sorting costs $O(n\log n)$. There are $O(n^2)$ choices of `i` and `j`, and the `k`/`l` scan is linear for each fixed pair because each pointer moves inward at most $n$ times. Therefore the scan costs $O(n^3)$ and dominates sorting. Appending each four-value result costs constant time, and $A$ itself is bounded by the work already considered.
- **Auxiliary space: $O(n)$ for this Python implementation, excluding the answer.** Python's in-place list sort may use $O(n)$ temporary memory. The loop indices and sum use $O(1)$ space. If the sorting algorithm's internal storage is excluded, the scanning portion is $O(1)$ auxiliary space. The returned `ans` requires $O(A)$ list entries, or $O(4A)=O(A)$ value slots because every row has exactly four values. This distinction explains the manifest's $O(n)$ bound while some abstract presentations call the method constant-space after sorting.

The arithmetic is safe in Python because integers grow as needed. In a fixed-width language, four values near $10^9$ should be promoted to a sufficiently wide integer type before addition.

## Alternatives and edge cases

- **Four nested loops:** It is conceptually direct but costs $O(n^4)$ and still needs careful value-level deduplication.
- **Recursive generalized k-Sum:** Fix one value recursively until reaching a two-pointer 2Sum base case. It generalizes cleanly to 5Sum and beyond, but the direct two-loop form here is simpler for exactly four values.
- **Pair-sum hash table:** Store index pairs by their sum and match complementary sums. It can reduce repeated arithmetic, but may require $O(n^2)$ or more memory and careful enforcement of non-overlapping indices and unique outputs.
- **Hash-set 2Sum after fixing two values:** This preserves $O(n^3)$ time but uses extra per-scan storage and makes deterministic duplicate handling less transparent than sorted pointers.
- **Fewer than four values:** The explicit `n < 4` guard returns `[]` immediately.
- **Exactly four values:** The loops examine the only possible index quadruple and return it precisely when its sum equals `target`.
- **All values equal:** Enough copies may form one answer, as five copies of `2` with target `8` do; duplicate skipping returns `[[2, 2, 2, 2]]` only once.
- **Negative values and a negative target:** Pointer monotonicity depends on sorted order, not on values being positive, so the same comparisons remain valid.
- **Repeated values are not forbidden:** Only indices must be distinct. Duplicate suppression removes repeated output rows, not legal use of equal values from different positions.
- **Any output order:** Sorting causes every row and the overall traversal to be deterministic, but the contract does not require that order.
- **Input mutation:** `nums.sort()` rearranges the provided list; callers that need the original order must pass a copy, although this problem imposes no such requirement.
