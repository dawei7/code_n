# Number of Ways to Earn Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2585 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-earn-points/) |

## Problem Description

### Goal

A test contains several question types. For type `i`, `types[i] = [count_i, marks_i]` means that at most `count_i` questions of that type are available and each selected question contributes `marks_i` points.

Count the ways to select questions whose total score is exactly `target`. Questions belonging to the same type are indistinguishable, so only the number selected from that type matters. Different rows remain different types, even when they award the same number of marks. Return the count modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `target`: The exact positive score to obtain, with $1 \leq \texttt{target} \leq 1000$.
- `types`: A list of $n$ pairs `[count_i, marks_i]`, where $1 \leq n \leq 50$ and both values in every pair are between $1$ and $50$.

**Return value**

- The number of valid selections modulo $10^9 + 7$.

### Examples

#### Example 1

- **Input:** `target = 6, types = [[6,1],[3,2],[2,3]]`
- **Output:** `7`

#### Example 2

- **Input:** `target = 5, types = [[50,1],[50,2],[50,5]]`
- **Output:** `4`

#### Example 3

- **Input:** `target = 18, types = [[6,1],[3,2],[2,3]]`
- **Output:** `1`
