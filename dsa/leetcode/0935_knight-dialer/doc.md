# Knight Dialer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 935 |
| Difficulty | Medium |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/knight-dialer/) |

## Problem Description

### Goal

A chess knight moves in an L shape: two cells along one axis and one cell along the other. Place such a knight on the standard numeric phone keypad, where it may occupy only the digit cells `0` through `9` and every move must be a valid knight jump between digit cells.

Given `n`, count the distinct phone numbers of length `n` that can be dialed. The knight may begin on any of the ten digits, which chooses the first digit, and then makes exactly `n - 1` valid jumps to select the remaining digits. Return the count modulo $10^9+7$ because it can be very large.

### Function Contract

**Inputs**

- `n`: the required phone-number length, where $1 \le n \le 5000$.

**Return value**

Return the number of length-$n$ digit sequences obtainable by choosing any starting digit and following valid knight moves, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `10`
- Explanation: Any digit may be the sole digit.

**Example 2**

- Input: `n = 2`
- Output: `20`

**Example 3**

- Input: `n = 3131`
- Output: `136006598`
