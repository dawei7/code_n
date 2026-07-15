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

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Keep the domain unchanged.** Split each address once at `@`. The right-hand domain is copied exactly, including all of its periods and any allowed characters, because normalization rules apply only to the local name.

**Canonicalize the local name in rule order.** Discard the first `+` and everything following it from the local portion, then remove every `.` from what remains. Applying the operations in this order makes the ignored suffix irrelevant and produces one canonical local name for every set of equivalent spellings. Combine that local name with `@` and the original domain.

**Count canonical recipients with a set.** Insert each normalized address into a hash set. Equivalent inputs produce the same set entry, whereas a different normalized local name or a different domain remains distinct. The final set size is therefore exactly the number of recipients.

#### Complexity detail

Splitting and normalizing examines each of the $S$ input characters a constant number of times, for $O(S)$ time. In the worst case all normalized addresses are distinct and their stored text totals $O(S)$ space.

#### Alternatives and edge cases

- **Pairwise normalized comparison:** Store normalized strings in a list and compare each new address with all earlier recipients. It is correct but can become quadratic in the number and length of addresses.
- **Character-by-character parser:** Build the normalized local name while scanning until `@`, skipping periods and ignoring characters after `+`. This has the same asymptotic bounds and can avoid temporary substrings.
- **Periods in the domain:** They must be preserved; removing them would incorrectly merge different domains.
- **Multiple plus characters:** The first plus begins the ignored suffix, so later pluses have no additional effect.
- **No special characters:** The address is already canonical and is still inserted normally.

</details>
