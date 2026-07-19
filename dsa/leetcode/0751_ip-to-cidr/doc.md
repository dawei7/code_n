# IP to CIDR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 751 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ip-to-cidr/) |

## Problem Description

### Goal

Given a starting IPv4 address `ip` and a positive count `n`, consider exactly `n` consecutive addresses beginning with `ip`. Represent that complete address range using CIDR blocks.

Return the smallest possible list of CIDR blocks whose union covers every requested address and no address before the start or after the end. Each block must be correctly aligned for its prefix length, and the returned blocks should follow address order without gaps or overlaps outside the target range.

### Function Contract

**Inputs**

- `ip`: the first IPv4 address in dotted-decimal notation.
- `n`: the positive number of consecutive addresses to cover.

**Return value**

- A minimum-length list of CIDR strings whose disjoint ranges cover exactly the requested addresses.

### Examples

**Example 1**

- Input: `ip = "255.0.0.7"`, `n = 10`
- Output: `["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]`
- Explanation: The middle block covers eight aligned addresses, while the two boundary addresses require singleton blocks.

**Example 2**

- Input: `ip = "0.0.0.0"`, `n = 4`
- Output: `["0.0.0.0/30"]`
- Explanation: The start is aligned to a four-address block, so one prefix covers the entire range.
