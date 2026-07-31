# Minimum Cost to Equalize Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3139 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-equalize-array/) |

## Problem Description
### Goal
You are given an integer array `nums` and two operation prices, `cost1` and `cost2`. You may apply either operation any number of times:

- choose one index and increase its element by $1$, paying `cost1`; or
- choose two distinct indices and increase both selected elements by $1$, paying `cost2`.

Only increments are allowed. Determine the minimum total cost needed to make every element of `nums` equal. Because that cost can be very large, return it modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `nums`: A nonempty list of positive integers.
- `cost1`: The positive cost of incrementing one element by $1$.
- `cost2`: The positive cost of incrementing two distinct elements by $1$ each.

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $1 \le n \le 10^5$, $1 \le \texttt{nums[i]} \le 10^6$, and $1 \le \texttt{cost1}, \texttt{cost2} \le 10^6$.

**Return value**

Return the minimum equalization cost modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `nums = [4, 1], cost1 = 5, cost2 = 2`
- Output: `15`
- Explanation: The second value needs three increments. A two-index operation cannot reduce the difference between two values, so three single increments cost $15$.

**Example 2**

- Input: `nums = [2, 3, 3, 3, 5], cost1 = 2, cost2 = 1`
- Output: `6`
- Explanation: Four two-index increments and one single increment can make every value $5$ for a total cost of $4 \cdot 1 + 1 \cdot 2 = 6$.

**Example 3**

- Input: `nums = [3, 5, 3], cost1 = 1, cost2 = 3`
- Output: `4`
- Explanation: A two-index increment costs more than two single increments, so raising both smaller values to $5$ with four single increments is optimal.
