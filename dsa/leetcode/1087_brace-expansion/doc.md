# Brace Expansion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1087 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Stack, Breadth-First Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [brace-expansion](https://leetcode.com/problems/brace-expansion/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/brace-expansion/).

### Goal
Expand a pattern where braces contain comma-separated single-character choices. Characters outside braces are fixed. Return every possible expanded word in lexicographic order.

### Function Contract
**Inputs**

- `s`: Brace expression without nested braces.

**Return value**

Sorted list of all expanded strings.

### Examples
**Example 1**

- Input: `s = "{a,b}c{d,e}f"`
- Output: `["acdf", "acef", "bcdf", "bcef"]`

**Example 2**

- Input: `s = "abcd"`
- Output: `["abcd"]`

**Example 3**

- Input: `s = "a{b,c}d"`
- Output: `["abd", "acd"]`

---

## Solution
### Approach
Parse the expression into a list of groups. A group is either a fixed character or a sorted list of choices from a brace block. Then perform backtracking over the groups, appending one choice from each group to build every word.

Sorting each brace choice list ensures the generated output is lexicographic.

### Complexity Analysis
- **Time Complexity**: `O(R * L)`, where `R` is the number of generated results and `L` is the output word length.
- **Space Complexity**: `O(R * L)` for the returned strings.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
