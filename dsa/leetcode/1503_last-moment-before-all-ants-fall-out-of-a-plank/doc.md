# Last Moment Before All Ants Fall Out of a Plank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1503 |
| Difficulty | Medium |
| Topics | Array, Brainteaser, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/) |

## Problem Description
### Goal

A wooden plank occupies the interval from position $0$ through position $n$. Every ant walks at one unit per second. Positions in `left` identify ants initially moving toward $0$, while positions in `right` identify ants initially moving toward $n$.

When two ants moving in opposite directions meet, both reverse direction immediately without spending additional time. An ant falls as soon as it reaches either end of the plank. Determine the time at which the final ant or ants fall. Initial positions are unique across both direction arrays, but either array may be empty.

### Function Contract
**Inputs**

Let $A=\lvert\texttt{left}\rvert+\lvert\texttt{right}\rvert$.

- `n`: the plank length, with $1 \le n \le 10^4$.
- `left`: distinct positions in $[0,n]$ for ants initially moving left.
- `right`: distinct positions in $[0,n]$ for ants initially moving right.
- A position appears in at most one array, and $1 \le A \le n+1$.

**Return value**

Return the integer time when the last ant reaches an end and falls immediately.

### Examples
**Example 1**

- Input: `n = 4, left = [4,3], right = [0,1]`
- Output: `4`
- Explanation: Although collisions exchange directions, some trajectory remains on the plank until time $4$.

**Example 2**

- Input: `n = 7, left = [], right = [0,1,2,3,4,5,6,7]`
- Output: `7`
- Explanation: The right-moving ant starting at $0$ crosses the full plank; the ant at $7$ falls immediately.

**Example 3**

- Input: `n = 7, left = [0,1,2,3,4,5,6,7], right = []`
- Output: `7`
- Explanation: The left-moving ant starting at $7$ needs seven seconds to reach $0$.
