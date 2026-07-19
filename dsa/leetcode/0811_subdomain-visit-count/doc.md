# Subdomain Visit Count

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 811 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subdomain-visit-count/) |

## Problem Description

### Goal

A count-paired domain such as `"9001 discuss.leetcode.com"` records visits to that complete domain. Every such visit also counts as an implicit visit to each parent subdomain, here `leetcode.com` and `com`.

Given all count-paired domains, sum the visits received by every full domain and parent subdomain. Return one string `"count domain"` for each accumulated domain, in any order. Counts from different input entries sharing a parent must be combined, and domain labels are separated at dots.

### Function Contract

**Inputs**

- `cpdomains`: count-paired domain strings in the form `"count domain"`.

**Return value**

- One `"total subdomain"` string for every distinct domain or parent subdomain. The entries may be returned in any order.

### Examples

**Example 1**

- Input: `cpdomains = ["9001 discuss.leetcode.com"]`
- Output: `["9001 discuss.leetcode.com","9001 leetcode.com","9001 com"]`
- Explanation: Every visit to the full domain also counts for both parent suffixes.

**Example 2**

- Input: `cpdomains = ["900 google.mail.com","50 yahoo.com","1 intel.mail.com","5 wiki.org"]`
- Output: `["900 google.mail.com","1 intel.mail.com","901 mail.com","50 yahoo.com","951 com","5 wiki.org","5 org"]`
- Explanation: Shared suffixes accumulate counts from all matching full domains.

**Example 3**

- Input: `cpdomains = ["10 a.com","5 b.a.com"]`
- Output: `["5 b.a.com","15 a.com","15 com"]`
- Explanation: The second entry contributes to both `a.com` and `com` in addition to its full name.
