# Coin Change (Count Ways)

| | |
|---|---|
| **ID** | `dp_30` |
| **Category** | dynamic_programming |
| **Complexity (required)** | $O(n * amount)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) |

## Problem statement

Given an integer array `coins` representing coins of different denominations, and an integer `amount` representing a total amount of money.
Return the **number of unique combinations** that make up that amount.
You may assume that you have an infinite number of each kind of coin.

**Input:** An array `coins` and an integer `amount`.
**Output:** An integer representing the total number of ways.

**Example:**
`amount = 5`, `coins = [1, 2, 5]`.
Combinations: `5`, `2+2+1`, `2+1+1+1`, `1+1+1+1+1`.
Output: `4`.

## When to use it

- Unlike the standard Coin Change problem (`dp_05`), which asks for the *minimum number of coins* (optimization), this asks for the *total number of ways* (combinatorics).
- It is a direct application of the **Unbounded Knapsack Problem**.

## Approach

We can use a 1D DP array.
Let `dp[j]` be the number of ways to make the amount `j`.

If we iterate through each coin denomination one by one, we can ask: "How many *additional* ways can I make the amount `j` if I include this current coin?"
The answer is: however many ways I could make the amount `j - coin`!

So, for each `coin`, we iterate through all amounts `j` from `coin` up to `amount`, and update:
`dp[j] = dp[j] + dp[j - coin]`

**Why iterate through coins in the outer loop, and amounts in the inner loop?**
Because we want **combinations**, not **permutations**. We treat `2+1` and `1+2` as the exact same way.
By strictly iterating through `coins` in the outer loop, we mathematically enforce an ordering (e.g., we only ever add `2`s after we are completely finished adding all the `1`s). This guarantees we never generate `1+2` and `2+1` separately!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_30: Coin Change (Count Ways).

dp[a] = number of ways to make a. For each coin c, walk
forward: dp[a] += dp[a - c].
"""


def solve(coins, n, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
```

</details>

## Walk-through

`amount = 5`, `coins = [1, 2, 5]`.
`dp = [1, 0, 0, 0, 0, 0]` (size 6).

**Coin = 1:**
- `j=1`: `dp[1] += dp[0]` -> `1`.
- `j=2`: `dp[2] += dp[1]` -> `1`.
- ... `dp` becomes `[1, 1, 1, 1, 1, 1]`. (1 way to make every amount using just 1s).

**Coin = 2:**
- `j=2`: `dp[2] += dp[0]` -> `1 + 1 = 2`.
- `j=3`: `dp[3] += dp[1]` -> `1 + 1 = 2`.
- `j=4`: `dp[4] += dp[2]` -> `1 + 2 = 3`.
- `j=5`: `dp[5] += dp[3]` -> `1 + 2 = 3`.
- `dp` becomes `[1, 1, 2, 2, 3, 3]`.

**Coin = 5:**
- `j=5`: `dp[5] += dp[0]` -> `3 + 1 = 4`.

Output: `dp[5] = 4`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n * amount)$ | $O(amount)$ |
| **Average** | $O(n * amount)$ | $O(amount)$ |
| **Worst** | $O(n * amount)$ | $O(amount)$ |

We iterate through n coins. For each coin, we iterate through up to `amount` values. Total time complexity is strictly $O(n x \text{amount})$.
Space complexity is $O(\text{amount})$ for the 1D DP array.

## Variants & optimizations

- **Count Permutations (Climbing Stairs):** What if we *did* care about the order? If `1+2` and `2+1` were considered two different ways? Simply **swap the nested loops!** Put the `amount` loop on the outside, and the `coins` loop on the inside. This allows any coin to be added at any time, generating all permutations! This is the exact logic behind `dp_02_climbing-stairs`.

## Real-world applications

- **Cash Register Software:** Determining if there is sufficient mathematical liquidity in a given currency denomination set to provide exact change for arbitrary transactions.

## Related algorithms in cOde(n)

- **[dp_05 - Coin Change](dp_05_coin-change.md)** — The optimization variant asking for the minimum coins.
- **[dp_03 - 0/1 Knapsack](dp_03_knapsack.md)** — The bounded variant where each item can only be used once (which uses backward inner-loop iteration instead of forward).

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
