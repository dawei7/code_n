# Number Of Rectangles That Can Form The Largest Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1725 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/) |

## Problem Description

### Goal

You are given an array `rectangles`, where `rectangles[i] = [l_i, w_i]` gives the length and width of the $i$-th rectangle. A rectangle may be cut into a square of side length $k$ whenever $k \le l_i$ and $k \le w_i$. Consequently, the largest square obtainable from that rectangle has side length $\min(l_i,w_i)$.

Let `maxLen` be the greatest square side length obtainable from any supplied rectangle. Return how many rectangles can produce a square whose side length is exactly `maxLen`. Each input pair contains two positive, unequal dimensions, although different rectangles may yield the same maximum square size.

### Function Contract

**Inputs**

- `rectangles`: an array of $n$ pairs `[l_i, w_i]`, where $1 \le n \le 1000$, each pair has exactly two entries, $1 \le l_i,w_i \le 10^9$, and $l_i \ne w_i$.

**Return value**

- Return the number of rectangles whose smaller dimension equals the largest smaller dimension in the array.

### Examples

**Example 1**

- Input: `rectangles = [[5,8],[3,9],[5,12],[16,5]]`
- Output: `3`
- Explanation: The largest square sides available from the four rectangles are `5`, `3`, `5`, and `5`, so three rectangles attain `maxLen = 5`.

**Example 2**

- Input: `rectangles = [[2,3],[3,7],[4,3],[3,7]]`
- Output: `3`
- Explanation: The obtainable maximum sides are `2`, `3`, `3`, and `3`.

**Example 3**

- Input: `rectangles = [[100,1]]`
- Output: `1`
- Explanation: With one rectangle, its smaller dimension necessarily determines `maxLen`.
