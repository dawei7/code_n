# Soup Servings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 808 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Probability and Statistics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/soup-servings/) |

## Problem Description

### Goal

Soups A and B each begin with `n` milliliters. On every turn, choose independently and uniformly among serving `(100, 0)`, `(75, 25)`, `(50, 50)`, or `(25, 75)` milliliters from `(A, B)`; if less than a requested amount remains, serve all of that soup.

The process stops immediately after a turn empties either soup. Return the probability that A becomes empty before B plus one half of the probability that both become empty on the same turn. There is no operation that serves `(0, 100)`.

### Function Contract

**Inputs**

- `n`: the nonnegative initial amount of each soup in milliliters.

**Return value**

- $\Pr(A\text{ empties first}) + 0.5 \cdot \Pr(A\text{ and }B\text{ empty together})$, within the required floating-point tolerance.

### Examples

**Example 1**

- Input: `n = 50`
- Output: `0.625`
- Explanation: Averaging the four first-serving outcomes gives the weighted probability `0.625`.

**Example 2**

- Input: `n = 100`
- Output: `0.71875`
- Explanation: Several serving rounds may occur; combining their equally likely branches gives `0.71875`.

**Example 3**

- Input: `n = 0`
- Output: `0.5`
- Explanation: Both soups are empty together before any serving, so the tie contributes one half.

### Required Complexity

- **Time:** $O(s^2)$
- **Space:** $O(s^2)$

<details>
<summary>Approach</summary>

#### General

**Scale away unused precision**

Every serving amount is a multiple of 25 milliliters. Replace `n` by $\left\lceil n / 25 \right\rceil$ units; the four operations then remove `(4,0)`, `(3,1)`, `(2,2)`, or `(1,3)` units from `(A,B)`. Rounding up is valid because attempting to remove more soup than remains simply empties it.

**Memoize the probability state**

Let `probability(a, b)` be the requested weighted probability from the remaining unit amounts. If both are nonpositive, return `0.5`; if only A is nonpositive, return `1`; if only B is nonpositive, return `0`. Otherwise, return one quarter of the four successor probabilities.

Each transition exactly conditions on one of the four equally likely operations. The base cases assign the required weight to every possible stopping outcome, so the recurrence's law-of-total-probability average is correct. Memoization evaluates each reachable `(a, b)` state once.

**Use convergence for very large inputs**

Soup A is never served less than B and is often served more, so the result approaches `1` rapidly. At $n = 4800$, the exact DP value already differs from `1` by about `0.00000501`; returning `1.0` at and above this cutoff stays within the accepted $10^{-5}$ tolerance and bounds the state space.

#### Complexity detail

Let $s = \min(\left\lceil n / 25 \right\rceil, 192)$. There are at most $O(s^2)$ pairs of remaining amounts, each with four constant-time transitions, so time and memo storage are $O(s^2)$. Recursion depth is $O(s)$ and is dominated by the memo table.

#### Alternatives and edge cases

- **Bottom-up table:** Fill probability states by increasing remaining amounts; it has the same $O(s^2)$ bounds but computes some unreachable states.
- **List-backed memoization:** Searching a per-row list for each cached state is correct, but it adds another factor of `s` to the work.
- **Uncached recursion:** Following all four branches directly repeats overlapping states and grows exponentially.
- **Exact simulation to arbitrary `n`:** It is unnecessary once convergence is inside the permitted error and can require an impractically large table.
- **Both soups empty:** Return `0.5`, not `1`, because ties receive half weight.
- **Only B empty:** Return `0` because A did not empty first.
- **Partial final serving:** A requested serving larger than the remaining amount empties that soup, which the nonpositive base checks model.
- **Zero input:** The initial state is already a tie.

</details>
