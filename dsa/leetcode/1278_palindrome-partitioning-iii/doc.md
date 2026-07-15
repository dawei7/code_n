# Palindrome Partitioning III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1278 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-partitioning-iii/) |

## Problem Description

### Goal

Given a lowercase string `s`, change as few of its characters as possible and then divide the resulting string into exactly `k` non-empty, contiguous, disjoint substrings. Every substring in the partition must be a palindrome.

A character change replaces the letter at one position with another lowercase English letter. Partition boundaries do not reorder or discard characters. Return the minimum number of changed positions needed to make some valid partition of exactly `k` palindromic pieces.

### Function Contract

**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \le n \le 100$.
- `k`: the exact number of non-empty substrings required, where $1 \le k \le n$.

**Return value**

- Return the minimum number of character replacements required across all `k` pieces.

### Examples

**Example 1**

- Input: `s = "abc", k = 2`
- Output: `1`

**Example 2**

- Input: `s = "aabbc", k = 3`
- Output: `0`

**Example 3**

- Input: `s = "leetcode", k = 8`
- Output: `0`

### Required Complexity

- **Time:** $O(kn^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Price every possible piece once**

For each substring `s[left:right + 1]`, compute the replacements needed to make it a palindrome. Its two outer characters require one change exactly when they differ; everything between them has already been priced by the shorter substring. Thus

$$
\operatorname{cost}(l,r)=\operatorname{cost}(l+1,r-1)+[s_l \ne s_r].
$$

Each mismatched mirrored pair needs at least one replacement, and changing either member makes that pair agree independently of all other pairs. The recurrence is therefore both necessary and sufficient.

**Choose partition boundaries with dynamic programming**

Let the previous dynamic-programming row store the minimum cost for splitting each prefix into one fewer piece. To form `parts` pieces ending at prefix length `end`, try every final-piece start `start` that leaves at least `parts - 1` characters for the earlier non-empty pieces. Combine the best earlier cost with `cost[start][end - 1]` and retain the minimum.

Every legal partition has one unique final boundary considered by this transition. Conversely, each transition joins a valid earlier partition to one non-empty palindromic piece. Induction on the number of pieces therefore shows that the value for the full string after `k` rows is the global minimum.

#### Complexity detail

The substring-cost table has $O(n^2)$ entries and takes $O(n^2)$ time to fill. Across $k$ partition rows, each of $O(n)$ prefix endpoints examines $O(n)$ possible starts, for $O(kn^2)$ total time. The cost table uses $O(n^2)$ space, while two partition rows use $O(n)$ additional space.

#### Alternatives and edge cases

- **Compute palindrome costs inside every transition:** It is correct but repeatedly scans the same substrings and can require $O(kn^3)$ time.
- **Top-down memoization:** Memoizing both substring costs and partition states has the same asymptotic bounds, but the iterative order avoids recursion overhead.
- **Enumerate all partitions:** Choosing all boundary combinations grows exponentially and is unnecessary because prefix states share the same optimal subproblems.
- **`k = 1`:** The answer is simply the mismatch count between mirrored pairs of the whole string.
- **`k = n`:** Every character forms a one-letter palindrome, so no changes are needed.
- **Already palindromic pieces:** Their precomputed cost is zero and the dynamic program preserves that possibility.

</details>
