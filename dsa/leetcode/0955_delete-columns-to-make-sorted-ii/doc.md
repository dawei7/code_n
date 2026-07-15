# Delete Columns to Make Sorted II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 955 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [delete-columns-to-make-sorted-ii](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/) |

## Problem Description

### Goal

You are given `strs`, an array of strings that all have the same length. Choose a set of column indices and delete every chosen column from every string; all undeleted characters retain their original left-to-right order.

After the deletions, the array of resulting strings must be in lexicographic non-decreasing order, so each row is no greater than the row immediately after it. The characters inside an individual row do not themselves need to be sorted. Return the minimum number of columns that must be deleted to satisfy the row ordering.

### Function Contract

Let $N$ be the number of strings and $M$ their common length.

**Inputs**

- `strs`: a list of $N$ lowercase English strings of equal length $M$, where $1 \le N,M \le 100$.

**Return value**

Return the minimum number of common column deletions needed to make `strs` lexicographically non-decreasing.

### Examples

**Example 1**

- Input: `strs = ["ca","bb","ac"]`
- Output: `1`
- Explanation: Deleting the first column leaves `["a","b","c"]`.

**Example 2**

- Input: `strs = ["xc","yb","za"]`
- Output: `0`
- Explanation: The rows are already in lexicographic order.

**Example 3**

- Input: `strs = ["zyx","wvu","tsr"]`
- Output: `3`
- Explanation: Every column must be deleted.

### Required Complexity

- **Time:** $O(NM)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Track which adjacent row pairs are already decided.** For each pair `strs[i]`, `strs[i + 1]`, remember whether an earlier kept column has already made the upper row strictly smaller. Once that happens, later columns cannot reverse this pair's lexicographic order.

**Reject a column only when it creates an unresolved inversion.** Scan columns from left to right. Before keeping a column, inspect every still-unresolved adjacent pair. If any has `strs[i][column] > strs[i + 1][column]`, keeping this column would make that pair permanently out of order at its first difference. The column must therefore be deleted, and no pair state changes.

**Commit every safe column.** If no unresolved pair is inverted, keep the column. Mark a pair resolved wherever its characters are strictly increasing in this column; pairs with equal characters remain unresolved. Keeping a safe column cannot harm an already-resolved pair, and deleting it could only discard useful information. Thus every deletion made by the greedy scan is forced, while every retained column is compatible with some optimal result. The deletion count is minimal when all columns have been considered.

#### Complexity detail

Each of the $M$ columns examines at most $N-1$ adjacent pairs, giving $O(NM)$ time. The resolved-state array contains $N-1$ booleans and uses $O(N)$ space.

#### Alternatives and edge cases

- **Rebuild retained prefixes:** After tentatively adding each column, reconstruct every row prefix and test whether the array is sorted. This follows the same greedy decisions but repeated prefix construction costs $O(NM^2)$ time.
- **Enumerate deletion subsets:** Testing every column subset finds the minimum but requires exponential time.
- **Confuse rows with columns:** The required order is between whole resulting strings; characters within a row may decrease.
- **Already resolved pair:** Later character inversions are irrelevant after an earlier kept character made the upper row smaller.
- **Equal rows:** They remain valid and may stay unresolved through every column.
- **One row:** There is no adjacent pair to violate the order, so zero deletions are needed.

</details>
