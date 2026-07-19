# Validate IP Address

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 468 |
| Difficulty | Medium |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/validate-ip-address/) |

## Problem Description
### Goal
Given a candidate address string, classify it under exact IPv4 and full-form IPv6 syntax. IPv4 requires exactly four dot-separated decimal fields, each from `0` through `255`, containing digits only and no leading zero unless the field is exactly `"0"`.

IPv6 requires exactly eight colon-separated groups, each containing one through four hexadecimal digits `0-9`, `a-f`, or `A-F`; leading zeroes are allowed, but compressed empty groups are not. Return `"IPv4"`, `"IPv6"`, or `"Neither"`. Reject missing or extra fields, trailing separators, whitespace, signs, out-of-range IPv4 values, and characters outside the relevant alphabet.

### Function Contract
**Inputs**

- `queryIP`: the candidate address string

**Return value**

- `"IPv4"`, `"IPv6"`, or `"Neither"`

### Examples
**Example 1**

- Input: `queryIP = "172.16.254.1"`
- Output: `"IPv4"`

**Example 2**

- Input: `queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"`
- Output: `"IPv6"`

**Example 3**

- Input: `queryIP = "256.256.256.256"`
- Output: `"Neither"`
