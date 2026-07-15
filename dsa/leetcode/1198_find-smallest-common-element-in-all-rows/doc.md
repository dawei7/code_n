# Find Smallest Common Element in All Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1198 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Matrix, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/) |

## Problem Description

### Goal

You are given an $m\times n$ integer matrix `mat`. Every row is sorted in strictly increasing order, so a value occurs at most once within any individual row even though it may occur in several different rows.

Find the smallest value that appears in every row of the matrix. Return that value when one or more common elements exist; return `-1` when the rows have no element shared by all of them.

### Function Contract

**Inputs**

- `mat`: An $m\times n$ matrix, where $1\le m,n\le500$ and $1\le\texttt{mat[i][j]}\le10^4$.
- Every row `mat[i]` is sorted in strictly increasing order.

**Return value**

- The smallest integer present in all $m$ rows, or `-1` if no such integer exists.

### Examples

**Example 1**

- Input: `mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]`
- Output: `5`

The value `5` occurs in all four rows.

**Example 2**

- Input: `mat = [[1,2,3],[2,3,4],[2,3,5]]`
- Output: `2`

Both `2` and `3` are common, and `2` is smaller.

**Example 3**

- Input: `mat = [[1,2,3],[4,5,6]]`
- Output: `-1`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count row membership directly.** Allocate a frequency table indexed by the allowed values from 1 through $10^4$. Scan the rows in order and increment the frequency of each encountered value. Strict increase guarantees that a value contributes at most once per row, so its frequency equals the number of processed rows containing it without needing a per-row set.

**Return when the final required occurrence appears.** A value is common exactly when its frequency reaches $m$. This can first happen while processing the last row. Because that row is strictly increasing and scanned from left to right, the first value to reach $m$ is also the smallest common element. If no frequency reaches $m$ by the end, return `-1`.

#### Complexity detail

The scan visits each of the $mn$ matrix entries once and performs constant work per entry, giving $O(mn)$ time. The frequency table has exactly 10001 slots because the value domain is fixed at $10^4$; its size does not grow with $m$ or $n$, so auxiliary space is $O(1)$ under the stated constraints.

#### Alternatives and edge cases

- **First-row candidates with binary search:** Binary-searching every first-row value in every other row uses $O(mn\log n)$ time and $O(1)$ extra space.
- **Explicit linear membership search:** Scanning each row separately for every first-row candidate can require $O(mn^2)$ time.
- **Pointer alignment:** Maintaining one pointer per row and repeatedly advancing rows below the current maximum takes linear total pointer advances and $O(m)$ space.
- **Single row:** Every value is common to the only row, so its first value is the answer.
- **One column:** A common element exists only when every row's sole value is equal.
- **Several common values:** The sorted final-row scan returns the smallest one before any larger common value.
- **No common value:** The complete scan ends without any count reaching $m$ and returns `-1`.
- **Strict increase:** No row contains duplicates, which is essential for raw frequency counts to represent row membership.

</details>
