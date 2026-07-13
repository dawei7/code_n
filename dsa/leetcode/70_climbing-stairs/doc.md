# Climbing Stairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 70 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/climbing-stairs/) |

## Problem Description
### Goal
A staircase has `n` steps, and each move may climb either one step or two steps. Starting below the first step, form movement sequences whose step sizes total exactly `n` without passing the top.

Return the number of distinct valid sequences. Order matters: for a three-step staircase, $1 + 2$ and $2 + 1$ are different ways. The input lies from `1` through `45`, so every staircase has at least one route consisting entirely of one-step moves.

### Function Contract
**Inputs**

- `n`: the positive number of stairs, with $1 \le n \le 45$

**Return value**

The number of valid move sequences.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `2`

**Example 2**

- Input: `n = 3`
- Output: `3`

**Example 3**

- Input: `n = 5`
- Output: `8`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Partition climbs by their final move**

Every route to stair `i` ends with either a one-step move from $i - 1$ or a two-step move from $i - 2$. Removing that last move maps the routes bijectively to climbs of the corresponding smaller staircase. The two final-move classes are disjoint, so $\operatorname{ways}(i) = \operatorname{ways}(i - 1) + \operatorname{ways}(i - 2)$.

**The recurrence needs only two rolling counts**

Initialize the counts for stairs 1 and 2 as 1 and 2. Advance through higher stairs by replacing them with the next Fibonacci-style sum. No earlier table entries are needed.

**Shift the pair after forming the next count**

Before computing stair `i`, the two variables contain exactly $\operatorname{ways}(i - 2)$ and $\operatorname{ways}(i - 1)$. Their sum is therefore `ways(i)`, and shifting the pair preserves the invariant for the next iteration.

**Trace the Fibonacci-style sequence**

For $n = 5$, begin with counts 1 and 2. Subsequent sums are 3 for stair 3, 5 for stair 4, and 8 for stair 5.

**The final step partitions every climb bijectively**

Every climb to stair `i` ends with either one step or two. Removing that final move maps the first group bijectively to climbs reaching $i - 1$ and the second to climbs reaching $i - 2$; adding the corresponding move reverses each mapping.

The two groups are disjoint and exhaustive, so their counts add. Starting from the direct counts for the first stairs and repeating this partition computes every subsequent value exactly.

#### Complexity detail

The loop advances once per stair, giving $O(n)$ time. Two running counts use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Unmemoized recursion:** repeats the same stair counts exponentially many times.
- **Memoization or a DP array:** achieves $O(n)$ time but stores $O(n)$ values unnecessarily.
- **Closed-form Fibonacci arithmetic:** can be constant-time in a floating-point model but risks rounding and is less robust for exact integers.
- $n = 1$ and $n = 2$ return their base counts directly. The challenge starts at positive `n`; a generalized $n = 0$ convention should be defined explicitly.
- Matrix exponentiation can reduce time to $O(\log n)$, but it adds machinery unnecessary for $n \le 45$.

</details>
