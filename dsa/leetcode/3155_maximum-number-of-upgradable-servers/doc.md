# Maximum Number of Upgradable Servers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3155 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-upgradable-servers/) |

## Problem Description
### Goal
A company operates $n$ data centers and wants to upgrade as many of their existing servers as possible. For center $i$, `count[i]` is its number of servers, `upgrade[i]` is the cost to upgrade one server, `sell[i]` is the money received by selling one server, and `money[i]` is the cash initially available there.

Each server at a center can be used in at most one way: it may be upgraded, sold to finance other upgrades at that same center, or left unchanged. Funds cannot be transferred between data centers. Return the maximum number of servers that can be upgraded independently at every center.

### Function Contract
**Inputs**

- `count`: An array of $n$ positive integers, where `count[i]` is the number of servers at data center $i$.
- `upgrade`: An array of $n$ positive integers, where `upgrade[i]` is the cost to upgrade one server at center $i$.
- `sell`: An array of $n$ positive integers, where `sell[i]` is the income from selling one server at center $i$.
- `money`: An array of $n$ positive integers, where `money[i]` is the center's initial money.

All four arrays have the same length, with $1 \le n \le 10^5$. Every array value lies between $1$ and $10^5$, inclusive.

**Return value**

Return an array of length $n$ whose element at index $i$ is the maximum number of servers that data center $i$ can upgrade without using money or servers from another center.

### Examples
**Example 1**

- Input: `count = [4, 3]`, `upgrade = [3, 5]`, `sell = [4, 2]`, `money = [8, 9]`
- Output: `[3, 2]`
- Explanation: Each center sells one server. The first then has $12$ to upgrade three servers, while the second has $11$ to upgrade two.

**Example 2**

- Input: `count = [1]`, `upgrade = [2]`, `sell = [1]`, `money = [1]`
- Output: `[0]`
- Explanation: The only server cannot both be sold and upgraded, and the initial money is insufficient.

**Example 3**

- Input: `count = [2, 5, 3]`, `upgrade = [4, 9, 2]`, `sell = [1, 2, 4]`, `money = [10, 1, 1]`
- Output: `[2, 1, 2]`
- Explanation: The centers are optimized separately; their best choices sell zero, four, and one server respectively.
