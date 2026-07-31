# Collecting Chocolates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2735 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/collecting-chocolates/) |

## Problem Description

### Goal

There are $n$ chocolates with distinct types numbered from $0$ through $n-1$. Chocolate `i` initially has type $i$ and costs `nums[i]` to collect.

For a cost of `x`, one operation simultaneously changes every chocolate currently having type $i$ into type $(i+1)\bmod n$. You may perform the operation any number of times and may collect chocolates before or after operations. Determine the minimum total amount needed to collect at least one chocolate of every type, including both operation costs and purchase costs.

### Function Contract

**Inputs**

- `nums`: Purchase costs for the initial chocolates, with $1 \le n=\lvert\texttt{nums}\rvert \le 1000$ and $1 \le \texttt{nums}[i] \le 10^9$.
- `x`: The cost of one simultaneous type rotation, with $1 \le x \le 10^9$.

**Return value**

Return the minimum total cost to collect every chocolate type.

### Examples

**Example 1**

- Input: `nums = [20,1,15], x = 5`
- Output: `13`
- Explanation: Two rotations cost `10`, and the chocolate of cost `1` can supply each of the three types at different stages, for a purchase total of `3`.

**Example 2**

- Input: `nums = [1,2,3], x = 4`
- Output: `6`
- Explanation: Buying every type immediately costs `6`, and no rotation improves that total.

**Example 3**

- Input: `nums = [10,1,10,10], x = 1`
- Output: `7`
- Explanation: After considering three rotations, every type can be bought for `1`; purchases cost `4` and operations cost `3`.
