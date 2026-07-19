# Brace Expansion II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1096 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/brace-expansion-ii/) |

## Problem Description

### Goal

Under the specified grammar, an expression represents a set of lowercase words, denoted by $R(e)$. A lowercase letter `x` represents the singleton set containing `x`. A comma-delimited group of at least two expressions represents the union of their sets, so duplicate words appear only once.

Adjacent expressions represent concatenation: combine every word from the left set with every word from the right set. Braces may nest, allowing union and concatenation to occur at multiple levels. Given a valid expression containing lowercase letters, braces, and commas, return all distinct words in $R(e)$ in lexicographic order.

### Function Contract

**Inputs**

- `expression`: a valid grammar expression of length $E$, where $1 \leq E \leq 60$ and every character is a lowercase English letter, `{`, `}`, or `,`.

Let $R$ be the number of distinct generated words, let $L$ be their maximum length, and define the total output text size as

$$
S = \sum_{w \in R(e)} \lvert w \rvert.
$$

**Return value**

The lexicographically sorted list of all distinct words represented by `expression`.

### Examples

**Example 1**

- Input: `expression = "{a,b}{c,{d,e}}"`
- Output: `["ac", "ad", "ae", "bc", "bd", "be"]`

**Example 2**

- Input: `expression = "{{a,z},a{b,c},{ab,z}}"`
- Output: `["a", "ab", "ac", "z"]`

The alternatives generate `ab` and `z` more than once, but the result is a set.
