# House Robber

| | |
|---|---|
| **ID** | `dp_11` |
| **Category** | dynamic |
| **Complexity (required)** | O(n) |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence) (same shape) |

## Problem statement

You are a robber planning a heist along a street. The street
has `n` houses in a row, each with some amount of money
`nums[i]`. Adjacent houses have connected security systems —
robbing two adjacent houses in the same night will trigger
the alarm. Maximize the total money you can steal without
robbing two adjacent houses.

**Input:** `nums = [a0, a1, ..., a(n-1)]`.
**Output:** the maximum total money.

**Example:**

| nums | Robbed | Max |
|---|---|---:|
| `[1, 2, 3, 1]` | 1+3 or 2+1 | **4** |
| `[2, 7, 9, 3, 1]` | 2+9+1 | **12** |
| `[2, 1, 1, 2]` | 2+1 (skip middle) or 1+2 | **4** |
| `[5]` | 5 | **5** |
| `[]` | (none) | **0** |

## When to use it

- The canonical "**rob-skip-decide**" 1D DP and one of the
  most-recognized interview warm-ups. The recurrence is
  intuitive: at each house, decide to skip it (keep the
  previous max) or take it (add to the max from two houses
  ago).
- Foundation for many **2-house-skip** DP variants: House
  Robber II (circular), House Robber III (tree), and the
  "delete-and-earn" problem (which reduces back to House
  Robber via bucket sort).

## Approach

Let `dp[i]` = the maximum money robbable considering only the
first `i+1` houses (houses `0..i`).

**Recurrence:** at house `i`, two options:
- **Skip it:** `dp[i] = dp[i-1]`.
- **Take it:** `dp[i] = nums[i] + dp[i-2]`. (You can't have
  robbed house `i-1`, so the previous take is at `i-2`.)
- Take the max: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.

**Base case:** `dp[0] = nums[0]` (only one house, take it).
`dp[1] = max(nums[0], nums[1])`.

**Space optimization:** `dp[i]` only depends on the last two
values. Roll with two variables: `prev` (= `dp[i-1]`) and
`prev2` (= `dp[i-2]`).

**Answer:** `dp[n-1]` (or `prev` at the end of the loop).

## Algorithm (pseudocode)

```
rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev2 = nums[0]                              # dp[0]
    prev = max(nums[0], nums[1])                 # dp[1]
    for i from 2 to len(nums) - 1:
        curr = max(prev, nums[i] + prev2)
        prev2 = prev
        prev = curr
    return prev
```

## Walk-through

`nums = [2, 7, 9, 3, 1]`. Answer: 12.

| i | nums[i] | prev2 | prev | candidate = prev | nums[i] + prev2 | curr = max |
|---:|---:|---:|---:|---:|---:|---:|
| init | — | 2 | 7 | — | — | — |
| 2 | 9 | 7 | 7 | 7 | 9 + 2 = 11 | **11** |
| 3 | 3 | 7 | 11 | 11 | 3 + 7 = 10 | **11** |
| 4 | 1 | 11 | 11 | 11 | 1 + 11 = 12 | **12** |

Returns 12. ✓ (Rob houses 0, 2, 4: 2 + 9 + 1 = 12.)

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(n) | O(1) — rolling |
| **Average** | O(n) | O(1) |
| **Worst** | O(n) | O(1) |

The 2D `dp` table version uses O(n) space, but the rolling
implementation is O(1). Both are O(n) time.

## Variants & optimizations

- **House Robber II (circular)** — houses are in a circle, so
  house `0` and house `n-1` are also adjacent. Solve the
  regular problem twice: once for `nums[0..n-2]`, once for
  `nums[1..n-1]`, take the max. (Not in cOde(n) directly.)
- **House Robber III (tree)** — houses are nodes in a binary
  tree, no two parent-child can be robbed. Recursion on
  subtrees; each node returns `(rob_this, dont_rob_this)`.
- **Delete and Earn** — given points you can take and adjacent
  points are forbidden, but the relation is value-based not
  position-based. Bucket sort by value, then run House Robber
  on the bucket array.
- **Maximum sum of non-adjacent elements** — exactly the same
  problem with different framing.

## Real-world applications

- **Job scheduling with conflicts** — pick a subset of jobs
  where no two adjacent (in some ordering) can be selected.
- **Subset selection with pairwise exclusions** — choose items
  from a list where some pairs are mutually exclusive.
- **Game theory** — many two-player game DP problems reduce
  to the same "decide or skip" recurrence.

## Related algorithms in cOde(n)

- **[dp_01 — Fibonacci](dp_01_fibonacci.md)** — same 2-variable
  rolling shape, addition instead of max. (d=5/10, r=9/10)
- **[dp_02 — Climbing Stairs](dp_02_climbing-stairs.md)** —
  the same shape with a + instead of max. (d=5/10, r=9/10)
- **[dp_18 — Max Product Subarray](dp_18_max-product-subarray.md)** —
  same 1D-decide-or-skip shape, but the DP state must track
  both min and max (because of negatives). (d=5/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
