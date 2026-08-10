## General

**View every sequence of operations as a partition**

An operation replaces one contiguous subarray by its maximum. If operations are performed repeatedly, the elements that eventually produce one final value always form one contiguous block of the original array. The final value of that block is its maximum; taking maxima in several stages gives the same result as taking the maximum of the whole block at once.

Therefore, the problem can be restated without simulating operations:

Partition `nums` into as many non-empty contiguous blocks as possible so that the sequence of block maxima is non-decreasing.

If the blocks are `B_1, B_2, ..., B_t`, their output is:

`max(B_1), max(B_2), ..., max(B_t)`.

Maximizing the final array size is exactly maximizing `t`. Once such a partition is known, each block can be collapsed independently, so the partition formulation loses no legal solution.

**Recognize the values that can end separate blocks**

Call position `i` a weak prefix record when:

`nums[i] >= max(nums[0..i-1])`.

“Weak” means equality is allowed. The first position is always a record. The protected source counts exactly these positions:

`mx` is the largest value seen so far, and `ans` increases whenever `x >= mx`. After accepting `x`, it assigns `mx = x`. Since accepted values are prefix maxima, `mx` remains the maximum of the entire scanned prefix, even though the source does not update it on smaller values.

For example, in `[4,2,5,3,5]`:

- `4` is the first record;
- `2` is below the prefix maximum `4`;
- the first `5` is a new record;
- `3` is below `5`;
- the final `5` equals the prefix maximum and is also a weak record.

The source counts three.

**Construct a valid partition from all weak records**

Let the weak-record indices be:

`r_1 < r_2 < ... < r_t`.

Create blocks that end at these indices:

- the first block is `nums[0..r_1]`;
- for `j > 1`, block `j` is `nums[r_(j-1)+1 .. r_j]`;
- if elements remain after `r_t`, append that trailing suffix to the last block.

The first record is index zero because values are positive and `mx` starts at zero, so the first block is ordinarily the singleton at index zero.

Why is the maximum of block `j` exactly `nums[r_j]`? Position `r_j` is a prefix record, so its value is at least every earlier element, including all other elements in its block. The record values are non-decreasing by definition. Thus the block maxima form:

`nums[r_1] <= nums[r_2] <= ... <= nums[r_t]`.

Any trailing elements after the last record are no larger than the last prefix maximum, so attaching them to the last block does not change that block's maximum.

This proves that all `t` counted records can be retained as a non-decreasing final array. It also explains the example partition:

`[4] | [2,5] | [3,5]`

with maxima `[4,5,5]`.

**Prove no partition can have more blocks**

It is not enough to show that the greedy count is achievable; it must also be an upper bound.

Consider any valid partition into blocks `B_1, ..., B_t` with non-decreasing maxima `M_1 <= ... <= M_t`. In each block `B_j`, choose an occurrence of its maximum `M_j`.

Every element in an earlier block is at most that earlier block's maximum, and every earlier maximum is at most `M_j`. Every earlier element inside `B_j` is also at most `M_j` because it is the block maximum. Therefore, when the chosen occurrence of `M_j` is reached in the original scan, no preceding array value is greater than it.

That chosen position is a weak prefix record.

Different blocks contain different positions, so the `t` blocks give `t` distinct weak-record witnesses. Consequently, no valid partition can contain more blocks than the total number of weak prefix records.

The construction achieves exactly that count, and the witness argument proves every solution has at most that count. These matching bounds establish optimality.

**Why equality must be retained**

Suppose the current prefix maximum is five and a later value is also five. That later position can end a new block whose maximum is five, following a previous block with maximum five. The result remains non-decreasing because equality is allowed.

Using `x > mx` would count only strict records and lose valid blocks. The source correctly uses `mx <= x`.

**Why smaller values are skipped rather than changing mx**

When `x < mx`, making `x` a singleton block immediately after a block with maximum `mx` would create a decrease. It must be absorbed into some block that also contains a later value at least `mx`, or into the final block if no such later record exists.

Either way, `x` cannot serve as the maximum witness of its own block in an optimal non-decreasing partition. It should not increase `ans`, and it should not lower `mx` because the earlier prefix maximum still constrains every later block maximum.

**Relate the count back to actual operations**

The algorithm returns only the maximum size, so it does not explicitly perform operations. The record-based partition proves realizability. For each block containing more than one element, select that full block and replace it by its maximum. Blocks can be processed independently from right to left to avoid any indexing inconvenience. Singleton blocks require no operation.

The resulting values are the non-decreasing record values and the array has exactly `ans` elements.

## Complexity detail

Let `n = len(nums)`. The source scans each value exactly once. Each iteration performs one comparison and, only for a weak record, two assignments/increments. Total time is `O(n)`.

The method stores only `ans`, `mx`, and the loop variable. It does not build the partition or modify `nums`, so auxiliary space is `O(1)`.

The linear time is asymptotically optimal for an unsummarized array: an unseen value can create an additional weak record or raise the prefix maximum and change how later values are counted, so every input position may matter.

The initialization `mx = 0` relies on the documented positive values. With arbitrary negative integers, `mx` should instead start at negative infinity or from the first element. Under `nums[i] >= 1`, the exact source is safe.

## Alternatives and edge cases

- **Dynamic programming over partitions:** One could define the best block count for prefixes and possible last maxima, but the weak-record upper bound collapses the problem to one greedy scan.
- **Monotonic stack simulation:** Stacks are useful for related merge problems, but here every merge takes a maximum and only the count is requested. Prefix records already characterize the optimum.
- **Actually perform subarray replacements:** Searching and mutating blocks adds work and indexing complexity. The partition proof shows the answer without constructing the operations.
- **Count strict prefix maxima:** This is wrong for non-decreasing output because equal adjacent block maxima are allowed. Weak records with `x == mx` must count.
- **Use the longest non-decreasing subsequence:** Selected subsequence values do not automatically correspond to maxima of contiguous blocks. The prefix-record condition is stronger and is derived from the operation.
- **Already non-decreasing array:** Every value is at least the preceding prefix maximum, so every position is counted and the answer is `n`.
- **Strictly decreasing array:** Only the first value is a weak record. The entire array must collapse into one block with that first, largest maximum.
- **All values equal:** Every position is a weak record, so no operation is needed and the answer is `n`.
- **One element:** It is the first weak record and the answer is one.
- **Small values between records:** They are absorbed into the block ending at the next record and do not change that block's maximum.
- **Trailing values below the last record:** They are absorbed into the final block; its maximum remains the last prefix maximum.
- **A later equal maximum:** It can end a separate block, which is why the comparison is inclusive.
- **Positive-value guarantee:** Starting `mx` at zero would fail for an all-negative generalization, but it is correct for the stated domain.
- **Input preservation:** The protected method returns only a count and leaves the original list untouched.
