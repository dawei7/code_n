# Interleaving String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 97 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/interleaving-string/) |

## Problem Description
### Goal
You are given source strings `s1` and `s2` and a proposed result `s3`. An interleaving divides each source into a sequence of nonempty substrings, with the two sequence lengths differing by at most one, then alternates whole substrings from the two sources starting with either one.

Determine whether some such alternating sequence produces `s3` exactly. The substrings from each source must remain in their original left-to-right order and together consume every character of both inputs. Empty sources follow the same order-preservation rule, and equal characters may allow several valid choices of substring boundaries.

### Function Contract
**Inputs**

- `s1`: the first source string
- `s2`: the second source string
- `s3`: the proposed interleaving

**Return value**

`True` exactly when `s3` is a valid interleaving of `s1` and `s2`.

### Examples
**Example 1**

- Input: `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"`
- Output: `True`

**Example 2**

- Input: `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"`
- Output: `False`

**Example 3**

- Input: `s1 = "", s2 = "", s3 = ""`
- Output: `True`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(\min(m, n))$

<details>
<summary>Approach</summary>

#### General

**Length equality is a necessary conservation check**

An interleaving uses every source character exactly once and introduces none, so `len(s1) + len(s2) = len(s3)` is necessary. Rejecting a mismatch also guarantees that DP state $(i,j)$ always refers to the well-defined target position $i + j - 1$ when a character is consumed.

**A state records how many characters have been consumed from each source**

Let `reachable(i,j)` mean that `s1[:i]` and `s2[:j]` can form exactly `s3[:i+j]`. The final target character in this prefix must come from one of two places:

- from `s1[i - 1]` if $\operatorname{reachable}(i - 1,j)$ and that character matches `s3[i+j-1]`;
- from `s2[j - 1]` if $\operatorname{reachable}(i,j - 1)$ and that character matches the same target position.

Use logical OR because when source characters are equal, both histories may be viable and a greedy commitment to one can fail later.

**One row retains both source-choice predecessors**

Store `dp[j]` for a fixed `i`. Before update, `dp[j]` still represents the state above, using one fewer `s1` character. After updating column $j - 1$, that left entry represents the current row using one fewer `s2` character. Fill left to right so both predecessors are available.

Place the shorter source on the column axis to minimize the rolling array. Interleaving is symmetric in the two sources, so swapping their DP roles does not change the answer.

**Initialize the axes where only one source is available**

Start with `dp[0] = True` for three empty prefixes. Along the initial row, each state can only extend from `s2`; at column zero of later rows, each state can only extend from `s1`. After updating general column `j`, `dp[j]` is true exactly when the first $i + j$ target characters can be formed from the corresponding source prefixes without changing either source order.

**Trace an ambiguous equal-character choice**

In `s1 = "aa"`, `s2 = "ab"`, and `s3 = "aaba"`, an early target `a` may match either source. The DP retains both reachable prefix pairs rather than selecting one. Later target characters eliminate incompatible histories while preserving the path that consumes all characters in order.

**The final source character partitions interleaving prefixes**

Any nonempty interleaving prefix ends by consuming either the next character from `s1` or the next from `s2`; source order permits no third possibility. Removing that final character exposes the corresponding shorter prefix pair, which must itself be reachable.

The transition tests exactly those two cases with character equality. Starting from the three empty prefixes, the DP therefore marks all and only reachable prefix pairs, including the complete strings.

#### Complexity detail

The algorithm visits each of the $(m + 1)(n + 1)$ prefix pairs once, giving $O(mn)$ time. The row has one entry per character of the shorter source, giving $O(\min(m, n))$ auxiliary space.

#### Alternatives and edge cases

- **Greedy matching:** fails when the same target character could validly come from either source.
- **Plain backtracking:** can revisit the same prefix pair exponentially many times.
- **Full two-dimensional DP:** is correct and also $O(mn)$ time, but uses $O(mn)$ space.
- Two empty sources interleave to the empty target. If only one source is empty, validity reduces to exact equality of the other source and target.
- Character counts alone are necessary but not sufficient because each source's internal order must be preserved.

</details>
