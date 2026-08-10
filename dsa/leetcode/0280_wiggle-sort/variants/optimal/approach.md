## General

**Repair one adjacent inequality at a time**

The required pattern is

$$
\texttt{nums}[0]
\le \texttt{nums}[1]
\ge \texttt{nums}[2]
\le \texttt{nums}[3]
\ge \cdots.
$$

Odd indices are peaks: an odd-indexed value must be at least the value immediately before it. Even positive indices are valleys: an even-indexed value must be at most the value immediately before it.

The exact solution scans from left to right. At index `i`, it inspects only `nums[i - 1]` and `nums[i]`. If their required inequality is reversed, it swaps those two adjacent values. The central insight is that this local repair also preserves every inequality already established to the left, so no sorting or backward repair is needed.

**State the parity rule exactly**

When `i` is odd, the pair occupies an even index followed by an odd index, so it must satisfy

$$
\texttt{nums}[i-1]\le\texttt{nums}[i].
$$

The source swaps precisely when `nums[i] < nums[i - 1]`.

When `i` is even, the pair occupies an odd index followed by an even index, so it must satisfy

$$
\texttt{nums}[i-1]\ge\texttt{nums}[i].
$$

The source swaps precisely when `nums[i] > nums[i - 1]`.

These two violations are joined by `or` in the condition. If the pair already satisfies the required non-strict inequality, it is left unchanged. Equal adjacent values are valid in either orientation because the pattern uses `<=` and `>=`, not strict comparisons.

**Why swapping fixes the current pair**

For odd `i`, a swap occurs only when the left value is larger than the right value. Exchanging them puts the smaller value on the even-indexed left side and the larger value on the odd-indexed right side, establishing `nums[i - 1] <= nums[i]`.

For even `i`, a swap occurs only when the new right value is larger than the left value. Exchanging them places the larger value at the odd-indexed left position and the smaller value at the even-indexed right position, establishing `nums[i - 1] >= nums[i]`.

Thus one adjacent swap is always sufficient to repair the newly considered inequality.

**Why the swap cannot break the earlier pair**

The subtle point is that swapping changes `nums[i - 1]`, which also belongs to the already processed pair ending at `i - 1`. The parity pattern guarantees that the change moves this shared value in a safe direction.

Suppose `i` is odd. Before this step, the previous inequality is

$$
\texttt{nums}[i-2]\ge\texttt{nums}[i-1].
$$

A swap occurs because the old `nums[i]` is smaller than the old `nums[i - 1]`. After the swap, position `i - 1` receives that smaller value. If `nums[i - 2]` was at least the old, larger value, it is certainly at least the new, smaller value. The earlier inequality remains true.

Now suppose `i` is even. The previous inequality is

$$
\texttt{nums}[i-2]\le\texttt{nums}[i-1].
$$

A swap occurs because the old `nums[i]` is larger than the old `nums[i - 1]`. Position `i - 1` receives that larger value. If `nums[i - 2]` was at most the old, smaller value, it remains at most the new, larger value. Again, the earlier inequality is preserved.

Positions before `i - 1` are untouched, so all still-earlier relationships remain unchanged.

**A left-to-right invariant proves the complete result**

After finishing iteration `i`, the prefix from index 0 through `i` satisfies every required alternating inequality.

At `i = 1`, the algorithm either finds the first pair valid or swaps it into valid order. For a later index, assume the prefix through `i - 1` is valid. If the new pair is valid, nothing changes. If it is invalid, the swap fixes that pair, and the parity argument above proves it preserves the only earlier pair sharing a modified position. All other earlier pairs are untouched. The invariant therefore holds after every iteration.

When the loop ends at the last index, the valid prefix is the whole array, proving the in-place result has the required wiggle pattern.

**Trace the first example**

Starting from `[3,5,2,1,6,4]`:

| `i` | Required pair relation | Action | Array afterward |
|---:|---|---|---|
| 1 | `3 <= 5` | already valid | `[3,5,2,1,6,4]` |
| 2 | `5 >= 2` | already valid | `[3,5,2,1,6,4]` |
| 3 | `2 <= 1` | swap 2 and 1 | `[3,5,1,2,6,4]` |
| 4 | `2 >= 6` | swap 2 and 6 | `[3,5,1,6,2,4]` |
| 5 | `2 <= 4` | already valid | `[3,5,1,6,2,4]` |

The final array matches an accepted output. It need not be the only valid permutation.

For `[6,6,5,6,3,8]`, every required comparison already holds, including the equality `6 <= 6`, so the algorithm makes no swaps.

## Complexity detail

Let $n$ be the array length. The loop visits each index from 1 through $n-1$ once. Each visit performs constant-time parity checks, comparisons, and at most one swap, giving $O(n)$ time.

This is asymptotically optimal because producing or validating an arrangement can depend on values throughout the input; a worst-case method must examine the array linearly.

The transformation uses only the loop index and temporary references involved in tuple assignment. It allocates no size-dependent data structure, so auxiliary space is $O(1)$. The list is modified in place, and the method intentionally returns `None`.

The algorithm performs at most $n-1$ swaps, one for each adjacent relationship. In many inputs it performs fewer, including zero for an already wiggled array.

## Alternatives and edge cases

- **Sort then swap neighboring positions:** Sorting first and exchanging selected adjacent values can create the wiggle pattern, but costs $O(n\log n)$ time and is unnecessary for non-strict inequalities.
- **Build a separate result:** Selecting alternating low and high values into another list is possible but uses $O(n)$ extra space and often still requires sorting.
- **Check only odd peaks:** Ensuring each odd index dominates both neighbors is equivalent, but the one-pass adjacent formulation repairs the right relationship as it arrives and proves preservation locally.
- **Length one:** The loop is empty, and the one-element array vacuously satisfies every adjacent inequality.
- **Length two:** One comparison and at most one swap establish `nums[0] <= nums[1]`.
- **All values equal:** Every non-strict inequality holds, so no swaps occur and the array is valid.
- **Already wiggled input:** Every violation test is false; the method preserves the existing order.
- **Strict wiggle variant:** This solution targets `<=` and `>=`. A requirement for strict `<` and `>` with duplicates is a different problem and may need median partitioning; the local equality-friendly proof would not suffice.
- **Negative values outside the stated range:** The logic uses only comparisons, so it would still work unchanged even though legal values are non-negative.
- **Input mutation:** Swapping changes the caller's list. That is required by the function contract; callers needing the original order must copy it before calling.
- **Existence guarantee:** For this non-strict version, the greedy proof itself constructs a valid arrangement for any array. The stated guarantee is therefore consistent but not additionally needed by the implementation.
