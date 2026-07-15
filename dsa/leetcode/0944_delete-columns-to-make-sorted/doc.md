# Delete Columns to Make Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 944 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-columns-to-make-sorted/) |

## Problem Description

### Goal

An array `strs` contains strings of equal length. Place the strings on separate rows in their given order to form a character grid. Each zero-indexed column is read from the top row downward.

A column is lexicographically sorted when its characters are in non-decreasing order from top to bottom. Delete every column that is not sorted in that sense, and return how many columns are deleted. Columns are evaluated independently; deleting one column does not reorder rows or change whether another column is sorted.

### Function Contract

Let $r$ be the number of strings and $c$ their common length.

**Inputs**

- `strs`: a list of $r$ strings with $1 \le r \le 100$.
- Every string has the same length $c$, where $1 \le c \le 1000$, and consists only of lowercase English letters.

**Return value**

Return the number of column indices whose characters are not in non-decreasing lexicographic order from row $0$ through row $r-1$.

### Examples

**Example 1**

- Input: `strs = ["cba", "daf", "ghi"]`
- Output: `1`

Columns `0` and `2` are sorted from top to bottom, but column `1` reads `"bfa"` and must be deleted.

**Example 2**

- Input: `strs = ["a", "b"]`
- Output: `0`

**Example 3**

- Input: `strs = ["zyx", "wvu", "tsr"]`
- Output: `3`

Every column decreases from the first row to the next, so all three columns are deleted.

### Required Complexity

- **Time:** $O(rc)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**An adjacent inversion is the complete test.** A column is in non-decreasing order exactly when every adjacent pair satisfies `strs[row][column] <= strs[row + 1][column]`. If any adjacent pair violates that relation, the column is not sorted and must be counted once. There is no need to compare more distant rows: if all adjacent relations hold, transitivity orders every earlier character before every later one.

Scan each of the $c$ columns. Within a column, compare consecutive rows from top to bottom. On the first inversion, increment the deletion count and stop scanning that column, because additional violations cannot change its contribution from one. If no inversion appears, leave the count unchanged. Since every column is classified independently and the scan uses exactly the defining condition, the final count is the required number of deletions.

#### Complexity detail

In the worst case, every one of the $c$ columns examines $r-1$ adjacent row pairs, giving $O(rc)$ time. The deletion count and loop indices occupy constant space, so the algorithm uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Sort each column:** Build the column characters, sort them, and compare the result with their original order. This is correct but uses extra storage and $O(cr\log r)$ time.
- **Compare every row pair:** A column is sorted if no earlier row contains a larger character than a later row. Checking all pairs is correct but takes $O(cr^2)$ time instead of using transitivity.
- **One row:** Every column is automatically sorted because there are no row pairs to violate the order.
- **Equal adjacent characters:** Equality is allowed by non-decreasing order and must not cause a deletion.
- **Early inversion:** Once one adjacent pair decreases, the column contributes exactly one deletion regardless of later characters.
- **All columns invalid:** The answer can equal $c$; deletions are counted by column, not by the number of inversions.

</details>
