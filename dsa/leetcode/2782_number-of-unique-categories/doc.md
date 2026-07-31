# Number of Unique Categories

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2782 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Union-Find, Interactive, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-unique-categories/) |

## Problem Description

### Goal

There are $n$ hidden elements numbered from $0$ through $n-1$. Every element belongs to exactly one category, but the category labels themselves are unavailable. Instead, a supplied `CategoryHandler` can reveal whether two chosen indices belong to the same category.

Use only these pairwise equality answers to determine how many distinct categories occur among all $n$ elements. Category membership is not guaranteed to follow the index order, so equal-category elements may be separated by elements from other categories.

### Function Contract

**Inputs**

- `n`: The number of elements, where $1 \le n \le 100$.
- `categoryHandler`: An interactive object exposing `haveSameCategory(a, b)`. It returns `true` exactly when valid indices `a` and `b` belong to the same category. It returns `false` if either index lies outside $[0,n-1]$.

The app judge constructs the `CategoryHandler` object from the integer array shown in a case input; equal array values model the oracle's hidden category equivalence. The solution itself accesses those values only through `haveSameCategory(a, b)`.

**Return value**

Return the number of equivalence classes induced by the hidden same-category relation.

### Examples

**Example 1**

- Input: `n = 6`, `categoryHandler = [1,1,2,2,3,3]`
- Output: `3`
- Explanation: Indices `0` and `1` form one category, indices `2` and `3` form another, and indices `4` and `5` form the third.

**Example 2**

- Input: `n = 5`, `categoryHandler = [1,2,3,4,5]`
- Output: `5`
- Explanation: No pair belongs to the same category, so every index represents a distinct category.

**Example 3**

- Input: `n = 3`, `categoryHandler = [1,1,1]`
- Output: `1`
- Explanation: Every pair belongs to the same category, leaving one unique category.
