# Count Numbers with Non-Decreasing Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3519 |
| Difficulty | Hard |
| Topics | Math, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/) |

## Problem Description
### Goal
Two decimal strings `l` and `r` describe the endpoints of an inclusive integer range, and `b` specifies a numeral base. For each integer in the range, consider its usual base-$b$ representation without leading zeros.

A representation is non-decreasing when every digit is at least the digit immediately before it while reading from most significant to least significant. Count the integers in $[l,r]$ whose base-$b$ digits satisfy that condition. Return the count modulo $10^9+7$; the endpoint strings themselves remain decimal regardless of `b`.

### Function Contract
**Inputs**

- `l`: The decimal representation of the inclusive lower endpoint, with no leading zeros.
- `r`: The decimal representation of the inclusive upper endpoint, with no leading zeros.
- `b`: The representation base, where $2 \le b \le 10$.

The endpoint lengths satisfy $1 \le \lvert l\rvert \le \lvert r\rvert \le 100$, and the value of `l` is at most the value of `r`.

**Return value**

Return the number of integers in the inclusive range whose canonical base-$b$ digits are non-decreasing, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `l = "23", r = "28", b = 8`
- Output: `3`
- Explanation: The decimal values become `27`, `30`, `31`, `32`, `33`, and `34` in base 8; only `27`, `33`, and `34` are non-decreasing.

**Example 2**

- Input: `l = "2", r = "7", b = 2`
- Output: `2`
- Explanation: Among binary `10`, `11`, `100`, `101`, `110`, and `111`, only `11` and `111` qualify.

**Example 3**

- Input: `l = "10", r = "12", b = 10`
- Output: `2`
- Explanation: `11` and `12` are non-decreasing, while `10` is not.
