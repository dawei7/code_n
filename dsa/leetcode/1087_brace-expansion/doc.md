# Brace Expansion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1087 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Stack, Breadth-First Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/brace-expansion/) |

## Problem Description

### Goal

The string `s` describes words using lowercase letters and brace groups. A lowercase letter outside braces is fixed in that position. A group such as `"{a,b,c}"` contributes exactly one of its comma-separated single-letter alternatives. Braces are not nested, and the expression is valid.

Form every word obtained by independently choosing one letter from each brace group while retaining every fixed letter. Return all expanded words in lexicographic order. Each output has one character for every fixed position or brace group in the expression.

### Function Contract

**Inputs**

- `s`: a valid, non-nested brace expression of length $n$ containing lowercase fixed letters and comma-separated single-letter alternatives.

Let $L$ be the number of output positions after treating each brace group as one position, and let $R$ be the number of expanded words.

**Return value**

- A lexicographically sorted list containing all $R$ expansions, each of length $L$.

### Examples

**Example 1**

- Input: `s = "{a,b}c{d,e}f"`
- Output: `["acdf", "acef", "bcdf", "bcef"]`

**Example 2**

- Input: `s = "abcd"`
- Output: `["abcd"]`

### Required Complexity

- **Time:** $O(n+RL)$
- **Space:** $O(n+RL)$

<details>
<summary>Approach</summary>

#### General

**Parse positions rather than punctuation:** Scan `s` from left to right. A fixed letter becomes a one-choice position. On an opening brace, locate its matching closing brace, split the interior on commas, and store the alternatives as one position.

**Sort choices before expansion:** Sort every brace position's alternatives. Fixed positions are already trivially sorted. This makes the depth-first traversal visit complete words in lexicographic order, so no separate global result sort is necessary.

**Build one character per position:** Backtrack over the parsed positions, appending each available choice and removing it after the recursive call. Reaching position $L$ yields one complete expansion.

Every expansion selects exactly one option from each parsed position, so each generated word is valid. Conversely, every valid independent selection corresponds to one unique root-to-leaf backtracking path and is generated once. At the earliest position where two generated words differ, the traversal exhausts the smaller sorted choice first, proving output order is lexicographic.

#### Complexity detail

Parsing takes $O(n)$ time. Producing $R$ strings of length $L$ requires $O(RL)$ time and output space. Parsed groups and the active recursion path use $O(n+L)$ additional storage, which is covered by $O(n+RL)$ total space.

#### Alternatives and edge cases

- **Generate then sort globally:** It is correct, but sorting $R$ complete strings adds $O(R\log R)$ comparisons after generation.
- **Quadratic insertion sort:** Sorting expansions by repeated shifting is correct but can take $O(R^2L)$ time when generation order is reversed.
- **Breadth-first Cartesian product:** Expand a list of prefixes group by group. It has the same output-sensitive bound but stores intermediate prefix sets explicitly.
- **No braces:** Return a one-element list containing `s`.
- **Adjacent groups:** Choose independently from each group; no fixed separator is implied.
- **Unsorted alternatives:** Sort them before traversal to guarantee lexicographic output.
- **Fixed prefix or suffix:** Preserve it in every expansion.

</details>
