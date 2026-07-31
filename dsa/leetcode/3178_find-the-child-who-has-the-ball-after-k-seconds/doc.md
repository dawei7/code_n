# Find the Child Who Has the Ball After K Seconds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3178 |
| Difficulty | Easy |
| Topics | Math, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/) |

## Problem Description
### Goal
There are $n$ children numbered from $0$ through $n-1$, standing from left to right in that order. Child $0$ initially holds a ball, and the first passes move toward the right.

After every second, the current holder passes the ball to the adjacent child in the active direction. Whenever the ball reaches either endpoint—child $0$ or child $n-1$—the passing direction reverses for the following movement. Return the number of the child who has received the ball after exactly $k$ seconds.

### Function Contract
**Inputs**

- `n`: The number of children in the line, numbered from $0$ to $n-1$.
- `k`: The positive number of one-second passes to perform.

The constraints are $2 \le n \le 50$ and $1 \le k \le 50$.

**Return value**

Return the index of the child holding the ball after $k$ seconds.

### Examples
**Example 1**

- Input: `n = 3, k = 5`
- Output: `1`

The positions are $0,1,2,1,0,1$, so child $1$ receives the fifth pass.

**Example 2**

- Input: `n = 5, k = 6`
- Output: `2`

After reaching child $4$ at second $4$, the ball moves back through children $3$ and $2$.

**Example 3**

- Input: `n = 4, k = 2`
- Output: `2`

The ball has not yet reached the right endpoint, so its first two positions are children $1$ and $2$.
