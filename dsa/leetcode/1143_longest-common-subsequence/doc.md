# Longest Common Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1143 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-common-subsequence/) |

## Problem Description

### Goal

A subsequence is formed from a string by deleting zero or more characters without changing the relative order of those that remain. For example, `"ace"` is a subsequence of `"abcde"`; the selected characters do not need to occupy adjacent positions.

Given lowercase strings `text1` and `text2`, return the length of their longest common subsequence—a string that is a subsequence of both inputs. The empty string is always common, so return `0` when the inputs share no nonempty subsequence.

### Function Contract

**Inputs**

- `text1`: a lowercase English string of length $m$, where $1 \le m \le 1000$.
- `text2`: a lowercase English string of length $n$, where $1 \le n \le 1000$.

**Return value**

The maximum possible length of a string obtainable as a subsequence of both `text1` and `text2`.

### Examples

**Example 1**

- Input: `text1 = "abcde", text2 = "ace"`
- Output: `3`
- Explanation: `"ace"` appears in order in both strings.

**Example 2**

- Input: `text1 = "abc", text2 = "abc"`
- Output: `3`

**Example 3**

- Input: `text1 = "abc", text2 = "def"`
- Output: `0`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(\min(m,n))$

<details>
<summary>Approach</summary>

#### General

**Define the prefix decision.** Let $D(i,j)$ denote the LCS length of the first $i$ characters of one string and the first $j$ characters of the other. An empty prefix has no nonempty subsequence, so row zero and column zero contain `0`.

**Handle matching and mismatching final characters.** If the two new final characters match, an optimal common subsequence can extend the best result for the two shorter prefixes, giving `previous[j - 1] + 1`. If they differ, an optimal subsequence must omit at least one of them, so take `max(previous[j], current[j - 1])`. These are exactly the two ways a common subsequence can relate to the latest prefix characters, which makes the recurrence exhaustive and correct by induction over prefix lengths.

**Retain only the preceding row.** Each state uses the current row's left neighbor and values from the immediately previous row. Keep `previous` and build a fresh `current` row for every character of the longer string. Put the shorter input on the column axis so both rows have $\min(m,n)+1$ entries. The final cell is the LCS length of the complete strings.

#### Complexity detail

The algorithm evaluates all $mn$ prefix pairs once, with constant work per pair, for $O(mn)$ time. Two rows of length $\min(m,n)+1$ use $O(\min(m,n))$ auxiliary space.

#### Alternatives and edge cases

- **Full two-dimensional table:** Storing every $D(i,j)$ state has the same $O(mn)$ time but uses $O(mn)$ space; it is useful when reconstructing an actual subsequence.
- **Memoized recursion with string slices:** The recurrence is correct, but allocating suffix slices for states adds avoidable copying and recursion overhead.
- **Naive recursion:** Branching on every mismatch without memoization repeats prefix states exponentially.
- **Substring confusion:** Matching characters may have gaps; requiring adjacency solves longest common substring instead.
- **No common character:** Every state remains zero and the answer is `0`.
- **Repeated characters:** Their occurrences cannot be reused or reordered; prefix indices enforce valid one-to-one order.

</details>
