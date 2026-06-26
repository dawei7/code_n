# Egg Dropping (Mathematical $O(K log N)$)

| | |
|---|---|
| **ID** | `dp_22` |
| **Category** | dynamic |
| **Complexity (required)** | $O(K log N)$ Time, $O(K)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 4/10 |
| **LeetCode Equivalent** | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) |

## Problem statement

You are given `k` identical eggs and a building with `n` floors. Find the minimum number of drops you need to guarantee finding the critical breaking floor in the worst-case scenario.
The standard DP approach (`dp_16`) solves this in $O(K x N^2)$. You must solve this optimally, handling inputs where N = 10,000.

**Input:** Two integers `k` (eggs) and `n` (floors).
**Output:** An integer representing the minimum number of drops.

## When to use it

- To impress an interviewer by completely transforming the DP state of a classic problem to drastically reduce the asymptotic bounds.
- This is a masterclass in "State Inversion".

## Approach

**1. The Flaw of Standard DP:**
The standard approach asks: *"Given `e` eggs and `f` floors, what is the minimum drops `m` needed?"*
`dp[eggs][floors] = moves`.
This forces us to iterate through every possible floor `x` to minimize the worst-case, causing the $O(N^2)$ bottleneck.

**2. State Inversion:**
Let's flip the question backward:
*"Given `m` moves and `e` eggs, what is the MAXIMUM number of floors `f` we can possibly test?"*
Let `dp[m][e]` be the maximum floors we can test with `m` moves and `e` eggs.

**3. Find the Transition (The recurrence relation):**
Suppose we make 1 drop from some floor. There are two outcomes:
- **If it breaks:** We used 1 move, lost 1 egg. We now have `m-1` moves and `e-1` eggs. The maximum floors we can safely test *below* us is exactly `dp[m-1][e-1]`.
- **If it survives:** We used 1 move, kept the egg. We now have `m-1` moves and `e` eggs. The maximum floors we can safely test *above* us is exactly `dp[m-1][e]`.

Therefore, the total maximum floors we can test is the floors below us, PLUS the floors above us, PLUS the 1 floor we just dropped from!
`dp[m][e] = dp[m-1][e-1] + dp[m-1][e] + 1`

**4. The Strategy:**
We don't know the required moves `m` yet! So we just start at `m = 1` and keep incrementing `m` forever.
We calculate `dp[m][k]` for our total `k` eggs.
The exact moment that `dp[m][k] >= n`, it means we have finally reached enough moves to test all `n` floors. That `m` is our answer!

**5. Space Optimization:**
Notice `dp[m]` only relies on `dp[m-1]`. We can compress this to a 1D array of size `K+1`! Just like 0/1 Knapsack, we must iterate the eggs `e` backwards.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_22: Egg Dropping.

Return the minimum number of trials needed in the worst
case to find the critical floor. dp[e][f] = min trials for
e eggs and f floors. Drop from floor x -> 1 + worst(
dp[e-1][x-1], dp[e][f-x]).
"""


def solve(eggs, floors):
    if floors == 0:
        return 0
    if eggs == 1:
        return floors
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]
    for f in range(1, floors + 1):
        dp[1][f] = f
    for e in range(2, eggs + 1):
        for f in range(1, floors + 1):
            best = f
            for x in range(1, f + 1):
                worst = 1 + max(dp[e - 1][x - 1], dp[e][f - x])
                if worst < best:
                    best = worst
            dp[e][f] = best
    return dp[eggs][floors]
```

</details>

## Walk-through

`k = 2` eggs, `n = 6` floors.
`dp = [0, 0, 0]` (size 3).

1. **moves = 1:**
   - `e=2`: `dp[2] = dp[1] + dp[2] + 1 = 0 + 0 + 1 = 1`.
   - `e=1`: `dp[1] = dp[0] + dp[1] + 1 = 0 + 0 + 1 = 1`.
   - `dp = [0, 1, 1]`. (Max 1 floor tested). `1 < 6`. Loop again!
2. **moves = 2:**
   - `e=2`: `dp[2] = dp[1](old) + dp[2](old) + 1 = 1 + 1 + 1 = 3`.
   - `e=1`: `dp[1] = dp[0] + dp[1] + 1 = 0 + 1 + 1 = 2`.
   - `dp = [0, 2, 3]`. (Max 3 floors tested). `3 < 6`. Loop again!
3. **moves = 3:**
   - `e=2`: `dp[2] = dp[1](old) + dp[2](old) + 1 = 2 + 3 + 1 = 6`.
   - `e=1`: `dp[1] = dp[0] + dp[1] + 1 = 0 + 2 + 1 = 3`.
   - `dp = [0, 3, 6]`. `6 >= 6`! Break loop.

Output `moves = 3`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(K log N)$ | $O(K)$ |
| **Average** | $O(K log N)$ | $O(K)$ |
| **Worst** | $O(K log N)$ | $O(K)$ |

How many moves m are required? In the absolute worst case (k=1), m=N. However, for any K \ge 2, the DP array grows exponentially fast! The maximum moves required will never exceed roughly $O(\log N)$ or \sqrt{N}.
Inside the while loop, we run an inner loop of size K.
Thus, the time complexity is phenomenally fast: $O(K log N)$.
Space complexity is strictly $O(K)$ for the 1D array.

## Variants & optimizations

- **Pure Mathematical Combinatorics ($O(K)$):** The state transitions `dp[e] = dp[e-1] + dp[e] + 1` mathematically map perfectly to binomial coefficients. The value of `dp[m][k]` is exactly \sum_{i=1}^{k} \binom{m}{i}. You can binary search the value m from 1 to N, and for each m, calculate the sum of binomial coefficients in $O(K)$ time. Total time becomes $O(K log N)$ but with strictly $O(1)$ space!

## Real-world applications

- **Algorithm Design Theory:** This is less about practical application and entirely about mastering the art of "State Reversal" in Dynamic Programming to shatter computational bottlenecks.

## Related algorithms in cOde(n)

- **[dp_16 - Egg Dropping Puzzle](dp_16_egg-dropping.md)** — The classic $O(K x N^2)$ Min-Max approach that this algorithm optimizes.
- **[dp_03 - 0/1 Knapsack](dp_03_knapsack.md)** — Teaches the 1D backward-iteration space optimization used here.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
