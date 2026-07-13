# Regular Expression Matching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 10 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/regular-expression-matching/) |

## Problem Description
### Goal
You are given a text string `s` and a pattern `p` using lowercase letters plus two special symbols. A dot `.` matches exactly one arbitrary character. An asterisk `*` modifies the immediately preceding letter or dot and allows that element to appear zero or more consecutive times.

Decide whether the pattern can match the entire text from beginning to end. Matching only a prefix or internal substring is not sufficient. An asterisk may eliminate its preceding element completely, so patterns can match an empty text, and several starred elements may interact; no other regular-expression operators have special meaning.

### Function Contract
**Inputs**

- `s`: `str`
- `p`: valid `str` pattern using lowercase letters, `.` and `*`

**Return value**

`True` when `p` matches the complete string; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "aa", p = "a"`
- Output: `False`

**Example 2**

- Input: `s = "aa", p = "a*"`
- Output: `True`

**Example 3**

- Input: `s = "ab", p = ".*"`
- Output: `True`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Model whole-string matching with prefix states**

Let `dp[i][j]` mean that the first `i` characters of `s` are matched by the first `j` characters of `p`. The answer is `dp[m][n]`, not any state that matches merely a substring. Recording prefix lengths turns every recursive choice into one of only $(m + 1)(n + 1)$ distinct subproblems and prevents ambiguous stars from being explored exponentially many times.

The full two-dimensional table is conceptually useful, but row `i` depends only on row $i - 1$ and values already computed in row `i`. Therefore two pattern-length rows are enough, reducing storage from $O(mn)$ to $O(n)$, where `n` is the pattern length.

**Ordinary pattern elements consume exactly one character**

If `p[j - 1]` is a literal or `.`, it must consume exactly the current string character. The state is true only if the characters are compatible and the two shorter prefixes already matched:

```text
current[j] = previous[j - 1] and (
    p[j - 1] == s[i - 1] or p[j - 1] == "."
)
```

This diagonal dependency prevents `.` from matching zero characters and ensures every consumed string character has one corresponding pattern element.

**A star has two exhaustive final roles**

At `p[j - 1] == "*"`, the repeated element is `p[j - 2]`. Every successful match using this pattern prefix falls into exactly one of two cases:

For `*`, there are two exhaustive possibilities:

- **Zero copies:** discard both the repeated element and its star, inheriting `current[j - 2]`.
- **One or more copies:** the repeated element must match `s[i - 1]`, and `previous[j]` must be true. Keeping the same pattern prefix available allows the star to consume another character later.

The second transition deliberately uses `previous[j]`, not `previous[j - 2]`: only the string becomes shorter, while the entire starred pair remains active.

**Initialize patterns that can match the empty string**

Set the empty-pattern, empty-string state to true. A nonempty pattern can match the empty string only if all of it can be removed as `element*` pairs. Thus, before processing any input character, each star position inherits the state two columns earlier:

```text
empty_row[j] = empty_row[j - 2]  when p[j - 1] == "*"
```

For example, `a*b*c*` can match empty, but `a*b` cannot. This initialization is not an optimization; without it, zero-occurrence chains at the beginning of a match would be lost.

**Preserve row meaning while compressing the table**

At the start of string row `i`, `previous[j]` is correct for every pattern prefix against `s[:i - 1]`. Set `current[0]` to false because a nonempty string cannot match an empty pattern. Then fill `current` from left to right. This order is important: a star's zero-copy transition reads `current[j - 2]`, which must already describe the same string prefix.

Each transition enumerates every legal final use of the current pattern element and no illegal one. After the rows are swapped, `previous` has the required meaning for the next input prefix.

**Trace how stars cooperate**

For `s = "aab"` and `p = "c*a*b"`, the empty row first establishes that `c*` and then `c*a*` can both represent empty. While processing the two `a` characters, `c*` continues to use zero copies and `a*` repeatedly uses its one-or-more transition. The final `b` uses the ordinary diagonal transition from the state where `c*a*` matched `aa`, making the complete-prefix state true.

This example also shows why a greedy rule such as “make each star consume as much as possible” is insufficient. A star must sometimes relinquish characters so that a later pattern element can match them; dynamic programming represents both possibilities without committing prematurely.

**Why the two star transitions cover every match**

An unstarred pattern element can participate in a complete-prefix match in only one way: it consumes the final string character when the symbols agree, leaving the preceding prefixes to match. For `x*`, split by how many copies the star contributes. Zero copies discard `x*` and use the state two pattern positions back. One or more copies consume the current matching character while keeping `x*` available for the remaining prefix.

Those cases are exhaustive and do not assume a greedy consumption count. Each DP cell therefore combines exactly all decompositions of its two prefixes, and the initialized empty-string row represents precisely the patterns made entirely of zero-copy starred elements. Building cells from shorter prefixes makes the final state true if and only if the whole string matches the whole pattern.

#### Complexity detail

There are `m` nonempty string rows and `n` pattern columns, and every cell performs constant work, so the running time is $O(mn)$. Two Boolean rows of length $n + 1$ use $O(n)$ auxiliary space. If the roles of string and pattern are fixed by the transitions, the pattern dimension is the one that must be retained.

#### Alternatives and edge cases

- **Naive recursive backtracking:** mirrors the definition but may explore exponentially many ways to divide repeated characters among adjacent stars.
- **Memoized recursion:** has the same $O(mn)$ state count and is correct, but uses recursion and a full memo table.
- **General regex engine:** supports a different, much larger syntax and may not enforce this problem's exact whole-string contract transparently.
- Empty strings require the special `element*` initialization. A pattern like `.*` can consume any sequence, but `.` alone consumes exactly one character.
- Consecutive or leading stars are excluded by the valid-pattern contract; an implementation need not invent semantics for them.

</details>
