# Kids With the Greatest Number of Candies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1431 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) |

## Problem Description

### Goal

Each position in `candies` records how many candies one child currently has. For each child independently, imagine giving that child all `extra_candies` while every other child's count remains unchanged.

Return whether the chosen child would then have the greatest number of candies among all children. Tying the greatest existing count is sufficient, and the extra candies are reused hypothetically for each position rather than distributed across the children.

### Function Contract

**Inputs**

- `candies`: an integer array of length $n$, where $2 \le n \le 100$ and $1 \le \texttt{candies[i]} \le 100$.
- `extra_candies`: the number hypothetically given to one child, where $1 \le \texttt{extra_candies} \le 50$.

**Return value**

- A boolean array of length $n$ whose entry at index `i` is `true` exactly when `candies[i] + extra_candies` is at least the greatest original candy count.

### Examples

**Example 1**

- Input: `candies = [2,3,5,1,3], extra_candies = 3`
- Output: `[true,true,true,false,true]`

**Example 2**

- Input: `candies = [4,2,1,1,2], extra_candies = 1`
- Output: `[true,false,false,false,false]`

**Example 3**

- Input: `candies = [12,1,12], extra_candies = 10`
- Output: `[true,false,true]`
