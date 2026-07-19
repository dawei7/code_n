# Minimize Rounding Error to Meet Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1058 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, String, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimize-rounding-error-to-meet-target/) |

## Problem Description

### Goal

Given decimal strings `prices = [p1, p2, ..., pN]` and an integer `target`, round every price independently. The rounded value for each price must be either its floor or its ceiling, and all rounded values must sum to `target`.

If no selection of floor and ceiling operations reaches the target, return `"-1"`. Otherwise, minimize the total rounding error

$$
E=\sum_{i=1}^{N}\left\lvert R_i(p_i)-p_i\right\rvert,
$$

where every $R_i$ is the chosen floor or ceiling operation. Return the smallest error as a string containing exactly three digits after the decimal point.

### Function Contract

**Inputs**

- `prices`: an array of $N$ strings, where $1 \le N \le 500$. Each string represents a value in $[0.0,1000.0]$ and has exactly three decimal places.
- `target`: an integer satisfying $0 \le \texttt{target} \le 10^6$.
- Let $K=1000$ be the number of thousandths in one unit.

**Return value**

- The minimum total rounding error formatted to three decimal places, or `"-1"` when the rounded sum cannot equal `target`.

### Examples

**Example 1**

- Input: `prices = ["0.700", "2.800", "4.900"], target = 8`
- Output: `"1.000"`
- Explanation: Rounding down, up, and up gives error `0.700 + 0.200 + 0.100 = 1.000`.

**Example 2**

- Input: `prices = ["1.500", "2.500", "3.500"], target = 10`
- Output: `"-1"`
- Explanation: Even rounding every value up produces a sum below the target.

**Example 3**

- Input: `prices = ["1.500", "2.500", "3.500"], target = 9`
- Output: `"1.500"`
