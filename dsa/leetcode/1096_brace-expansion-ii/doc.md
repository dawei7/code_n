# Brace Expansion II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1096 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [brace-expansion-ii](https://leetcode.com/problems/brace-expansion-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/brace-expansion-ii/).

### Goal
Expand an expression with nested braces, comma unions, and implicit concatenation. Return all distinct generated words in lexicographic order.

### Function Contract
**Inputs**

- `expression`: Brace expression containing lowercase letters, braces, and commas.

**Return value**

Sorted list of unique expanded strings.

### Examples
**Example 1**

- Input: `expression = "{a,b}{c,{d,e}}"`
- Output: `["ac", "ad", "ae", "bc", "bd", "be"]`

**Example 2**

- Input: `expression = "{{a,z},a{b,c},{ab,z}}"`
- Output: `["a", "ab", "ac", "z"]`

**Example 3**

- Input: `expression = "{a,b}c"`
- Output: `["ac", "bc"]`

---

## Solution
### Approach
Parse the expression with recursive descent. A comma represents union, while adjacent factors represent Cartesian-product concatenation. A factor is either a literal character or a nested brace expression.

Each parser step returns a set of strings. Union combines sets; concatenation builds every prefix-suffix combination. At the end, sort the final set.

### Complexity Analysis
- **Time Complexity**: `O(R * L log R)` for `R` generated unique strings of length up to `L`, including final sorting.
- **Space Complexity**: `O(R * L)` for the generated sets.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
