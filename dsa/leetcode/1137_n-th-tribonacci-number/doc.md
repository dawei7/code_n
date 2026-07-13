# N-th Tribonacci Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1137 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [n-th-tribonacci-number](https://leetcode.com/problems/n-th-tribonacci-number/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/n-th-tribonacci-number/).

### Goal
The Tribonacci sequence Tn is defined as follows:
`T0 = 0`, `T1 = 1`, `T2 = 1`, and `Tn+3 = Tn + Tn+1 + Tn+2` for `n >= 0`.

Given `n`, return the value of `Tn`.

### Function Contract
**Inputs**

- `n`: int

**Return value**

int - n-th Tribonacci number

### Examples
**Example 1**

- Input: `n = 4`
- Output: `4`

**Example 2**

- Input: `n = 1`
- Output: `1`

**Example 3**

- Input: `n = 0`
- Output: `0`

---

## Solution
### Approach
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
