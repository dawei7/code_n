# Coin Change

| | |
|---|---|
| **ID** | `dp_05` |
| **Category** | dynamic |
| **Complexity (required)** | $O(n²)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Change-making problem](https://en.wikipedia.org/wiki/Change-making_problem) |

## Problem statement

Given an array of coin denominations `coins` and a target
`amount`, find the **minimum number of coins** needed to make
up that amount. Each coin can be used **unlimited times**
(unbounded knapsack). If the amount can't be made, return
`-1` (or `+∞` in cOde(n)'s engine).

**Input:** `coins = [c1, c2, ..., cn]` (positive integers),
`amount` (non-negative integer).
**Output:** the minimum number of coins summing to `amount`,
or `-1` if impossible.

**Example:**

| coins | amount | Output | Explanation |
|---|---|---:|---|
| [1, 5, 10, 25] | 11 | 2 | 10 + 1 |
| [1, 5, 10, 25] | 30 | 2 | 25 + 5 |
| [2] | 3 | -1 | impossible |
| [1] | 0 | 0 | zero coins for zero amount |
| [1, 2, 5] | 11 | 3 | 5 + 5 + 1 |

## When to use it

- The canonical **unbounded-knapsack minimize-variants** problem
  in interviews. Slightly more common than the maximization
  variant because the answer (minimum count) is a small number
  that fits in an `int`.
- Whenever you have "**infinite supply of each item, minimize
  count**" with a one-dimensional resource constraint, this
  shape applies.

## Approach

Let `dp[a]` = the minimum number of coins to make amount `a`,
or `+∞` if impossible.

**Recurrence:** for the last coin of denomination `c`,
`dp[a] = 1 + dp[a - c]` (we used one `c` and now need to make
up the rest). Try every `c` and take the minimum:

```
dp[a] = min(1 + dp[a - c])   over all c in coins with c <= a
```

**Base case:** `dp[0] = 0` (zero coins for zero amount).
**Initialization:** `dp[a] = +∞` for `a > 0`.

**Iteration order:** `a` from `1` to `amount` (any order works
because all sub-problems `a - c` are smaller; no negative
edges).

**Return:** `dp[amount]` if finite, else `-1`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_05: Coin Change.

Minimum number of coins summing to the given amount.
"""


def solve(coins, amount):
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for v in range(1, amount + 1):
        for c in coins:
            if c <= v and dp[v - c] + 1 < dp[v]:
                dp[v] = dp[v - c] + 1
    return dp[amount] if dp[amount] != INF else -1
```

</details>

## Walk-through

`coins = [1, 5, 10, 25]`, `amount = 11`.

`dp = [0, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞, +∞]`.

| a | try c=1 | try c=5 | try c=10 | try c=25 | dp[a] |
|---:|---:|---:|---:|---:|---:|
| 1 | 1+dp[0]=1 | — | — | — | 1 |
| 2 | 1+dp[1]=2 | — | — | — | 2 |
| 3 | 1+dp[2]=3 | — | — | — | 3 |
| 4 | 1+dp[3]=4 | — | — | — | 4 |
| 5 | 1+dp[4]=5 | 1+dp[0]=1 | — | — | **1** |
| 6 | 1+dp[5]=2 | 1+dp[1]=2 | — | — | 2 |
| 7 | 1+dp[6]=3 | 1+dp[2]=3 | — | — | 3 |
| 8 | 1+dp[7]=4 | 1+dp[3]=4 | — | — | 4 |
| 9 | 1+dp[8]=5 | 1+dp[4]=5 | — | — | 5 |
| 10 | 1+dp[9]=6 | 1+dp[5]=2 | 1+dp[0]=1 | — | **1** |
| 11 | 1+dp[10]=2 | 1+dp[6]=3 | 1+dp[1]=2 | — | **2** |

Answer: `dp[11] = 2` (10 + 1). ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n · amount)$ | $O(amount)$ |
| **Average** | $O(n · amount)$ | $O(amount)$ |
| **Worst** | $O(n · amount)$ | $O(amount)$ |

Pseudo-polynomial in `amount`, just like 0/1 knapsack. For
very large `amount`, consider greedy if the coin system is
canonical (US coins are; arbitrary coin systems are not — see
the Wikipedia entry for the precise characterization).

## Variants & optimizations

- **Greedy for canonical coin systems** — if the denominations
  satisfy the canonical-coin property (every greedy choice is
  also the optimal choice for some amount), you can do
  $O(amount / max_denom)$ without a DP. US coins `[1, 5, 10, 25]`
  are canonical.
- **Count ways** — instead of minimum, count the number of
  distinct ways to make the amount. Initial `dp[0] = 1`,
  `dp[a] += dp[a - c]` for each coin. (See `dp_30`.)
- **Print the coins used** — keep a `parent[a] = c` table
  alongside `dp` and reconstruct by walking back from
  `parent[amount]`.
- **BFS** — view amounts as graph nodes, edges as "add a coin",
  do BFS from `0` until you hit `amount`. Often faster in
  practice when the answer is small.

## Real-world applications

- **Cash register software** — break a purchase total into
  bills/coins, minimizing the count (or matching a desired
  mix).
- **Vending machines** — the coin change problem in reverse
  (the machine *gives* change).
- **Currency arbitrage** — converting between currencies via
  a chain of conversions.
- **Subway fare systems** — find the minimum number of tickets
  to cover a set of trips.

## Related algorithms in cOde(n)

- **[dp_03 — 0/1 Knapsack](dp_03_knapsack.md)** — bounded
  variant (each item once). (d=5/10, r=9/10)
- **[dp_30 — Coin Change (Count Ways)](dp_30_coin-change-count-ways.md)** —
  unbounded, counting solutions instead of minimizing.
  (d=3/10, r=9/10)
- **[greedy_10 — Minimum Coins](greedy_10_minimum-coins.md)** —
  the greedy version; works for canonical coin systems.
  (d=3/10, r=6/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
