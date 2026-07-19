# K-Similar Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 854 |
| Difficulty | Hard |
| Topics | Hash Table, String, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/k-similar-strings/) |

## Problem Description
### Goal
Two strings are $k$-similar when exactly $k$ operations, each swapping the letters at any two positions of the first string, can transform it into the second string. The swapped positions do not need to be adjacent.

Given anagrams `s1` and `s2`, find the smallest nonnegative $k$ for which they are $k$-similar. Both strings use only the lowercase letters `a` through `f`, and repeated letters are allowed.

### Function Contract
**Inputs**

- `s1`: a string of length $n$, where $1 \leq n \leq 20$ and every character belongs to `{"a","b","c","d","e","f"}`.
- `s2`: an anagram of `s1` with the same length.

For a character $c$, let $f_c$ be its frequency. The number of distinct anagrams reachable by swaps is

$$
P = \frac{n!}{\prod_c f_c!}.
$$

**Return value**

Return the minimum number of arbitrary-position swaps needed to transform `s1` into `s2`.

### Examples
**Example 1**

- Input: `s1 = "ab", s2 = "ba"`
- Output: `1`

**Example 2**

- Input: `s1 = "abc", s2 = "bca"`
- Output: `2`

One shortest sequence is `"abc" -> "bac" -> "bca"`.

**Example 3**

- Input: `s1 = "abc", s2 = "abc"`
- Output: `0`
