# Sort the Students by Their Kth Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2545 |
| Difficulty | Medium |
| Topics | Array, Sorting, Matrix |
| Official Link | [sort-the-students-by-their-kth-score](https://leetcode.com/problems/sort-the-students-by-their-kth-score/) |

## Problem Description & Examples
### Goal
Given a 2D matrix representing the examination scores of students (where each row corresponds to a student and each column to a subject), reorder the rows such that the students are sorted in descending order based on their scores in a specific column `k`.

### Function Contract
**Inputs**

- `score`: A list of lists of integers (`List[List[int]]`), where `score[i][j]` represents the score of the $i$-th student in the $j$-th subject.
- `k`: An integer representing the index of the subject to be used as the sorting criterion.

**Return value**

- A list of lists of integers (`List[List[int]]`) representing the matrix rows rearranged by the $k$-th column values in descending order.

### Examples
**Example 1**

- Input: `score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2`
- Output: `[[7,5,11,2],[10,6,9,1],[4,8,3,15]]`

**Example 2**

- Input: `score = [[3,4],[5,6]], k = 0`
- Output: `[[5,6],[3,4]]`

**Example 3**

- Input: `score = [[1,2,3],[4,5,6]], k = 1`
- Output: `[[4,5,6],[1,2,3]]`

---

## Underlying Base Algorithm(s)
The problem is solved using a stable sorting algorithm (Timsort in Python). By providing a custom key to the sorting function that targets the $k$-th index of each row, we can efficiently reorder the rows based on the specified column.

---

## Complexity Analysis
- **Time Complexity**: $O(M \cdot N + M \log M)$, where $M$ is the number of students (rows) and $N$ is the number of subjects (columns). We iterate through the rows to sort them, and the sorting operation takes $O(M \log M)$ comparisons.
- **Space Complexity**: $O(M)$ or $O(M \cdot N)$ depending on the implementation of the sort (Python's `sort` creates a new list of references, effectively $O(M)$ additional space).
