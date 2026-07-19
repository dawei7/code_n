# Max Difference You Can Get From Changing an Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1432 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/) |

## Problem Description

### Goal

Start with the positive integer `num`. One replacement operation chooses a decimal digit `x` and another digit `y`, then changes every occurrence of `x` in `num` to `y`. Apply this operation independently twice to produce integers `a` and `b`; the two operations may choose different digit pairs.

Neither result may have a leading zero or equal zero. The chosen digits may be equal, so an operation is allowed to leave the number unchanged. Return the greatest possible value of `a - b` over all valid choices.

### Function Contract

**Inputs**

- `num`: an integer satisfying $1 \le \texttt{num} \le 10^8$.
- Let $d$ be the number of decimal digits in `num`.

**Return value**

- The maximum difference between a valid independently maximized replacement result and a valid independently minimized replacement result.

### Examples

**Example 1**

- Input: `num = 555`
- Output: `888`

**Example 2**

- Input: `num = 9`
- Output: `8`

**Example 3**

- Input: `num = 123456`
- Output: `820000`
