# Neighboring Bitwise XOR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2683 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation |
| Official Link | [neighboring-bitwise-xor](https://leetcode.com/problems/neighboring-bitwise-xor/) |

## Problem Description & Examples
### Goal
Given a 0-indexed binary array `derived` of length `n`, determine if there exists a binary array `original` of the same length `n` such that each element `derived[i]` is the result of the bitwise XOR operation between `original[i]` and `original[(i + 1) % n]`. The comparison is cyclic, meaning `original[n-1]` is XORed with `original[0]` to produce `derived[n-1]`. Return `true` if such an `original` array can be constructed, otherwise return `false`.

### Function Contract
**Inputs**

- `derived`: A list of integers, where each element is either 0 or 1. The length `n` of `derived` is between 1 and 10^5.

**Return value**

- `bool`: `True` if a valid `original` binary array exists, `False` otherwise.

### Examples
**Example 1**

- Input: `derived = [1, 1, 0]`
- Output: `True`
- Explanation: If `original = [0, 1, 0]`, then:
  - `original[0] XOR original[1] = 0 XOR 1 = 1` (matches `derived[0]`)
  - `original[1] XOR original[2] = 1 XOR 0 = 1` (matches `derived[1]`)
  - `original[2] XOR original[0] = 0 XOR 0 = 0` (matches `derived[2]`)
  All conditions are met.

**Example 2**

- Input: `derived = [1, 0]`
- Output: `False`
- Explanation: No `original` binary array of length 2 can satisfy the conditions.
  If `original = [0, 0]`: `0 XOR 0 = 0` (expected `1`), `0 XOR 0 = 0` (expected `0`). Fails.
  If `original = [0, 1]`: `0 XOR 1 = 1` (expected `1`), `1 XOR 0 = 1` (expected `0`). Fails.
  If `original = [1, 0]`: `1 XOR 0 = 1` (expected `1`), `0 XOR 1 = 1` (expected `0`). Fails.
  If `original = [1, 1]`: `1 XOR 1 = 0` (expected `1`), `1 XOR 1 = 0` (expected `0`). Fails.

**Example 3**

- Input: `derived = [0, 0, 0]`
- Output: `True`
- Explanation: If `original = [0, 0, 0]`, then all `derived[i]` will be `0 XOR 0 = 0`. This satisfies the conditions.

---

## Underlying Base Algorithm(s)
The core of the problem lies in understanding the properties of the XOR operation and its cyclic nature. The relationship `derived[i] = original[i] XOR original[(i + 1) % n]` can be rearranged to `original[(i + 1) % n] = original[i] XOR derived[i]`.

This allows us to construct the `original` array iteratively if we assume a value for `original[0]`.
Let's trace the values:
`original[1] = original[0] XOR derived[0]`
`original[2] = original[1] XOR derived[1] = (original[0] XOR derived[0]) XOR derived[1]`
`original[3] = original[2] XOR derived[2] = (original[0] XOR derived[0] XOR derived[1]) XOR derived[2]`
...
`original[i] = original[0] XOR (derived[0] XOR derived[1] XOR ... XOR derived[i-1])`

For the array to be valid, the final cyclic condition must hold: `derived[n-1] = original[n-1] XOR original[0]`.
Substituting the expression for `original[n-1]`:
`derived[n-1] = (original[0] XOR (derived[0] XOR derived[1] XOR ... XOR derived[n-2])) XOR original[0]`

Since `X XOR X = 0`, the `original[0]` terms cancel out:
`derived[n-1] = (derived[0] XOR derived[1] XOR ... XOR derived[n-2])`

Rearranging this equation, we get:
`derived[0] XOR derived[1] XOR ... XOR derived[n-2] XOR derived[n-1] = 0`

This means that for a valid `original` array to exist, the bitwise XOR sum of all elements in the `derived` array must be 0. If this condition holds, we can always construct a valid `original` array (e.g., by setting `original[0] = 0` and propagating the values). If the condition does not hold, no such `original` array can exist.

Therefore, the algorithm is simply to calculate the XOR sum of all elements in `derived` and check if it equals 0.

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the length of the `derived` array. This is because we iterate through the `derived` array exactly once to compute the XOR sum of its elements.
- **Space Complexity**: `O(1)`. We only use a single variable to store the running XOR sum, which requires constant extra space regardless of the input size.
