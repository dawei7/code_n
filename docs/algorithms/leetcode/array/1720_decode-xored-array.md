# Decode XORed Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1720 |
| Difficulty | Easy |
| Topics | Array, Bit Manipulation |
| Official Link | [decode-xored-array](https://leetcode.com/problems/decode-xored-array/) |

## Problem Description & Examples
### Goal
An encoded array stores `arr[i] XOR arr[i + 1]` for each adjacent pair of an original array. Given the first original value, reconstruct the whole original array.

### Function Contract
**Inputs**

- `encoded`: a list of XOR values between adjacent original elements.
- `first`: the first value of the original array.

**Return value**

Return the decoded original array.

### Examples
**Example 1**

- Input: `encoded = [1,2,3], first = 1`
- Output: `[1,0,2,1]`

**Example 2**

- Input: `encoded = [6,2,7,3], first = 4`
- Output: `[4,2,0,7,4]`

**Example 3**

- Input: `encoded = [], first = 5`
- Output: `[5]`

---

## Underlying Base Algorithm(s)
Use the XOR identity `a XOR b = encoded[i]`, so `b = a XOR encoded[i]`. Start with `first`, then append `decoded[-1] XOR encoded[i]` for every encoded value.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` besides the output array
