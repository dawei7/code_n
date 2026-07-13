# Distinct Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 115 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distinct-subsequences/) |

## Problem Description
### Goal
Given two strings `s` and `t`, count the distinct subsequences of `s` that equal `t`. A subsequence is formed by deleting any number of characters from `s` while preserving the relative order of every character that remains; characters cannot be rearranged or reused.

Two results are distinct when they select different source indices, even if repeated characters make the resulting text look identical. Return the total number of valid index selections as an integer. Selecting no characters forms the empty target exactly once, while a nonempty target cannot be formed from an empty source or from a source with too few usable characters.

### Function Contract
**Inputs**

- `s`: the source string from which characters may be deleted
- `t`: the target string that selected characters must form

**Return value**

The number of source subsequences equal to `t`.

### Examples
**Example 1**

- Input: `s = "rabbbit", t = "rabbit"`
- Output: `3`

**Example 2**

- Input: `s = "babgbag", t = "bag"`
- Output: `5`

**Example 3**

- Input: `s = "", t = ""`
- Output: `1`

### Required Complexity

- **Time:** $O(nm)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Count index selections, not merely distinct resulting text**

Let `dp[j]` be the number of increasing source-index selections within the processed source prefix that spell `t[:j]`. Different index sets count separately even when repeated source characters make their selected text look identical.

Set `dp[0] = 1`: every source prefix has exactly one way to form the empty target—select no indices. All positive target lengths initially have zero ways before any source character is processed.

**Backward updates prevent one source position from being selected twice**

For current source character `char`, if `char = t[j - 1]`, add `dp[j - 1]` to `dp[j]`. Existing `dp[j]` counts subsequences that skip this source position; the added term counts those that use it as their final selected index.

Iterate `j` from right to left. Then `dp[j - 1]` still describes the source prefix before `char`. A forward update could first use `char` to increase `dp[j - 1]` and immediately reuse the same position to increase `dp[j]`.

**Every update partitions choices by use of the current index**

After processing `s[:i]`, each `dp[j]` equals the number of increasing index selections within that prefix spelling `t[:j]`.

**Trace repeated characters as different index choices**

In `rabbbit`, each of the three source `b` positions can participate in different index choices. Backward updates accumulate those choices without merging them merely because their resulting text is the same.

**Use-or-omit partitions the source index choices**

For target prefix `t[:j]`, every subsequence choice either omits the current source position, leaving its existing count unchanged, or uses that position as the final character. The second case is possible only on a character match and extends exactly one choice forming `t[:j-1]` from earlier positions.

The cases are disjoint because they differ on whether the current index is selected, and together exhaust all index sets. Backward target updates ensure the extending count still refers to the source prefix before the current character, so no position is reused.

#### Complexity detail

For source length `n`, each character examines at most `m = len(t)` target positions, giving $O(nm)$ time. The target-prefix table uses $O(m)$ space.

#### Alternatives and edge cases

- **Enumerate source subsequences:** explores exponentially many index sets.
- **Two-dimensional DP:** is correct in $O(nm)$ time but uses $O(nm)$ space.
- **Update target positions forward:** reuses one source character multiple times and overcounts.
- An empty target has one subsequence in every source. A nonempty target cannot be formed from an empty source or when `len(t) > len(s)`.
- Large answers may exceed narrow integer types; use the numeric width guaranteed by the platform language contract.

</details>
