# Coin Change

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 322 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/coin-change/) |

## Problem Description
### Goal
Given positive integer coin denominations and a nonnegative target `amount`, choose any number of coins whose values sum exactly to the target. Each denomination has an unlimited supply, so it may be selected repeatedly and coin order does not create a different solution.

Return the minimum number of coins among all exact combinations. Return `-1` when no combination can form the amount, and return `0` for amount zero by choosing no coins. A greedy choice of the largest denomination is not guaranteed to be optimal for arbitrary coin systems. The function returns only the minimum count, not the selected denominations.

### Function Contract
**Inputs**

- `coins`: the available positive denominations
- `amount`: the target total

**Return value**

The minimum number of coins whose values sum to `amount`, or `-1` if no combination exists.

### Examples
**Example 1**

- Input: `coins = [1,2,5], amount = 11`
- Output: `3`

**Example 2**

- Input: `coins = [2], amount = 3`
- Output: `-1`

**Example 3**

- Input: `coins = [1], amount = 0`
- Output: `0`

### Required Complexity

- **Time:** $O(cA)$
- **Space:** $O(A)$

<details>
<summary>Approach</summary>

#### General

**Solve every smaller total once**

Let `dp[x]` be the minimum coins needed to form total `x`. The empty total needs no coins, so `dp[0] = 0`. Initialize every positive total as unreachable.

For each total from one through `amount`, consider which denomination could be its final coin. If coin `d` is no larger than the total and `total - d` is reachable, appending `d` creates a solution with `dp[total - d] + 1` coins. Take the minimum over all such final coins.

**The final coin partitions every possible solution**

Any nonempty combination forming `x` has some last coin `d`; removing it leaves a combination for $x - d$. An optimal combination must therefore consist of one coin plus an optimal combination for one of those predecessor totals. If the predecessor were not optimal, replacing it would improve the original combination.

The recurrence checks every denomination as that final coin, so it includes the final coin of an optimal solution and cannot return a larger count. Every finite value it creates corresponds to an actual predecessor combination plus one real coin, so it cannot return an impossible or too-small count either.

For `[1,3,4]` and amount six, the table finds `dp[3] = 1` and then `dp[6] = 2`. This is why denomination-greedy choice is insufficient: taking four first would use three coins (`4+1+1`) instead of two (`3+3`).

#### Complexity detail

Let `c` be the number of denominations and `A` the target amount. Each of the `A` positive totals checks every coin once, giving $O(cA)$ time. The table has $A + 1$ entries and uses $O(A)$ space.

#### Alternatives and edge cases

- **Always take the largest possible coin:** fails for noncanonical denomination systems such as `[1,3,4]` at amount six.
- **Enumerate coin combinations recursively:** repeats the same remaining amounts and can take exponential time without memoization.
- **Breadth-first search over reachable totals:** also finds the minimum coin count in $O(cA)$ time when totals are visited once.
- Amount zero returns zero regardless of the denominations. When every predecessor of the target is unreachable, the answer remains `-1`.

</details>
