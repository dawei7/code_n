# Number of Dice Rolls With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1155 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/) |

## Problem Description

### Goal

You have $n$ dice. Every die has $k$ faces numbered from $1$ through $k$, and one face-up number is produced by each roll.

Among the $k^n$ possible ordered roll outcomes, count how many have face-up numbers whose sum is exactly `target`. Outcomes that assign different values to individual dice are different ways, even when their totals agree. Because the count can be very large, return it modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `n`: The number of dice, with $1 \le n \le 30$.
- `k`: The number of faces on every die, with $1 \le k \le 30$; the available values are the integers from $1$ through $k$.
- `target`: The required sum, with $1 \le \texttt{target} \le 1000$.

**Return value**

- The number of ordered roll outcomes whose sum is exactly `target`, reduced modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `n = 1`, `k = 6`, `target = 3`
- Output: `1`

**Example 2**

- Input: `n = 2`, `k = 6`, `target = 7`
- Output: `6`

The six ordered outcomes are `(1, 6)`, `(2, 5)`, `(3, 4)`, `(4, 3)`, `(5, 2)`, and `(6, 1)`.

**Example 3**

- Input: `n = 30`, `k = 30`, `target = 500`
- Output: `222616187`

### Required Complexity

- **Time:** $O(n \cdot \texttt{target})$
- **Space:** $O(\texttt{target})$

<details>
<summary>Approach</summary>

#### General

**Build sums one die at a time.** Let `dp[s]` be the number of ways the dice processed so far can total `s`. Before any die is rolled, `dp[0] = 1` and every positive sum has zero ways. For a new die, the recurrence for total `s` is the sum of the previous values `dp[s - face]` over faces from $1$ through $k$. This considers every possible final die value exactly once, and removing that value leaves precisely an outcome represented by the previous row.

**Reuse a sliding range sum.** Computing each recurrence by looping over all $k$ faces would add a factor of $k$. As `s` increases, however, its contributing range changes from `dp[s - k]` through `dp[s - 1]` to the next adjacent range. Maintain a variable `window`: add `dp[s - 1]`, remove `dp[s - k - 1]` once that index exists, and assign the reduced window to `next_dp[s]`. Each sum is then updated in constant time.

Replacing `dp` only after the full next row is built prevents one die from being counted more than once in the same transition. By induction on the number of processed dice, every stored value counts exactly the ordered outcomes for its row and sum; after $n$ rows, `dp[target]` is therefore the requested count. A target below $n$ or above $n k$ is unreachable and can return zero immediately.

#### Complexity detail

For each of the $n$ dice, the algorithm scans at most `target` sum positions and performs constant work at each one. This gives $O(n \cdot \texttt{target})$ time. The current and next dynamic-programming rows each contain `target + 1` integers, so the auxiliary space is $O(\texttt{target})$. Modular reduction keeps intermediate counts bounded without changing any final residue.

#### Alternatives and edge cases

- **Three nested loops:** Summing all possible faces independently for every state is straightforward but costs $O(n \cdot k \cdot \texttt{target})$ time.
- **Top-down memoization:** Caching states avoids repeated subproblems, but each state still tries up to $k$ faces and recursion adds overhead.
- **Enumerate roll outcomes:** Exploring all $k^n$ sequences is exponential and becomes infeasible long before the maximum constraints.
- **Unreachable target:** The minimum possible sum is $n$ and the maximum is $n k$; values outside that interval have zero ways.
- **One-faced dice:** When $k = 1$, exactly one outcome exists and it succeeds only when `target == n`.
- **Modulo arithmetic:** Apply the modulus during every row update so large combinatorial counts never need to be retained exactly.

</details>
