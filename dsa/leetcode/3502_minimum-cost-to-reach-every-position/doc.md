# Minimum Cost to Reach Every Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3502 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-reach-every-position/) |

## Problem Description

### Goal

There are $n+1$ people standing in a line at positions $0$ through $n$, and you begin at position $n$. For every person in front of you, `cost[i]` is the amount that person charges to swap positions with you. Whenever you swap with somebody ahead of your current position, you must pay that person's listed cost.

A person behind your current position may instead swap with you for free. For every target position $i$ from $0$ through $n-1$, determine the minimum total amount needed to reach exactly that position. Each target is considered independently from the original arrangement. Return all $n$ minimum costs in position order.

### Function Contract

**Inputs**

- `cost`: A list of $n$ positive integers; `cost[i]` is the price of swapping with the person initially at position $i$ while that person is in front of you.

The constraints are $1 \le n \le 100$ and $1 \le \texttt{cost[i]} \le 100$.

**Return value**

Return a length-$n$ list `answer` where `answer[i]` is the minimum total cost required to reach position $i$.

### Examples

#### Example 1

- **Input:** `cost = [5,3,4,1,3,2]`
- **Output:** `[5,3,3,1,1,1]`
- **Explanation:** Paying person $1$ reaches position $1$ and makes position $2$ reachable for free. Paying person $3$ similarly makes positions $3$, $4$, and $5$ reachable for cost $1$.

#### Example 2

- **Input:** `cost = [1,2,4,6,7]`
- **Output:** `[1,1,1,1,1]`
- **Explanation:** After paying person $0$, every later position is behind you and can be reached through a free swap.
