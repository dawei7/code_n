# Diet Plan Performance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1176 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/diet-plan-performance/) |

## Problem Description

### Goal

A dieter consumes `calories[i]` calories on day $i$. For every consecutive sequence of exactly `k` days, let $T$ be the total calories consumed in that window. The dieter loses one point when $T<\texttt{lower}$, gains one point when $T>\texttt{upper}$, and receives no point change when $\texttt{lower}\leq T\leq\texttt{upper}$.

The score begins at zero. Evaluate every `k`-day window whose start is between `0` and `calories.length - k`, inclusive, and return the final score after all days. The result may be negative.

### Function Contract

**Inputs**

- `calories`: An array of daily calorie counts with $1 \leq \lvert\texttt{calories}\rvert \leq 10^5$ and $0 \leq \texttt{calories[i]} \leq 20000$.
- `k`: The exact window length, with $1 \leq \texttt{k} \leq \lvert\texttt{calories}\rvert$.
- `lower`: The inclusive lower boundary for a no-change window.
- `upper`: The inclusive upper boundary for a no-change window, with $0 \leq \texttt{lower} \leq \texttt{upper}$.
- Let $n=\lvert\texttt{calories}\rvert$.

**Return value**

- The sum of the point changes from all $n-k+1$ consecutive windows of length `k`.

### Examples

**Example 1**

- Input: `calories = [1,2,3,4,5]`, `k = 1`, `lower = 3`, `upper = 3`
- Output: `0`

The first two days lose one point each, the middle day changes nothing, and the last two days gain one point each.

**Example 2**

- Input: `calories = [3,2]`, `k = 2`, `lower = 0`, `upper = 1`
- Output: `1`

**Example 3**

- Input: `calories = [6,5,0,0]`, `k = 2`, `lower = 1`, `upper = 5`
- Output: `0`
