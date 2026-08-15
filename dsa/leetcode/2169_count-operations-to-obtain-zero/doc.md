# Count Operations to Obtain Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2169 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-operations-to-obtain-zero/) |

## Problem Description

### Goal

Start with two non-negative integers `num1` and `num2`. While both are
positive, exactly one subtraction is required per operation:

- if `num1 >= num2`, replace `num1` with `num1 - num2`;
- otherwise, replace `num2` with `num2 - num1`.

The comparison is repeated using the updated values, so the process is fully
determined. Return how many operations occur before either integer becomes
zero. If an input is already zero, the process stops without performing an
operation.

### Function Contract

**Inputs**

- `num1`: an integer between $0$ and $10^5$, inclusive.
- `num2`: an integer between $0$ and $10^5$, inclusive.

For the complexity bound, define

$$
M=\max\{2,\texttt{num1},\texttt{num2}\}.
$$

**Return value**

Return the exact number of prescribed subtraction operations needed to make
`num1` or `num2` equal zero.

### Examples

#### Example 1

- **Input:** `num1 = 2, num2 = 3`
- **Output:** `3`

The states are `(2, 3)`, `(2, 1)`, `(1, 1)`, and `(0, 1)`, so three
operations are performed.

#### Example 2

- **Input:** `num1 = 10, num2 = 10`
- **Output:** `1`

Equality follows the `num1 >= num2` rule, and one subtraction changes the
first value to zero.

#### Example 3

- **Input:** `num1 = 0, num2 = 7`
- **Output:** `0`

The stopping condition already holds.
