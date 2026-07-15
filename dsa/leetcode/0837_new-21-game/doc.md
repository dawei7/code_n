# New 21 Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 837 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Sliding Window, Probability and Statistics |
| Official Link | [LeetCode](https://leetcode.com/problems/new-21-game/) |

## Problem Description
### Goal
Alice begins with `0` points. While her total is less than `k`, she draws a number chosen uniformly from the integers in `[1, maxPts]` and adds it to her score. Draws are independent and every value in that range has equal probability.

Alice stops drawing as soon as her score is `k` or more. Return the probability that her final score is `n` or fewer. An answer within $10^{-5}$ of the true probability is accepted.

### Function Contract
**Inputs**

- `n`: the largest final score counted as successful.
- `k`: the score at which Alice stops drawing; $0 \leq k \leq n \leq 10^4$.
- `maxPts`: the inclusive upper bound on one draw, with $1 \leq \texttt{maxPts} \leq 10^4$.

**Return value**

Return the probability that Alice's score is at most `n` when the game stops.

### Examples
**Example 1**

- Input: `n = 10, k = 1, maxPts = 10`
- Output: `1.00000`

Alice draws once, and every possible result lies at or below `10`.

**Example 2**

- Input: `n = 6, k = 1, maxPts = 10`
- Output: `0.60000`

Exactly six of the ten equally likely one-draw results are successful.

**Example 3**

- Input: `n = 21, k = 17, maxPts = 10`
- Output: `0.73278`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Assign probability to each reachable score**

Let $p_x$ be the probability that Alice reaches exact score $x$. Initially $p_0=1$. To arrive at a positive score $x$, the preceding score must lie from $x-\texttt{maxPts}$ through $x-1$, and it must be below `k` because terminal scores never draw again. Since every draw has probability $1/\texttt{maxPts}$,

$$
p_x = \frac{1}{\texttt{maxPts}}
\sum_{j=\max(0,x-\texttt{maxPts})}^{\min(x-1,k-1)} p_j.
$$

**Maintain the recurrence as a sliding window**

Keep the sum of precisely those drawable predecessor probabilities. Dividing it by `maxPts` produces the next $p_x$. If $x<k$, add $p_x$ to the window because that score may lead to later draws; otherwise add it to the successful result when $x\leq n$. Remove $p_{x-\texttt{maxPts}}$ after it becomes too old, provided that score was below `k` and therefore had been included.

The window equals the recurrence's predecessor sum before every iteration: it starts with $p_0$, then each update adds the newly eligible drawable state and removes the state leaving the draw range. Thus every computed $p_x$ is exact. Terminal scores from `k` through `n` are disjoint successful outcomes, so their accumulated probability is the requested answer.

If `k` is zero, no draw occurs. Also, the largest possible terminal score is `k - 1 + maxPts`; when `n` reaches that value, every outcome succeeds and the answer is immediately one.

#### Complexity detail

Each score from `1` through `n` performs constant work, so the time is $O(n)$. The probability array has `n + 1` entries and uses $O(n)$ space; a circular buffer could reduce this to $O(\texttt{maxPts})$ while preserving the same time bound.

#### Alternatives and edge cases

- **Sum every predecessor range directly:** This follows the same recurrence but revisits up to `maxPts` earlier probabilities for each score, costing $O(n\cdot\texttt{maxPts})$ time.
- **Prefix sums of drawable states:** A cumulative array can answer each predecessor-range sum in constant time and also achieves $O(n)$ time, with careful exclusion of terminal states.
- **No draws:** When `k = 0`, Alice finishes at zero, and the probability is one because `k <= n`.
- **Guaranteed upper bound:** If `n >= k - 1 + maxPts`, no terminal score can exceed `n`.
- **Terminal states:** A probability at score `k` or above contributes to the answer but must never re-enter the window of states that can draw.
- **Floating-point drift:** Small subtraction error can occur in the moving sum, but double precision is comfortably within the required $10^{-5}$ tolerance.

</details>
