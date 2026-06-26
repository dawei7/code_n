# Partition Equal Subset Sum

| | |
|---|---|
| **ID** | `dp_17` |
| **Category** | dynamic |
| **Complexity (required)** | $O(N * S)$ Time, $O(S)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |

## Problem statement

Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

**Input:** An array `nums` of positive integers.
**Output:** A boolean: `True` if a valid partition exists, `False` otherwise.

## When to use it

- You should instantly recognize this as a thin disguise for the **Subset Sum** (`dp_06`) or **0/1 Knapsack** (`dp_03`) problem!
- Use it to demonstrate your ability to reduce a seemingly complex partitioning problem into a standard algorithmic template.

## Approach

**1. The Mathematical Reduction:**
If we divide the array into two subsets A and B such that \text{Sum}(A) == \text{Sum}(B), then it mathematically must be true that \text{Sum}(A) + \text{Sum}(B) = \text{TotalSum}.
Therefore, 2 x \text{Sum}(A) = \text{TotalSum}.
This implies two absolute facts:
1. If the `TotalSum` is ODD, it is physically impossible to partition the array equally using integers. Return `False` instantly.
2. If the `TotalSum` is EVEN, the problem is exactly identical to asking: "Does there exist ANY subset A whose sum is exactly \frac{\text{TotalSum}}{2}?"

We have now perfectly reduced the problem to `dp_06 - Subset Sum` with `target = TotalSum // 2`!

**2. Define the State:**
Let `dp[s]` be a boolean indicating whether a subset exists that sums to exactly `s`.

**3. Find the Transition (The recurrence relation):**
For each number `num` in the array, we iterate backwards through the DP array from `target` down to `num`.
We update `dp[s]` to be `True` if it was already `True` (we don't need `num`), OR if `dp[s - num]` was `True` (we use `num` to reach `s`).
`dp[s] = dp[s] OR dp[s - num]`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_17: Partition Equal Subset Sum.

True iff arr can be split into two equal-sum subsets.
"""


def solve(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False
    target = total // 2
    reachable = {0}
    for v in arr:
        reachable = reachable | {s + v for s in reachable}
    return target in reachable
```

</details>

## Walk-through

`nums = [1, 5, 11, 5]`.
`TotalSum` = 22. `target` = 11.
`dp` size 12 initialized to `[T, F, F, F, F, F, F, F, F, F, F, F]`.

1. **num = 1:**
   - Loop `s` from 11 down to 1.
   - `dp[1] = dp[1] or dp[0] = T`.
   - State: `[T, T, F, F, F, F, F, F, F, F, F, F]`.
2. **num = 5:**
   - Loop `s` from 11 down to 5.
   - `dp[6] = dp[6] or dp[1] = T`.
   - `dp[5] = dp[5] or dp[0] = T`.
   - State: sums `{0, 1, 5, 6}` are `True`.
3. **num = 11:**
   - Loop `s` from 11 down to 11.
   - `dp[11] = dp[11] or dp[0] = T`.
   - `dp[target]` is now `True`! Early stopping triggers.

Result is `True`. ✓ (The subsets are `[11]` and `[1, 5, 5]`).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(S)$ |
| **Average** | $O(N * S)$ | $O(S)$ |
| **Worst** | $O(N * S)$ | $O(S)$ |

*Where N is the length of `nums` and S is half the total sum.*
The outer loop runs N times, the inner loop up to S times. Total worst-case time is strictly $O(N x S)$.
Because S is bounded by N x 100 (given standard LeetCode constraints where `nums[i] <= 100`), this algorithm is exceedingly fast. The early stopping optimization often drops the best-case time to near $O(N)$.
Space is exactly $O(S)$ using the 1D rolling array optimization.

## Variants & optimizations

- **Partition to K Equal Sum Subsets:** What if you need to partition the array into K equal subsets instead of 2? This entirely shatters the standard DP approach! If K > 2, 1D DP is mathematically insufficient. You must use Bitmask DP ($O(K x 2^N)$) or purely DFS Backtracking with heavy pruning.
- **Bitset Optimization:** In C++, `std::bitset` allows you to execute the inner loop as a single $O(1)$ bitwise shift operation (`dp |= (dp << num)`). This is a phenomenally powerful trick in competitive programming to bypass TLE limits.

## Real-world applications

- **Fair Division:** Dividing an inheritance or a collection of discrete, indivisible assets between two parties perfectly equally.
- **Process Scheduling:** Load-balancing jobs of varying processing times evenly across exactly two CPU cores to minimize total execution time (makespan).

## Related algorithms in cOde(n)

- **[dp_06 - Subset Sum](dp_06_subset-sum.md)** — The literal exact same algorithm. This file serves to show the mathematical reduction.
- **[bb_06 - Subset Sum (Branch & Bound)](../branch_and_bound/bb_06_subset-sum.md)** — How to solve this if S is astronomically large and N is small.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
