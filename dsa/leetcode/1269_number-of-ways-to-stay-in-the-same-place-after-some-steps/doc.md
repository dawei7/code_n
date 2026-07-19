# Number of Ways to Stay in the Same Place After Some Steps

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1269 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/) |

## Problem Description

### Goal

A pointer starts at index $0$ of an array containing `arrLen` positions. One step may move the pointer one position left, move it one position right, or leave it at its current position. Every intermediate position must remain inside the array, so a move left from index $0$ or right from index `arrLen - 1` is not allowed.

Given `steps` and `arrLen`, count the distinct sequences of exactly `steps` moves that finish with the pointer back at index $0$. Because this count can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `steps`: the exact number of moves, with $1 \le \texttt{steps} \le 500$.
- `arrLen`: the number of array positions, with $1 \le \texttt{arrLen} \le 10^6$.

Let

$$
w = \min\left(\texttt{arrLen}, \left\lfloor\frac{\texttt{steps}}{2}\right\rfloor+1\right)
$$

be the number of positions that can still participate in a walk returning to index $0$.

**Return value**

- Return the number of valid move sequences that end at index $0$ after exactly `steps` moves, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `steps = 3, arrLen = 2`
- Output: `4`

**Example 2**

- Input: `steps = 2, arrLen = 4`
- Output: `2`

**Example 3**

- Input: `steps = 4, arrLen = 2`
- Output: `8`
