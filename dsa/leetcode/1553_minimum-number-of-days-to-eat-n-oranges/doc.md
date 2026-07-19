# Minimum Number of Days to Eat N Oranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1553 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/) |

## Problem Description
### Goal
You begin with `n` oranges. On each day, choose exactly one allowed action: eat one orange; if the current amount is divisible by two, eat half of the oranges; or, if it is divisible by three, eat two thirds of the oranges.

Return the minimum number of days required to eat every orange. Divisibility is tested against the number remaining at the start of that day, and even when both division actions are available, only one action may be taken that day.

### Function Contract
**Inputs**

- `n`: the initial number of oranges, where $1 \le n \le 2 \times 10^9$.

**Return value**

The minimum number of daily actions needed to reduce the number of remaining oranges to zero.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `4`
- Explanation: Eat one orange, then use the divisible-by-three action on nine, followed by the divisible-by-three action on three, and finally eat the last orange.

**Example 2**

- Input: `n = 6`
- Output: `3`
- Explanation: Eat three oranges by halving, then eat two thirds of the remaining three, then eat the last orange.

**Example 3**

- Input: `n = 1`
- Output: `1`
- Explanation: The only possible action eats the single orange.
