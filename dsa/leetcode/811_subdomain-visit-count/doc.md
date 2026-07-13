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

### Required Complexity

- **Time:** $O(c)$
- **Space:** $O(c)$

<details>
<summary>Approach</summary>

#### General

**Extract the count and full domain**

Split each input once at the space, parse the visit count, and add it to a hash counter under the full domain.

**Walk through suffix boundaries**

After counting the current domain, find its first dot and discard the leading label. Count that suffix, then repeat until no dot remains. For `discuss.leetcode.com`, this visits exactly `discuss.leetcode.com`, `leetcode.com`, and `com`.

Every reported visit to a full domain is also a visit to each suffix beginning at a label boundary, and the loop adds its count to all and only those names. Summing contributions in the counter therefore yields the exact aggregate for every distinct subdomain. Formatting each counter entry produces the required result, with order intentionally irrelevant.

#### Complexity detail

Let `c` be the total number of characters across the input. Each domain has only the bounded label structure from the problem contract, so parsing its suffixes and hashing them takes $O(c)$ expected time overall. Stored distinct suffix strings and counts use $O(c)$ space.

#### Alternatives and edge cases

- **Split labels then join suffixes:** Build `labels[i:]` for every position; this is straightforward and has the same bound under the limited domain depth.
- **Sort all contributions:** Emit every `(subdomain, count)` pair, sort by subdomain, and combine adjacent matches; hashing avoids the $O(k \log k)$ ordering step.
- **Linear list aggregation:** Searching a growing result list for every suffix is correct but can take $O(k^2)$ comparisons for `k` distinct subdomains.
- **Repeated input domain:** Counts must add rather than overwrite.
- **Top-level domain:** With no dot, it contributes only to itself.
- **Shared parent:** Unrelated full domains may still aggregate under the same suffix.
- **Output order:** Do not rely on a particular hash-table traversal order.

</details>
