# Construct the Rectangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 492 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-the-rectangle/) |

## Problem Description
### Goal
Given the positive integer area of a rectangular web page, choose positive integer dimensions `L` and `W`. Their product must equal `area`, and the width may not exceed the length, so $L \ge W$.

Among every factor pair meeting those conditions, return `[L, W]` with the smallest possible difference $L - W$. The desired pair is therefore the one closest to a square, not necessarily the first factorization found from the largest length. A prime area returns `[area, 1]`, while a perfect square returns two equal dimensions.

### Function Contract
**Inputs**

- `area`: a positive integer rectangle area

**Return value**

- The closest valid factor pair as `[length, width]`

### Examples
**Example 1**

- Input: `area = 4`
- Output: `[2, 2]`

**Example 2**

- Input: `area = 37`
- Output: `[37, 1]`

**Example 3**

- Input: `area = 122122`
- Output: `[427, 286]`

### Required Complexity

- **Time:** $O(\sqrt{area})$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**The closest pair straddles the square root**

For `length >= width`, the width cannot exceed `sqrt(area)`. As a valid width grows toward the square root, its quotient moves toward it and the dimension difference shrinks.

**Search widths downward**

Start at `floor(sqrt(area))` and decrease until finding a divisor. Its quotient is automatically at least as large as the width.

**Why the first divisor is optimal**

The search's first divisor is the largest valid width not exceeding the square root. Every other factor pair uses a smaller width and larger length, so none can have a smaller difference.

#### Complexity detail

At most `floor(sqrt(area))` widths are tested, giving $O(\sqrt{area})$ time for prime areas. Only the current width and quotient are stored, so space is $O(1)$.

#### Alternatives and edge cases

- **Scan lengths upward from the square root:** is correct but may take $O(area)$ tests for a prime.
- **Enumerate all factor pairs:** continues after the optimum is already known.
- **Floating square root:** needs care near rounding boundaries; integer square root avoids them.
- **Perfect square:** returns equal dimensions immediately.
- **Prime area:** returns `[area, 1]`.
- **Area one:** returns `[1, 1]`.
- **Dimension order:** place the quotient first.

</details>
