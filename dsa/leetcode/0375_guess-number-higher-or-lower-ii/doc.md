# Guess Number Higher or Lower II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 375 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) |

## Problem Description
### Goal
A hidden number lies in the inclusive range `1..n`. Each wrong guess `x` costs `x` dollars and reveals whether the target is lower or higher; correctly guessing the target ends the game without an additional wrong-guess cost.

Choose an adaptive strategy whose later guesses may depend on earlier responses. Return the minimum amount of money that guarantees finding the number in the worst case over every possible target. Minimizing the number of guesses alone is insufficient because guesses have different costs. For $n = 1$, no wrong guess is needed and the guaranteed cost is zero.

### Function Contract
**Inputs**

- `n`: the inclusive upper bound of the possible hidden numbers

**Return value**

- The minimum worst-case total cost of a strategy guaranteed to identify every target in `1..n`.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `16`

**Example 2**

- Input: `n = 1`
- Output: `0`

**Example 3**

- Input: `n = 2`
- Output: `1`

### Required Complexity

- **Time:** $O(n^3)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Define the cost of guaranteeing an interval**

Let `dp[left][right]` be the minimum money needed to guarantee the answer when the target is known to lie in the inclusive interval `[left,right]`. An empty or one-value interval costs zero because no wrong paid guess is necessary.

**Price each possible first guess by its worse branch**

If the first guess is `guess`, a wrong answer costs `guess`. The response then leaves either `[left, guess - 1]` or `[guess + 1, right]`. A guaranteed strategy must afford the more expensive of those two possibilities, so this first choice costs

`guess + max(dp[left][guess - 1], dp[guess + 1][right])`.

Take the minimum of this value over every possible first guess.

**Fill shorter intervals before longer ones**

Process interval lengths from two through `n`. Every transition reads only strictly shorter intervals, so their optimal costs are already known. The final answer is `dp[1][n]`.

**Why minimax matches the guarantee**

For any selected first guess, an adversarial hidden value can force the more expensive remaining side, making the transition's maximum a necessary cost. Conversely, after either response, following the stored optimal strategy for that subinterval succeeds within that same maximum. Minimizing over first guesses therefore gives both a lower bound no strategy can beat and a strategy that achieves it.

**Trace two possible values**

For interval `[1,2]`, guessing one costs one only if it is wrong; that wrong response identifies two immediately. Guessing two could cost two. The minimum guaranteed cost is therefore one.

#### Complexity detail

There are $O(n^2)$ intervals. Each tries up to $O(n)$ first guesses, for $O(n^3)$ time. The two-dimensional interval table stores $O(n^2)$ scalar costs.

#### Alternatives and edge cases

- **Recursive minimax without memoization:** repeats the same intervals exponentially many times.
- **Top-down memoization:** evaluates the same $O(n^2)$ states and $O(n)$ choices per state with recursion overhead.
- **Enumerate every hidden target for each pivot:** computes the same worst branch directly but adds another factor of `n`, reaching $O(n^4)$ time.
- Guessing the mathematical midpoint is not always cost-optimal because larger wrong guesses cost more.
- A single possible target requires zero guaranteed payment.
- The objective minimizes worst-case cost, not the expected cost for a probability distribution.
- The paid amount includes only wrong guesses; the final correct guess costs nothing.

</details>
