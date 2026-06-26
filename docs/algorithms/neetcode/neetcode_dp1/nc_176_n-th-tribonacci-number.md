## Problem Description & Examples
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

## Underlying Base Algorithm(s)
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
