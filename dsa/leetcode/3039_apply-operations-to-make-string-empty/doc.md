# Apply Operations to Make String Empty

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3039 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/apply-operations-to-make-string-empty/) |

## Problem Description

### Goal

You are given a string `s`. Perform an operation by considering every lowercase English letter from `'a'` through `'z'`: if that letter currently occurs in the string, remove its first occurrence. Repeat this operation until the string becomes empty.

Return the entire string as it appears immediately before the final operation. The relative order of the remaining characters is never changed by an operation; only selected occurrences are deleted.

### Function Contract

Let $n=\lvert\texttt{s}\rvert$.

**Inputs**

- `s`: A string of lowercase English letters with $1 \le n \le 5 \cdot 10^5$.

**Return value**

Return the nonempty string present immediately before the operation that removes all of its remaining characters.

### Examples

#### Example 1

- **Input:** `s = "aabcbbca"`
- **Output:** `"ba"`
- **Explanation:** The successive strings are `"aabcbbca"`, `"abbca"`, `"ba"`, and `""`. Thus `"ba"` is the state immediately before the last operation.

#### Example 2

- **Input:** `s = "abcd"`
- **Output:** `"abcd"`
- **Explanation:** Every letter occurs once, so the first operation also empties the string.
