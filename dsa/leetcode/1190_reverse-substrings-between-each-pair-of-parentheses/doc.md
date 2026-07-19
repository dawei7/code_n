# Reverse Substrings Between Each Pair of Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1190 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/) |

## Problem Description

### Goal

You are given a string `s` made of lowercase English letters and parentheses. Every opening parenthesis has a matching closing parenthesis, and the pairs may be nested.

Reverse the string inside each matching pair, processing the innermost pair before any pair that contains it. Those inner transformations therefore become part of the contents reversed by their enclosing pairs. Return the fully transformed sequence of letters with every parenthesis removed from the result.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $1\le n\le2000$, containing only lowercase English letters and balanced parentheses.

**Return value**

- The string produced after all matched-parenthesis reversals have been applied from the inside out and all parentheses have been omitted.

### Examples

**Example 1**

- Input: `s = "(abcd)"`
- Output: `"dcba"`

**Example 2**

- Input: `s = "(u(love)i)"`
- Output: `"iloveu"`

First reverse `"love"` within the inner pair, then reverse the contents of the outer pair.

**Example 3**

- Input: `s = "(ed(et(oc))el)"`
- Output: `"leetcode"`

The reversals successively affect `"oc"`, its enclosing contents, and finally the entire outer contents.
