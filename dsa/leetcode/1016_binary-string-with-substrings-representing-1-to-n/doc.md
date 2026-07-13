# Binary String With Substrings Representing 1 To N

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1016 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [binary-string-with-substrings-representing-1-to-n](https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/).

### Goal
Given a binary string `s` and an integer `n`, decide whether every integer from `1` through `n` appears somewhere in `s` as its binary representation.

### Function Contract
**Inputs**

- `s`: Binary string.
- `n`: Positive integer upper bound.

**Return value**

Boolean indicating whether all binary strings for values in `[1, n]` occur as substrings of `s`.

### Examples
**Example 1**

- Input: `s = "0110", n = 3`
- Output: `true`

**Example 2**

- Input: `s = "0110", n = 4`
- Output: `false`

**Example 3**

- Input: `s = "1111000101", n = 5`
- Output: `true`

---

## Solution
### Approach
Scan all substrings whose length is at most the bit length of `n`. Convert each substring incrementally into an integer and record values between `1` and `n`. Stop extending a substring once its value exceeds `n`, because adding more bits can only keep it too large.

After the scan, every required number is represented exactly when the set contains `n` distinct values. This avoids iterating over huge missing ranges directly.

### Complexity Analysis
- **Time Complexity**: `O(m log n)`, where `m` is the length of `s`.
- **Space Complexity**: `O(min(n, m log n))` for the discovered values.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
