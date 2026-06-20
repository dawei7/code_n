# Target Sum

| | |
|---|---|
| **ID** | `dp_28` |
| **Category** | dynamic |
| **Complexity (required)** | $O(N * S)$ Time, $O(S)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Target Sum](https://leetcode.com/problems/target-sum/) |

## Problem statement

You are given an integer array `nums` and an integer `target`.
You want to build an expression out of `nums` by adding one of the symbols `+` and `-` before each integer in `nums` and then concatenate all the integers.
Return the number of different expressions that you can build, which evaluates to `target`.

**Input:** An integer array `nums` and an integer `target`.
**Output:** An integer representing the total number of ways to reach the target.

## When to use it

- To show your ability to mathematically reduce a seemingly unique combinatorial problem directly into the canonical **0/1 Knapsack** (`dp_03`) or **Subset Sum** (`dp_06`) framework.

## Approach

**1. The Mathematical Reduction:**
Let's divide all the numbers into two sets:
- Set P: The numbers that we assigned a `+` sign.
- Set N: The numbers that we assigned a `-` sign.

The sum of our expression is: \text{Sum}(P) - \text{Sum}(N) = \text{target}.
We also know absolutely that: \text{Sum}(P) + \text{Sum}(N) = \text{TotalSum} (the sum of all elements in the array).

If we add these two equations together, we get:
2 x \text{Sum}(P) = \text{target} + \text{TotalSum}
\text{Sum}(P) = (\text{target} + \text{TotalSum}) / 2

This is an incredible revelation! The problem is mathematically identical to asking: **"How many subsets of `nums` sum up to exactly `(target + TotalSum) / 2`?"**
We have perfectly reduced this to the `dp_06 - Subset Sum` problem!

**Edge Cases to catch immediately:**
- If `(target + TotalSum)` is an odd number, it's mathematically impossible to reach the target using integers. Return 0.
- If `abs(target) > TotalSum`, it's impossible to reach. Return 0.

**2. Define the State:**
Let `dp[s]` be the number of ways to pick a subset of numbers that sum to exactly `s`.
Our new target is S = (\text{target} + \text{TotalSum}) / 2.

**3. Find the Base Case:**
`dp[0] = 1`. There is exactly 1 way to reach a sum of 0: pick no elements! (Note: if there are zeroes in `nums`, they will naturally double the ways later).

**4. Find the Transition (The recurrence relation):**
For each number `num` in the array, we iterate backwards through the DP array from S down to `num`.
The number of ways to reach sum `s` is simply the number of ways we ALREADY had to reach `s` (without using `num`), PLUS the number of ways to reach `s - num` (which means we decided to use `num`)!
`dp[s] = dp[s] + dp[s - num]`

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_28: Target Sum.

Reduce to subset-sum: find number of subsets with sum
equal to (target + total_sum) // 2. Classic 0/1 knapsack
counting DP with 1D backward iteration.
"""


def solve(nums, n, target):
    total = sum(nums)
    if (target + total) % 2 != 0 or abs(target) > total:
        return 0
    s = (target + total) // 2
    dp = [0] * (s + 1)
    dp[0] = 1
    for num in nums:
        for j in range(s, num - 1, -1):
            dp[j] += dp[j - num]
    return dp[s]
```

</details>

## Walk-through

`nums = [1, 1, 1, 1, 1]`, `target = 3`.
`total_sum` = 5.
`subset_target` = (3 + 5) / 2 = 4.
`dp` size 5 initialized to `[1, 0, 0, 0, 0]`.

1. **num = 1 (1st):**
   - `s=4..1`: `dp[1] += dp[0]`.
   - `dp` state: `[1, 1, 0, 0, 0]`.
2. **num = 1 (2nd):**
   - `s=4..1`: `dp[2] += dp[1]`, `dp[1] += dp[0]`.
   - `dp` state: `[1, 2, 1, 0, 0]`.
3. **num = 1 (3rd):**
   - `s=4..1`: `dp[3]+=dp[2]`, `dp[2]+=dp[1]`, `dp[1]+=dp[0]`.
   - `dp` state: `[1, 3, 3, 1, 0]`. (This is Pascal's Triangle!).
4. **num = 1 (4th):**
   - `s=4..1`: `dp[4]+=1`, `dp[3]+=3`, `dp[2]+=3`, `dp[1]+=1`.
   - `dp` state: `[1, 4, 6, 4, 1]`.
5. **num = 1 (5th):**
   - `s=4`: `dp[4] += dp[3] = 1 + 4 = 5`.
   - `dp` state: `[1, 5, 10, 10, 5]`.

Result `dp[4]` is 5. ✓ (The subsets of size 4 out of 5 elements is exactly 5!).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(S)$ |
| **Average** | $O(N * S)$ | $O(S)$ |
| **Worst** | $O(N * S)$ | $O(S)$ |

*Where N is the number of elements and S is `subset_target`.*
The outer loop runs N times. The inner loop runs up to S times. Total time is $O(N x S)$.
Space complexity is strictly $O(S)$ for the 1D rolling array.

## Variants & optimizations

- **Top-Down Memoization with True Target:** If the mathematical trick eludes you during an interview, you can solve this directly using Top-Down Memoization! Your state is `solve(index, current_sum)`. Because `current_sum` can be negative, you must offset it by `TotalSum` when storing it in a 2D cache array, or simply use a Hash Map `cache[(index, current_sum)]`. Time complexity remains $O(N x \text{TotalSum})$.

## Real-world applications

- **Signal Processing / Error Correction:** Finding the total number of permutations a binary phase-shift keying (BPSK) signal could have flipped signs and still resulted in the same final integrated amplitude.

## Related algorithms in cOde(n)

- **[dp_17 - Partition Equal Subset Sum](dp_17_partition-equal-subset-sum.md)** — Another problem that requires mathematical reduction to Subset Sum.
- **[dp_06 - Subset Sum](dp_06_subset-sum.md)** — The foundational algorithm this problem reduces to.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
