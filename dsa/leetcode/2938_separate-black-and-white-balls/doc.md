# Separate Black and White Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2938 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/separate-black-and-white-balls/) |

## Problem Description

### Goal

There are $n$ balls arranged from left to right on a table. Their colors are
encoded by a 0-indexed binary string `s`: each `1` is a black ball and each
`0` is a white ball. The relative order among balls of the same color does
not affect the requested arrangement.

One step selects two adjacent balls and swaps their positions. Determine the
minimum number of such steps needed to place every white ball to the left of
every black ball. A string already having that form requires zero steps.

### Function Contract

**Inputs**

- `s`: a binary string encoding the balls from left to right

Let $n=\lvert\texttt{s}\rvert$. The contract guarantees
$1 \le n \le 10^5$, and every character of `s` is either `0` or `1`.

**Return value**

The minimum number of adjacent swaps needed to group all white balls on the
left and all black balls on the right.

### Examples

#### Example 1

- **Input:** `s = "101"`
- **Output:** `1`
- **Explanation:** Swap the first two balls to obtain `"011"`.

#### Example 2

- **Input:** `s = "100"`
- **Output:** `2`
- **Explanation:** Moving the leading black ball past both white balls produces
  `"001"` in two adjacent swaps.

#### Example 3

- **Input:** `s = "0111"`
- **Output:** `0`
- **Explanation:** Every white ball is already to the left of every black ball.
