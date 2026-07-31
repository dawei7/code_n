# Apply Bitwise Operations to Make Strings Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2546 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [apply-bitwise-operations-to-make-strings-equal](https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/) |

## Problem Description

### Goal

Two 0-indexed binary strings `s` and `target` have the same length $n$. An operation chooses two different indices `i` and `j` in `s` and updates both positions simultaneously, using their original bits: `s[i]` becomes the bitwise OR of the pair, while `s[j]` becomes their bitwise XOR.

Apply this operation any number of times, including zero times. Determine whether some sequence of choices can transform `s` into `target`, and return a Boolean result.

### Function Contract

**Inputs**

- `s`: The binary string that may be transformed.
- `target`: The desired binary string, with the same length as `s`.

The common length $n$ is between 2 and $10^5$, and both strings contain only `0` and `1`.

**Return value**

Return `true` if the allowed simultaneous updates can make `s` equal `target`; otherwise return `false`.

### Examples

**Example 1**

- Input: `s = "1010", target = "0110"`
- Output: `true`
- Explanation: The existing `1` bits allow operations to move, create, and remove additional `1` bits until the target pattern is reached.

**Example 2**

- Input: `s = "11", target = "00"`
- Output: `false`
- Explanation: An operation on a pair containing a `1` never produces two zeros, so the last `1` cannot be removed.
