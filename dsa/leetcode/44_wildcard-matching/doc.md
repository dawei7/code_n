# Wildcard Matching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 44 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Greedy, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/wildcard-matching/) |

## Problem Description
### Goal
You are given a text string `s` and a wildcard pattern `p`. Ordinary pattern characters match themselves, `?` matches exactly one arbitrary character, and `*` matches any consecutive sequence of characters, including an empty sequence.

Determine whether the pattern matches the complete text from beginning to end rather than merely a prefix or substring. Each asterisk may consume a different number of characters, and consecutive asterisks have the same expressive effect as one. Return a boolean indicating whether some valid assignment of wildcard lengths covers all of `s`.

### Function Contract
**Inputs**

- `s`: `str`
- `p`: `str` containing ordinary characters, `?`, and `*`

**Return value**

`True` when the complete pattern matches the complete string; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "aa", p = "a"`
- Output: `False`

**Example 2**

- Input: `s = "aa", p = "*"`
- Output: `True`

**Example 3**

- Input: `s = "cb", p = "?a"`
- Output: `False`

### Required Complexity

- **Time:** $O(nm)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Define states for complete prefix-to-prefix matches**

Let `dp[i][j]` mean that `p[:j]` matches all of `s[:i]`. This whole-prefix meaning prevents a successful substring match from being mistaken for a complete match. An ordinary character or `?` consumes exactly one character from both sides, so its transition uses the diagonal state `dp[i - 1][j - 1]` and a character-compatibility check.

Only the previous string row and the current row are needed. For non-star tokens, the dependency is in the previous row; for stars, one dependency is in the current row to the left. Filling pattern columns from left to right therefore supports row compression safely.

**A star either stays empty or extends its current match**

At pattern position `j`, `*` has two exhaustive ways to finish a prefix match:

- match no characters, discarding the star via `current[j - 1]`;
- consume the current string character while keeping the star available via `previous[j]`.

Repeated use of the second transition represents any positive star length. Their logical OR therefore covers every sequence length without enumerating those lengths explicitly.

Initialize the empty-string row by propagating truth only through leading stars. Once an ordinary token or `?` appears, that and every longer prefix ending there cannot match empty unless later transitions still include the unmatched token—which they do not.

**Preserve row meaning during compression**

Before each string row, `previous[j]` exactly describes whether `p[:j]` matches the earlier string prefix. Set `current[0]` false for a nonempty string. Then every transition enumerates all legal final behavior of the current pattern token, so `current[j]` exactly describes the extended string prefix. Swapping rows restores the invariant for the next character.

**Trace a star that consumes a middle run**

For `adceb` and `*a*b`, the first star may match empty before `a`, then the second star repeatedly inherits from its previous-row state while consuming `dce`. The final literal `b` takes a diagonal match, making the complete-prefix state true.

**Each state is determined by its token's final action**

A literal or `?` can complete a prefix match only by consuming the current character and extending the diagonal shorter-prefix state. A `*` completes a match in exactly two forms: it consumes nothing and inherits from the pattern without the star, or it consumes the current character after the same star matched a shorter string prefix.

These final actions are exhaustive for each token type and refer only to already computed shorter prefixes. Therefore every true state corresponds to a valid whole-prefix match, and every valid match has one of the represented final actions. The bottom-right state consequently describes the complete string and pattern exactly.

#### Complexity detail

The algorithm fills one constant-time state for every pair of string and pattern prefix lengths, giving $O(nm)$ time. Two Boolean arrays of length $m + 1$ use $O(m)$ auxiliary space.

#### Alternatives and edge cases

- **Naive recursive star branching:** may retry exponentially many distributions of characters among stars.
- **Full DP table:** has the same $O(nm)$ time but uses $O(nm)$ space instead of two rows.
- **Greedy last-star backtracking:** often fast and constant-space, but its subtle worst-case behavior and invariant are harder to guarantee than the explicit DP state space.
- Empty input matches an empty pattern or a pattern consisting entirely of stars, but not a pattern containing `?` or an ordinary character.
- Unlike regular-expression problem 10, `*` here is an independent wildcard for any character sequence; it does not repeat the preceding token.

</details>
