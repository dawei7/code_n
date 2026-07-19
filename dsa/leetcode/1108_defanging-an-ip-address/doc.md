# Defanging an IP Address

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1108 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/defanging-an-ip-address/) |

## Problem Description

### Goal

You are given `address`, a valid IPv4 address written in its usual dotted-decimal form. The address contains four decimal octets separated by three period characters, such as `"1.1.1.1"` or `"255.100.50.0"`.

Return the defanged version of this IP address. Defanging replaces every period `"."` with the three-character text `"[.]"`; every digit and its position relative to the other digits remains unchanged. The returned value is a new string, not a parsed numeric address.

### Function Contract

**Inputs**

- `address`: a valid IPv4 address string of length $n$, where $7 \le n \le 15$.

**Return value**

- The string obtained by replacing each of the address's three `"."` separators with `"[.]"`.

### Examples

**Example 1**

- Input: `address = "1.1.1.1"`
- Output: `"1[.]1[.]1[.]1"`

**Example 2**

- Input: `address = "255.100.50.0"`
- Output: `"255[.]100[.]50[.]0"`
