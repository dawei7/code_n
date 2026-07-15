# Shortest Common Supersequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1092 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/shortest-common-supersequence/) |

## Problem Description

### Goal

Given two lowercase English strings `str1` and `str2`, find the shortest string that contains both inputs as subsequences. A string is a subsequence of another when deleting zero or more characters from the latter leaves the former, without changing the order of retained characters.

Return any shortest common supersequence. More than one string can have the minimum length, and no lexicographic tie-breaking rule is required; the result only needs to preserve both input sequences and be as short as possible.

### Function Contract

**Inputs**

- `str1`: a lowercase English string of length $m$, where $1 \le m \le 1000$.
- `str2`: a lowercase English string of length $n$, where $1 \le n \le 1000$.

**Return value**

- Any minimum-length string containing both `str1` and `str2` as subsequences.

### Examples

**Example 1**

- Input: `str1 = "abac"`, `str2 = "cab"`
- Output: `"cabac"`

Deleting the first `c` leaves `"abac"`, while deleting the final `"ac"` leaves `"cab"`.

**Example 2**

- Input: `str1 = "aaaaaaaa"`, `str2 = "aaaaaaaa"`
- Output: `"aaaaaaaa"`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Measure the maximum reusable backbone:** Build the longest-common-subsequence length table. `lcs[i][j]` records the greatest number of characters that prefixes `str1[:i]` and `str2[:j]` can share in order. Equal final characters extend the diagonal state; unequal characters take the better state after dropping one final character.

**Reconstruct the supersequence backward:** Start at `(m, n)`. When the current characters match, append that character once and move diagonally. Otherwise, move toward a neighboring state with the larger LCS length and append the character removed from the other string. Either direction is valid when the lengths tie.

**Include unmatched prefixes:** Once one index reaches zero, append the other string's remaining prefix. Reverse the collected characters because reconstruction proceeded from the end.

Every move appends the character needed to preserve whichever input index it decreases, and a diagonal move shares one matching character between both subsequences. Thus the result contains both inputs. It shares exactly an LCS of length $L$, so its length is $m+n-L$. No common supersequence can be shorter because sharing more than $L$ ordered characters would imply a longer common subsequence.

#### Complexity detail

The table has $(m+1)(n+1)$ states and each takes constant time, giving $O(mn)$ time and space. Backtracking adds $O(m+n)$ time and output storage, which does not exceed the table bounds for non-empty inputs.

#### Alternatives and edge cases

- **Store a complete string per DP state:** It is correct but repeatedly copies growing strings, adding a factor proportional to output length in time and space.
- **Compute an LCS string first:** Merge unmatched input segments around that LCS. It has the same asymptotic bounds but requires a second traversal through the inputs.
- **Greedy character matching:** A locally early match may reduce future overlap and does not guarantee minimum length.
- **Identical strings:** Return either input unchanged.
- **No common character:** Every shortest result has length $m+n$ and interleaves both strings.
- **One input already a subsequence:** Return the containing string.
- **Multiple optima:** Any minimum-length answer preserving both subsequences is valid.

</details>
