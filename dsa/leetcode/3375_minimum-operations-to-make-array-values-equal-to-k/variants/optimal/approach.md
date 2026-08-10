## General

**The operation can only lower values.** It replaces values strictly above a chosen `h` by `h`. No element ever increases. Therefore, if any `nums[i] < k`, it can never reach the larger target `k`. The source detects this immediately and returns `-1`.

Assume from now on that every value is at least `k`.

**Understand what validity permits at one step.** Let the current distinct values in descending order be

$$
v_1>v_2>\cdots>v_p.
$$

For `h` to be valid, all current values strictly greater than `h` must be identical. If `h < v_2`, then both $v_1$ and $v_2$ are above `h` and are different, so validity fails. Consequently a valid operation that changes the maximum cannot jump below the next distinct level.

Choosing `h=v_2` is valid: the only values strictly above it are copies of $v_1$. The operation merges the entire top level into the next level in one step.

**Each distinct level above `k` costs one operation.** Repeating the merge removes distinct values from largest downward. Once only the smallest current level above `k` remains, choose `h=k` and lower it to the target. This constructs a solution using one operation for every distinct original value greater than `k`.

No operation can eliminate two distinct levels above `k` at once, because choosing below the second-highest would make the values above `h` non-identical. Therefore the same count is also a lower bound and is the minimum.

**Why frequencies do not matter.** One operation changes every occurrence above `h` simultaneously. Whether the current maximum appears once or one hundred times, lowering that entire value level still costs one operation. Only the set of distinct heights matters.

**How the source counts those levels.** Set `s` stores every distinct input value. Variable `mi` records the minimum. Because the earlier guard ensures every value is at least `k`, there are two cases:

- if `mi == k`, the set includes target level `k`, which needs no operation, so return `len(s)-1`;
- if `mi > k`, every set value is above the target, and even the minimum must be lowered in a final operation, so return `len(s)`.

Expression `len(s) - int(k == mi)` implements both cases. Python converts true to one and false to zero.

**Trace `[5,2,5,4,5]` with `k=2`.** Distinct levels are 5, 4, and 2. First choose `h=4`; only the 5s lie above it, so they become 4. Then choose `h=2`; all current 4s are identical above two and become two. There are two distinct values above the target, matching the return.

**Trace a target below the minimum.** For `[9,7,5,3]` and `k=1`, all four distinct levels exceed the target. The sequence can use `h=7,5,3,1`, costing four. Since `mi != k`, the source does not subtract one.

**Why a below-target value makes the whole task impossible.** Later operations may also lower other values past it, but the final goal requires every value to equal exactly `k`. The already smaller element cannot be raised or selected for replacement because only values greater than `h` change. No sequence repairs it.

**Why the returned count is exact.** The validity rule forces distinct levels to be removed one at a time, establishing the lower bound. Descending merges realize that bound and end at `k` whenever no value starts below it. The set/minimum arithmetic returns precisely this number.

## Complexity detail

The loop visits each of $n$ values once. Hash-set insertion is expected $O(1)$, so expected time is $O(n)$. An early below-target value may stop sooner.

If $u$ distinct values occur, the set uses $O(u)$ space. Other variables use $O(1)$. This matches the manifest; with the stated value range, $u$ is also at most 100.

## Alternatives and edge cases

- **Store only values greater than `k`:** Then the answer is simply that set's size; the exact source stores all values and conditionally excludes `k`.
- **Sort distinct values:** It makes the constructive order explicit but costs $O(n\log n)$ rather than expected linear time.
- **Simulate array replacements:** It repeats work across elements and is unnecessary once distinct levels are understood.
- **Any value below `k`:** Return `-1` immediately.
- **All values equal `k`:** The set has one value, the subtraction produces zero operations.
- **All values equal above `k`:** One valid operation lowers them directly to `k`.
- **Minimum above `k`:** It still needs the final operation to target.
- **Many copies of one level:** Frequency does not increase the count.
- **Negative values:** The local constraints are positive, but the order argument itself depends only on comparisons.
- **Valid `h` between levels:** It can lower the maximum to an intermediate new level, but that never reduces the minimum number of level eliminations.
- **Skipping a distinct level:** Choosing `h` below it is invalid while a larger different level remains.
- **Boolean-to-integer conversion:** `int(k == mi)` removes only the already-correct target level.
- **Infinity initialization:** `mi` is always replaced because the array is nonempty.
- **Input preservation:** Only a set and minimum are built; `nums` is unchanged.
- **Import requirements:** `inf` and `List` must be available.
