## General

**Sorting turns a grouping search into local checks**

Every output group must contain exactly three values, and within a group the difference between the maximum and minimum must be at most `k`. The original order does not matter, so the first operation is `nums.sort()`. After sorting, the smallest and largest value of any three consecutive entries are immediately visible.

The implementation then walks through the sorted list in steps of three. For a block beginning at `i`, it checks

`nums[i + 2] - nums[i] > k`.

Because `nums[i] <= nums[i + 1] <= nums[i + 2]`, this is exactly the block’s maximum-minus-minimum difference. If it is too large, the function returns an empty list. Otherwise, the slice `nums[i:i + 3]` is appended to the answer.

The even-looking detail that the step is three follows from the contract: the array length is divisible by three, and every element must belong to exactly one size-three group. There are no leftover values.

**Why the smallest available values should stay together**

Consider the smallest value not yet assigned, call it $x$. It must be grouped with two other remaining values. In sorted order, the next two values are the closest possible partners on the high side. Any other partners are at least as large, so they cannot produce a smaller maximum-minus-minimum difference.

Therefore, if the third-smallest remaining value is already more than `k` above $x$, no legal group can contain $x$. Since every valid partition must place $x$ somewhere, the entire instance is impossible. This proves that a failed consecutive block is a genuine impossibility signal rather than merely a failure of one arbitrary grouping choice.

When the first three remaining values do satisfy the limit, taking them together is the safest use of the smallest value: replacing either partner with a later, larger value cannot improve that group. Keeping later values for later groups also avoids spending a small value that may be needed to stay close to other small values. Applying this same argument after removing the first triple gives the greedy grouping inductively.

Another way to see the structure is to imagine group maxima in sorted order. Each group consumes three elements. The first group cannot avoid drawing three values from the low end without making its maximum at least as large as the third sorted value. The consecutive construction realizes the smallest possible maximum for that group. Repeating this rank argument aligns every group with one consecutive block.

**Trace the exact data flow**

Suppose `nums = [1, 3, 4, 8, 7, 9]` and `k = 2`. Sorting changes it to `[1, 3, 4, 7, 8, 9]`. The first block has difference `4 - 1 = 3`, which exceeds two. The smallest value one cannot be paired with two legal partners: even its two closest remaining choices are three and four, and four is too far away. Returning an empty list is correct.

With `nums = [1, 2, 3, 7, 8, 9]` and `k = 2`, both consecutive differences are two. The output is `[[1, 2, 3], [7, 8, 9]]`. The solution does not need to explore permutations inside a group because only its values and range matter.

**Why checking only the endpoints is sufficient**

For a sorted triple $a \le b \le c$, every pairwise absolute difference is at most $c-a$. If $c-a \le k$, then $b-a \le k$ and $c-b \le k$ automatically. Conversely, if the maximum/minimum difference exceeds `k`, the group violates the stated condition. Thus one subtraction per group completely validates it.

**Important implementation behavior**

Python’s `list.sort()` rearranges `nums` in place. The method therefore does not preserve the caller’s original order. This does not affect the returned answer because order has no semantic role in the problem, but it is observable to a caller that reuses the same list.

Each appended slice is a new three-element list. The returned groups do not alias contiguous regions of `nums`; changing a returned inner list later would not rewrite `nums`.

If any block fails, the already-created local `ans` is discarded when the method returns `[]`. There is no partial solution because the contract requires a partition using every element.

## Complexity detail

Let $N$ be the number of values. Sorting takes $O(N\log N)$ time. The block loop makes $N/3$ iterations, with constant-time endpoint checking and copying exactly three values each time, for $O(N)$ additional time. The total is $O(N\log N)$.

The returned nested lists contain all $N$ values, so output space is $O(N)$. Python’s Timsort can use $O(N)$ temporary storage in the worst case, making auxiliary implementation space $O(N)$ as reflected by the manifest. Excluding sorting workspace and the required output, the loop’s own state is $O(1)$.

## Alternatives and edge cases

- **Backtracking over group assignments:** Trying arbitrary triples explores a combinatorial number of partitions. Sorting exposes the forced local feasibility checks.
- **Heap extraction in triples:** Repeatedly taking the three smallest values also works but costs $O(N\log N)$ with a heap and is less direct than one sort followed by a scan.
- **Check all three pair differences:** For a sorted triple, maximum minus minimum dominates the other two, so extra comparisons are redundant.
- **A failed first block:** If even the two closest partners are too far from the smallest value, no rearrangement can rescue it.
- **A failed later block:** Earlier valid triples have consumed exactly the smallest available ranks. The same smallest-remaining-value argument applies inductively.
- **Duplicate values:** Sorting keeps equal values adjacent, and a zero difference is always within any nonnegative `k`.
- **`k = 0`:** Every group must contain three equal values; the endpoint test enforces exactly that condition.
- **Input mutation:** The exact implementation sorts `nums` in place. Copy first if caller-visible preservation were required, but that would add another $O(N)$ list.
- **Failure output:** The required signal is the completely empty list, not a partial list of groups formed before the failing block.
