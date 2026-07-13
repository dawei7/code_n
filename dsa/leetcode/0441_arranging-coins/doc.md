# Arranging Coins

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 441 |
| Difficulty | Easy |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/arranging-coins/) |

## Problem Description
### Goal
Given a positive number of coins `n`, build a staircase whose first row uses one coin, second row uses two, and row `r` uses exactly `r` coins. Rows must be completed in order from the first onward.

Return the greatest number of complete rows that can be built. Any remaining coins insufficient for the next full row are ignored, and no earlier row may be shortened to complete a later one. Equivalently, find the largest integer `k` whose triangular total $k \cdot (k + 1) / 2$ does not exceed `n`, using arithmetic that avoids overflow.

### Function Contract
**Inputs**

- `n`: the positive number of available coins

**Return value**

- Return the greatest integer `k` such that the first `k` rows require no more than `n` coins.

### Examples
**Example 1**

- Input: `n = 5`
- Output: `2`

**Example 2**

- Input: `n = 8`
- Output: `3`

**Example 3**

- Input: `n = 1`
- Output: `1`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Express complete rows with a triangular number**

The first `k` rows consume $1 + 2 + \ldots + k = k(k + 1) / 2$ coins. We need the largest integer `k` satisfying $k(k + 1) / 2 \le n$.

**Solve the quadratic boundary exactly**

Rearranging gives $k^{2} + k - 2n \le 0$. Its nonnegative root is $(-1 + \sqrt{1 + 8n}) / 2$, so the desired row count is the floor of that root. Use integer square root on $1 + 8n$ to avoid floating-point rounding, then compute $(\operatorname{isqrt}(1 + 8n) - 1) \mathbin{\operatorname{div}} 2$.

**Why flooring selects the maximum feasible row**

The triangular-number function is strictly increasing for nonnegative integers. Values at or below the positive root satisfy the coin inequality, while the next integer lies above the root and requires more than `n` coins. Flooring therefore returns exactly the last complete row.

#### Complexity detail

Under the canonical signed 32-bit input bound, integer square root and the fixed arithmetic expression take $O(1)$ time and $O(1)$ space.

#### Alternatives and edge cases

- **Binary search the row count:** test triangular numbers in $O(\log n)$ time and $O(1)$ space.
- **Subtract one row at a time:** takes $O(\sqrt{n})$ time because the number of complete rows is proportional to $\sqrt{n}$.
- **Floating-point quadratic formula:** works over the stated range but integer square root makes the boundary exact by construction.
- **Exact triangular number:** no coins remain, and the root is already an integer.
- **Incomplete next row:** leftover coins do not increase the answer.
- **One coin:** completes exactly the first row.

</details>
