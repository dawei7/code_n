# Unique Email Addresses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 929 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-email-addresses/) |

## Problem Description

### Goal

Every valid email address has a non-empty local name and a non-empty domain name separated by one `@` character. Besides lowercase English letters, the supplied addresses may contain `.` and `+` characters.

Periods in the local name are ignored when mail is delivered: for example, `"alice.z@leetcode.com"` and `"alicez@leetcode.com"` reach the same recipient. This rule does not apply to the domain name, where periods remain significant.

Within the local name, the first `+` and every character after it are also ignored. For example, `"m.y+name@email.com"` is delivered to `"my@email.com"`. The period and plus rules may both apply to one address, but neither rule changes its domain.

Given `emails`, where one message is sent to every listed address, return the number of different normalized addresses that actually receive at least one message.

### Function Contract

**Inputs**

- `emails`: a list of between $1$ and $100$ valid email strings, each of length at most $100$, with exactly one `@`, non-empty local and domain names, and a domain ending in `".com"`.

Let

$$
S = \sum_{e \in \texttt{emails}} \lvert e \rvert
$$

be the total number of characters across all input addresses.

**Return value**

Return the number of distinct recipient addresses after applying the local-name period and plus rules.

### Examples

**Example 1**

- Input: `emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]`
- Output: `2`
- Explanation: The messages reach `"testemail@leetcode.com"` and `"testemail@lee.tcode.com"`.

**Example 2**

- Input: `emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]`
- Output: `3`
