# Match Substring After Replacement

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2301 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, String Matching |
| Official Link | [LeetCode](https://leetcode.com/problems/match-substring-after-replacement/) |

## Problem Description

### Goal

Given strings `s` and `sub`, determine whether `sub` can become a contiguous
substring of `s`. A directed mapping `[old, new]` permits one occurrence of
`old` in `sub` to be replaced by `new`. Any mapping may be used for any number
of matching positions, but each individual `sub` position may be replaced at
most once.

Replacement is optional and directional. An unchanged character always
matches itself; `[old, new]` does not permit `new` to become `old`, and two
mappings cannot be chained on one character.

Return whether some alignment of `sub` within `s` matches position by position
under those rules.

### Function Contract

**Inputs**

- `s`: The string in which a transformed `sub` must appear contiguously.
- `sub`: The nonempty pattern whose positions may each undergo zero or one replacement.
- `mappings`: Directed character pairs `[old, new]`.

Let $S=\lvert\texttt{s}\rvert$, $P=\lvert\texttt{sub}\rvert$, and
$R=\lvert\texttt{mappings}\rvert$. The contract guarantees
$1 \le P \le S \le 5000$ and $0 \le R \le 1000$. Characters are uppercase or
lowercase English letters or digits, and each mapping has distinct endpoints.

**Return value**

`true` if at least one length-$P$ substring of `s` can be matched by applying
valid one-step replacements independently to positions of `sub`; otherwise
`false`.

### Examples

#### Example 1

- **Input:** `s = "fool3e7bar"`, `sub = "leet"`, `mappings = [["e", "3"], ["t", "7"], ["t", "8"]]`
- **Output:** `true`

#### Example 2

- **Input:** `s = "fooleetbar"`, `sub = "f00l"`, `mappings = [["o", "0"]]`
- **Output:** `false`

#### Example 3

- **Input:** `s = "Fool33tbaR"`, `sub = "leetd"`, `mappings = [["e", "3"], ["t", "7"], ["t", "8"], ["d", "b"], ["p", "b"]]`
- **Output:** `true`
