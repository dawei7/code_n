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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Select a grammar from the delimiter**

An IPv4 candidate uses dots and an IPv6 candidate uses colons. Split on the relevant delimiter and require exactly four IPv4 fields or eight IPv6 fields. Splitting preserves empty fields, so leading, trailing, or doubled delimiters fail later checks.

**Validate every IPv4 decimal field**

Each field must contain one to three ASCII decimal digits, represent a value from 0 through 255, and have no leading zero unless it is exactly `"0"`. Signs, whitespace, letters, empty fields, and padded values are invalid.

**Validate every IPv6 hexadecimal field**

Each of eight fields must contain one to four characters drawn only from `0-9`, `a-f`, or `A-F`. Leading zeros are allowed. The shortened `::` notation is outside this problem's accepted full-form grammar because it creates empty fields and fewer than eight explicit groups.

**Return neither on mixed or malformed structure**

A string that does not satisfy every rule for its selected grammar is `"Neither"`. Numeric conversion alone is insufficient because permissive parsers may accept signs, whitespace, leading zeros, or compressed IPv6 forms that the contract rejects.

#### Complexity detail

Splitting and validating all fields scans `n` characters, giving $O(n)$ time. The split fields collectively store $O(n)$ characters or views, so auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Manual one-pass parser:** avoids split arrays and can use $O(1)$ auxiliary state, but delimiter and final-field handling are more error-prone.
- **Regular expressions:** can encode both grammars compactly, though the numeric IPv4 bound still needs careful expression or conversion.
- **System IP-address parser:** may accept compressed IPv6 or alternate IPv4 spellings not allowed by this challenge.
- **IPv4 leading zero:** `"01"` is invalid even though its numeric value is in range.
- **IPv4 bound:** `255` is valid and `256` is not.
- **IPv6 case:** uppercase and lowercase hexadecimal letters are both accepted.
- **Empty field or trailing delimiter:** fails the nonempty group rule.
- **Mixed delimiters and `::` compression:** return `"Neither"`.

</details>
