# Check If All 1's Are at Least Length K Places Away

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1437 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/) |

## Problem Description

### Goal

Given a binary array `nums`, determine whether every two entries equal to `1` are separated by at least `k` array positions. For ones at indices $i<j$, this means that the number of intervening positions, $j-i-1$, must be at least $k$.

Return `true` when the condition holds for the entire array. Arrays with fewer than two ones satisfy it automatically, and when $k=0$, adjacent ones are permitted because zero intervening positions are required.

### Function Contract

**Inputs**

- `nums`: a binary array of length $n$, where $1 \le n \le 10^5$.
- `k`: the required minimum number of positions between ones, where $0 \le k \le n$.

**Return value**

- `true` if every pair of ones is at least $k$ places apart; otherwise `false`.

### Examples

**Example 1**

- Input: `nums = [1,0,0,0,1,0,0,1], k = 2`
- Output: `true`

**Example 2**

- Input: `nums = [1,0,0,1,0,1], k = 2`
- Output: `false`

**Example 3**

- Input: `nums = [0,1,0,0,1], k = 1`
- Output: `true`
