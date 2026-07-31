# Sort the Students by Their Kth Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2545 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [sort-the-students-by-their-kth-score](https://leetcode.com/problems/sort-the-students-by-their-kth-score/) |

## Problem Description

### Goal

A class has $m$ students who each completed $n$ exams. Their results are stored in a 0-indexed $m \times n$ integer matrix `score`: row `i` belongs to student $i$, and `score[i][j]` is that student's result on exam $j$. Every integer in the matrix is distinct.

Given a 0-indexed exam index `k`, reorder the students, including all of each student's scores, from the highest score on exam `k` to the lowest. Return the matrix with its rows in that order.

### Function Contract

**Inputs**

- `score`: An $m \times n$ integer matrix whose rows represent students and whose columns represent exams.
- `k`: The 0-indexed exam column used to rank the rows.

Both $m$ and $n$ are between 1 and 250, every score is between 1 and $10^5$, all scores are distinct, and $0 \le k < n$.

**Return value**

Return all rows of `score` ordered by their value at column `k` in strictly descending order.

### Examples

**Example 1**

- Input: `score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2`
- Output: `[[7,5,11,2],[10,6,9,1],[4,8,3,15]]`
- Explanation: The selected exam scores are 11, 9, and 3 in descending order.

**Example 2**

- Input: `score = [[3,4],[5,6]], k = 0`
- Output: `[[5,6],[3,4]]`
- Explanation: Student 1 scored 5 on exam 0, ahead of student 0's score of 3.
