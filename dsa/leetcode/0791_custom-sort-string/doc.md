# Custom Sort String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 791 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/custom-sort-string/) |

## Problem Description

### Goal

The distinct characters in string `order` define a custom relative ordering. Rearrange all characters of `s` so that whenever character `x` appears before character `y` in `order`, every occurrence of `x` appears before every occurrence of `y` in the result.

Return any permutation of `s` satisfying that rule. Characters not present in `order` may appear anywhere, and every input character occurrence must be preserved exactly once. Their relative ordering is otherwise unconstrained.

### Function Contract

**Inputs**

- `order`: a string of distinct lowercase letters defining their custom order.
- `s`: the lowercase string to rearrange.

**Return value**

- Any permutation of `s` that places characters named in `order` in the required relative order.

### Examples

**Example 1**

- Input: `order = "cba", s = "abcd"`
- Output: `"cbad"`
- Explanation: Ranked characters appear as `c`, then `b`, then `a`; unranked `d` may be placed freely.

**Example 2**

- Input: `order = "bcafg", s = "abcd"`
- Output: `"bcad"`
- Explanation: The characters shared with `order` follow `b`, `c`, `a`; `d` is unranked.

**Example 3**

- Input: `order = "kqep", s = "kqeep"`
- Output: `"kqeep"`
- Explanation: Repeated `e` characters stay together at their ranked position.
