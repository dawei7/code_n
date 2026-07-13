# Valid Perfect Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 367 |
| Difficulty | Easy |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-perfect-square/) |

## Problem Description
### Goal
Given a positive integer `num`, determine whether some integer `r` satisfies `r * r = num`. Such values are perfect squares, including `1`, while values strictly between consecutive integer squares are not.

Return `True` only for an exact square and `False` otherwise. Do not use a built-in square-root function or a floating-point approximation whose rounding could misclassify large inputs. The task asks only for the boolean result, not for `r`; use integer arithmetic that avoids overflow or controls it when comparing candidate squares.

### Function Contract
**Inputs**

- `num`: a positive integer

**Return value**

- `True` exactly when there is an integer `r` such that `r * r = num`; otherwise `False`.

### Examples
**Example 1**

- Input: `num = 16`
- Output: `True`

**Example 2**

- Input: `num = 14`
- Output: `False`

**Example 3**

- Input: `num = 1`
- Output: `True`

### Required Complexity

- **Time:** $O(\log num)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Search the monotone square function**

For non-negative integers, $r^{2}$ increases strictly as $r$ increases. That monotonicity allows binary search over candidate roots instead of testing them one by one. The value $1$ is handled directly; for larger inputs, any square root lies between $1$ and `floor(num / 2)`.

**Discard half of the candidates each step**

At each iteration, square the midpoint. Equality proves that `num` is a perfect square. If the square is smaller, every candidate at or below the midpoint is too small, so move the left boundary above it. If the square is larger, move the right boundary below it. When the interval becomes empty, every possible integer root has been excluded.

**Why termination proves the Boolean result**

The search interval initially contains every feasible root. Each comparison removes only candidates whose squares are all strictly on the wrong side of `num`, preserving any valid root in the remaining interval. Therefore finding equality is sufficient for `True`, while exhausting the interval proves that no integer root exists.

#### Complexity detail

The candidate interval is halved on every iteration, so the search performs $O(\log num)$ comparisons. It stores only interval boundaries, the midpoint, and its square, using $O(1)$ space.

#### Alternatives and edge cases

- **Newton iteration:** converges quickly to the integer square root and also uses constant space, but its update and stopping conditions are less direct.
- **Subtract consecutive odd numbers:** uses the identity $1 + 3 + \ldots + (2r - 1) = r ^{2}$ but takes $O(\sqrt{num})$ iterations.
- **Linear candidate scan:** is correct but also requires $O(\sqrt{num})$ time.
- Input `1` is the smallest positive perfect square.
- Values immediately below or above a large square must return false.
- In fixed-width languages, comparing `mid <= num / mid` can avoid multiplication overflow; Python integers grow automatically.

</details>
