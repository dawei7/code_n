# Count of Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2719 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/count-of-integers/) |

## Problem Description

### Goal

Two positive integers, `num1` and `num2`, are supplied as decimal strings and define an inclusive interval. For any integer in that interval, its digit sum is the sum of the numerical values of all digits in its ordinary decimal representation.

Count the integers from `num1` through `num2` whose digit sum lies in the inclusive range from `min_sum` to `max_sum`. Because the interval can extend to $10^{22}$ and the number of qualifying integers can be very large, return the count modulo $10^9+7$.

### Function Contract

Let $L=\max(\lvert\texttt{num1}\rvert,\lvert\texttt{num2}\rvert)$ and $S=\texttt{max_sum}$.

**Inputs**

- `num1`: The lower interval endpoint as a decimal string, where $1 \le \texttt{num1} \le 10^{22}$.
- `num2`: The upper interval endpoint as a decimal string, where $\texttt{num1} \le \texttt{num2} \le 10^{22}$.
- `min_sum`: The inclusive minimum allowed digit sum, where $1 \le \texttt{min_sum} \le 400$.
- `max_sum`: The inclusive maximum allowed digit sum, where $\texttt{min_sum} \le \texttt{max_sum} \le 400$.

**Return value**

Return the number of integers in the inclusive interval whose digit sum is between `min_sum` and `max_sum`, modulo $10^9+7$.

### Examples

**Example 1**

- Input: `num1 = "1", num2 = "12", min_sum = 1, max_sum = 8`
- Output: `11`
- Explanation: Every integer in the interval except $9$ has a digit sum between $1$ and $8$.

**Example 2**

- Input: `num1 = "1", num2 = "5", min_sum = 1, max_sum = 5`
- Output: `5`
- Explanation: Each one-digit integer in the interval has an allowed digit sum.

**Example 3**

- Input: `num1 = "1", num2 = "100", min_sum = 1, max_sum = 1`
- Output: `3`
- Explanation: The qualifying integers are $1$, $10$, and $100$.
