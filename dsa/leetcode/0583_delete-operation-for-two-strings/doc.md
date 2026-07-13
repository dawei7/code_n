# Delete Operation for Two Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 583 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-operation-for-two-strings/) |

## Problem Description
### Goal
Given two strings `word1` and `word2`, make the strings the same using deletion steps. In one step, you may delete exactly one character from either string; remaining characters keep their relative order, and insertion, replacement, or reordering is not allowed.

Return the minimum number of steps required. Deletions may be split between the two strings in any way, and the common result may be empty when necessary, although retaining the longest possible shared subsequence minimizes the total number removed.

### Function Contract
**Inputs**

- `word1: str`: the first string
- `word2: str`: the second string

**Return value**

- The smallest number of deletions from both strings combined that leaves the same remaining string on each side

### Examples
**Example 1**

- Input: `word1 = "sea", word2 = "eat"`
- Output: `2`

**Example 2**

- Input: `word1 = "leetcode", word2 = "etco"`
- Output: `4`

**Example 3**

- Input: `word1 = "a", word2 = "b"`
- Output: `2`

### Required Complexity

- **Time:** $O(m n)$
- **Space:** $O(\min(m, n))$

<details>
<summary>Approach</summary>

#### General

**The surviving characters form a common subsequence**

Deleting characters preserves the relative order of everything left behind. Therefore, any string that both inputs can become through deletions must be a subsequence of each input.

**Keep the longest possible shared subsequence**

If a common subsequence has length `L`, producing it costs $m - L$ deletions from `word1` and $n - L$ from `word2`, for $m + n - 2L$ total. A longer common subsequence always saves two deletions, so the optimum keeps a longest common subsequence.

**Compute LCS with one rolling row**

Make the shorter string the dynamic-programming column dimension. For each character of the longer string, build a new row. Matching characters extend the diagonal value by one; different characters take the better LCS obtained by excluding either current character. Only the previous row and current row are needed.

**Why the deletion count is minimal**

The dynamic program returns the maximum length of any sequence that can survive in both strings. Deleting all other characters constructs equal strings using $m + n - 2L$ deletions, so that bound is attainable. Any solution with fewer deletions would leave a longer shared subsequence than the computed LCS, contradicting its maximality.

#### Complexity detail

For lengths `m` and `n`, every character pair is processed once, taking $O(m n)$ time. The two rows use $O(\min(m, n))$ space after placing the shorter string on the column axis.

#### Alternatives and edge cases

- **Direct deletion-distance dynamic programming:** store the minimum deletions for every prefix pair; it has the same $O(m n)$ time and can also be space optimized.
- **Full LCS table:** simplifies reconstruction but uses $O(m n)$ space when only the length is needed.
- **Naive recursive LCS:** is faithful to the recurrence but repeats overlapping prefix states and takes exponential time.
- **Identical strings:** require zero deletions.
- **No shared characters:** every character from both strings must be deleted.
- **Repeated characters:** positions and order matter; character frequencies alone are insufficient.
- **One-character strings:** need zero deletions when equal and two when different.
- **One string as a subsequence of the other:** delete only the extra characters from the longer string.

</details>
