# Minimum ASCII Delete Sum for Two Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 712 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) |

## Problem Description
### Goal
Given two strings `s1` and `s2`, delete characters from either string until their remaining character sequences are equal. Every deletion costs the ASCII value of the character removed.

Return the lowest possible total ASCII sum of all deleted characters. Remaining characters keep their relative order, and the two final strings may be empty when that is optimal. The objective minimizes deletion cost rather than merely the number of deletions, so removing fewer high-valued characters may cost more than removing several lower-valued ones.

### Function Contract
**Inputs**

- `s1`: the first lowercase English string
- `s2`: the second lowercase English string

**Return value**

- The minimum possible total ASCII deletion cost

### Examples
**Example 1**

- Input: `s1 = "sea", s2 = "eat"`
- Output: `231`

**Example 2**

- Input: `s1 = "delete", s2 = "leet"`
- Output: `403`

**Example 3**

- Input: `s1 = "abc", s2 = "abc"`
- Output: `0`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(\min(m, n))$

<details>
<summary>Approach</summary>

#### General

**Define a prefix-equality cost**

Let a DP state represent the minimum cost to make prefixes of the two strings equal. An empty prefix can match a nonempty prefix only by deleting every character of the latter, which supplies the first row and column.

**Keep matching characters for free**

When the current characters are equal, an optimal solution can retain both, so the state takes the diagonal cost for the preceding prefixes.

**Choose one deletion when characters differ**

Unequal final characters cannot both remain. Delete the first string's character and add its ASCII value to the state above, or delete the second string's character and add its value to the state on the left. The cheaper choice is optimal because it accounts for both exhaustive possibilities.

**Compress the table to one row**

Use the shorter string for columns. Before overwriting `dp[j]`, save its old value as the next diagonal; `dp[j]` still represents the state above and the newly written `dp[j - 1]` represents the state on the left.

**Why the recurrence yields the global minimum**

Every solution for unequal trailing characters must make one of the two modeled deletions first. Matching trailing characters can be retained without cost and reduce to the diagonal prefixes. Since boundary states are exact and each state minimizes over all valid first decisions followed by optimal smaller states, induction proves the final value is the minimum deletion sum.

#### Complexity detail

The algorithm fills one state for each of the $m \cdot n$ character pairs, taking $O(mn)$ time. Its row has one entry per character of the shorter string, using $O(\min(m, n))$ extra space.

#### Alternatives and edge cases

- **Weighted common subsequence:** maximize the ASCII sum of a common subsequence, then subtract twice that kept weight from the sum of both strings; it has the same $O(mn)$ time bound.
- **Full two-dimensional table:** stores every prefix state and is easier to visualize, but uses $O(mn)$ space.
- **Unmemoized recursion:** branch on both possible deletions at every mismatch; it is correct but exponential in the worst case.
- Equal strings require no deletions and return `0`.
- If the strings share no character, every character from both must be deleted.
- Character weights matter: a common subsequence with fewer high-ASCII characters can be better than a longer low-weight alternative.

</details>
