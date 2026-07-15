# Profitable Schemes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 879 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/profitable-schemes/) |

## Problem Description
### Goal
A group has `n` members and a list of possible crimes. Crime $i$ produces `profit[i]` profit and requires `group[i]` members. A member who participates in one selected crime cannot participate in another, so a chosen subset cannot require more than `n` members in total.

A profitable scheme is any subset of crimes whose combined profit is at least `minProfit` and whose combined member requirement is at most `n`. Count the distinct qualifying crime subsets and return the result modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the available member count, where $1 \leq n \leq 100$.
- `minProfit`: the required profit threshold $P$, where $0 \leq P \leq 100$.
- `group`: an array of $m$ positive member requirements, where $1 \leq m \leq 100$ and $1 \leq \texttt{group[i]} \leq 100$.
- `profit`: an array of the same length, where $0 \leq \texttt{profit[i]} \leq 100$ gives the corresponding crime's profit.

**Return value**

Return the number of subsets whose total members are at most `n` and whose total profit is at least $P$, modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 5, minProfit = 3, group = [2,2], profit = [2,3]`
- Output: `2`

Crime `1` alone and the subset containing both crimes qualify.

**Example 2**

- Input: `n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]`
- Output: `7`

Every nonempty subset fits and reaches the profit threshold.

**Example 3**

- Input: `n = 1, minProfit = 0, group = [1], profit = [0]`
- Output: `2`

Both the empty subset and the subset containing the crime meet a zero threshold.

### Required Complexity
- **Time:** $O(mn(P+1))$
- **Space:** $O(n(P+1))$

<details>
<summary>Approach</summary>

#### General

**Track exact members but cap profit at the threshold**

Let `dp[used][earned]` count subsets of the crimes processed so far that use exactly `used` members. The profit coordinate records the exact total only below $P$; index $P$ represents every total of at least $P$. Initialize `dp[0][0] = 1` for the empty subset.

For a crime requiring `members` and producing `gain`, extend each state that still fits within `n`. Its destination is `used + members` and `min(P, earned + gain)`. Iterate `used` downward so a state created by the current crime cannot select that same crime again. Iterating the profit coordinate downward gives the same one-use protection within each member row and keeps the update conventional.

**Each subset follows one unique transition path**

For every processed crime, a subset either omits it and stays in its existing state or includes it and moves through exactly one update from the corresponding smaller subset. Thus no subset is lost or counted twice. Capping profit is safe because once a subset reaches $P$, only its member usage matters for all future feasibility. After all crimes, summing `dp[used][P]` over every allowed `used` counts precisely the profitable schemes.

#### Complexity detail

For each of the $m$ crimes, the algorithm scans at most $n+1$ member counts and $P+1$ capped profit states. Total time is $O(mn(P+1))$. The table contains $(n+1)(P+1)$ counters, so auxiliary space is $O(n(P+1))$.

#### Alternatives and edge cases

- **Enumerate all crime subsets:** Direct inclusion/exclusion is correct but takes $O(2^m)$ time.
- **Three-dimensional dynamic programming:** Adding a crime-index dimension makes the recurrence explicit but increases space to $O(mn(P+1))$.
- **Track uncapped total profit:** This preserves correctness but wastes states above the only threshold that affects the answer.
- **Zero minimum profit:** The empty subset is a valid scheme, as are any other subsets that satisfy the member limit.
- **Crime too large for the group:** It cannot be selected, but all states that omit it remain unchanged.
- **Zero-profit crime:** It can still double some scheme counts when enough members are available because selecting it creates a distinct subset.
- **Identical crime data:** Crimes remain distinct by index, so subsets choosing different equal-looking crimes are counted separately.
- **Modulo updates:** Apply the modulus while accumulating counts so fixed-width implementations do not overflow.

</details>
