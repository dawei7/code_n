# Subset Sum

| | |
|---|---|
| **ID** | `dp_06` |
| **Category** | dynamic |
| **Complexity (required)** | O(n²) |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Subset sum problem](https://en.wikipedia.org/wiki/Subset_sum_problem) |

## Problem statement

Given a set of non-negative integers `nums` and a target
`target`, determine whether there is a **subset** of `nums`
that sums exactly to `target`. (Each element can be used at
most once.)

**Input:** an array `nums` and a target sum `target`.
**Output:** `True` if some subset sums to `target`, else `False`.

**Example:**

| nums | target | Answer | Subset |
|---|---|---|---|
| `[3, 34, 4, 12, 5, 2]` | 9 | True | `{4, 5}` or `{3, 2, 4}` |
| `[3, 34, 4, 12, 5, 2]` | 30 | False | — |
| `[1, 5, 11, 5]` | 11 | True | `{11}` |
| `[1, 2, 3]` | 7 | True | `{1, 2, 4}` (no 4) — wait, `{1, 3, 3}` — actually no. The answer is False; 1+2+3=6 ≠ 7. |

## When to use it

- The decision-version of 0/1 knapsack. Foundation for
  "**partition**" problems (`dp_17`), the **Merkle-Hellman**
  cryptosystem, and many interview sub-problems.
- Whenever the question is "**can I pick a subset that
  exactly equals X?**", this is the shape.

## Approach

Let `dp[i][t]` = can the first `i` elements form a subset that
sums to `t`?

**Recurrence** (consider element `nums[i-1]`):
- **Skip it:** `dp[i][t] = dp[i-1][t]`.
- **Take it** (if `nums[i-1] <= t`): `dp[i][t] = dp[i-1][t - nums[i-1]]`.
- Either: `dp[i][t] = dp[i-1][t] OR dp[i-1][t - nums[i-1]]`.

**Base case:** `dp[0][0] = True` (empty set sums to 0).
`dp[0][t] = False` for `t > 0`.

**Answer:** `dp[n][target]`.

**Space optimization:** roll the 2D table into a 1D `bool`
array, iterated **right-to-left** so we don't overwrite the
row we're still using:

```
dp[0] = True
for x in nums:
    for t from target down to x:
        dp[t] = dp[t] or dp[t - x]
return dp[target]
```

## Algorithm (pseudocode)

```
subset_sum(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for t from target down to x:
            if dp[t - x]:
                dp[t] = True
    return dp[target]
```

## Walk-through

`nums = [3, 1, 4, 1]`, `target = 5`. Answer: True (`{1, 4}`).

`dp = [T, F, F, F, F, F]`.

**x = 3:**

| t | dp[t] before | candidate (dp[t-3]) | dp[t] after |
|---:|---:|---:|---:|
| 5 | F | dp[2]=F | F |
| 4 | F | dp[1]=F | F |
| 3 | F | dp[0]=T | **T** |

`dp = [T, F, F, T, F, F]`.

**x = 1:**

| t | dp[t] before | candidate (dp[t-1]) | dp[t] after |
|---:|---:|---:|---:|
| 5 | F | dp[4]=F | F |
| 4 | F | dp[3]=T | **T** |
| 3 | T | dp[2]=F | T |
| 2 | F | dp[1]=F | F |
| 1 | F | dp[0]=T | **T** |

`dp = [T, T, F, T, T, F]`.

**x = 4:**

| t | dp[t] before | candidate (dp[t-4]) | dp[t] after |
|---:|---:|---:|---:|
| 5 | F | dp[1]=T | **T** |
| 4 | T | dp[0]=T | T |

`dp = [T, T, F, T, T, T]`.

**x = 1:**

| t | dp[t] before | candidate (dp[t-1]) | dp[t] after |
|---:|---:|---:|---:|
| 5 | T | dp[4]=T | T |
| 4 | T | dp[3]=T | T |

`dp[5] = T`. Answer: True. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(n·target) | O(target) |
| **Average** | O(n·target) | O(target) |
| **Worst** | O(n·target) | O(target) |

Pseudo-polynomial in `target` (same caveat as 0/1 knapsack).
For very large `target`, exact solution is exponential.

## Variants & optimizations

- **Count the subsets** — change `dp[t] = dp[t] or dp[t - x]`
  to `dp[t] = dp[t] + dp[t - x]`.
- **Find the actual subset** — keep a parallel `parent[t, i]`
  indicating whether `dp[t]` was set via skip or take; walk
  back to reconstruct the subset.
- **Partition Equal Subset Sum** (`dp_17`) — does there exist
  a subset summing to `total / 2`? Apply this DP with
  `target = total / 2`.
- **Minimum-subset-sum-difference** — minimize `|sum1 - sum2|`
  over a partition into two equal-ish subsets. Same DP,
  different objective (track achievable sums, find best).
- **Bounded subset sum** (each element at most `k` times) —
  use the binary-decomposition trick to convert to 0/1.
- **Multiple queries** — sort `nums` once, then for each
  query use a sorted-set based DP (meet-in-the-middle for
  `n > 30`).

## Real-world applications

- **Merkle-Hellman knapsack cryptosystem** — built on the
  hardness of subset sum. (Broken by lattice reduction, but
  historically important.)
- **Resource allocation** — "can we assign the available staff
  to cover exactly the required hours?"
- **Scheduling** — "is there a subset of jobs that fits in
  the day's capacity exactly?"
- **Combinatorial auctions** — "is there a subset of bids
  that exactly equals the seller's reserve?"
- **Portfolio rebalancing** — "can we pick a subset of
  positions that sums to the target notional?"

## Related algorithms in cOde(n)

- **[dp_03 — 0/1 Knapsack](dp_03_knapsack.md)** — bounded
  variant with two attributes (weight + value), maximize.
  (d=5/10, r=9/10)
- **[dp_17 — Partition Equal Subset Sum](dp_17_partition-equal-subset-sum.md)** —
  `dp_06` applied to `target = total/2`. (d=5/10, r=9/10)
- **[dp_05 — Coin Change](dp_05_coin-change.md)** — unbounded
  variant (each coin can be used many times). (d=5/10, r=9/10)
- **[dp_30 — Coin Change (Count Ways)](dp_30_coin-change-count-ways.md)** —
  unbounded, count solutions. (d=3/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
