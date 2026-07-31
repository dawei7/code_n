# Maximum Students on a Single Bench

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3450 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-students-on-a-single-bench/) |

## Problem Description
### Goal
The two-dimensional array `students` records observations of students sitting on benches. Each row has the form `[student_id, bench_id]`, meaning that the identified student is present on the identified bench.

Determine the maximum number of unique students recorded on any one bench. Repeated rows for the same student and bench describe the same presence and must contribute only once to that bench's count. The same student identifier is counted separately for each different bench on which it appears. If `students` is empty, return zero.

### Function Contract
**Inputs**

- `students`: A list of $n$ pairs `[student_id, bench_id]`.

The constraints are $0 \le n \le 100$, $1 \le \texttt{student_id} \le 100$, and $1 \le \texttt{bench_id} \le 100$.

**Return value**

Return the largest number of distinct student identifiers associated with a single bench, or `0` when no rows are present.

### Examples
**Example 1**

- Input: `students = [[1, 2], [2, 2], [3, 3], [1, 3], [2, 3]]`
- Output: `3`

**Example 2**

- Input: `students = [[1, 1], [1, 1]]`
- Output: `1`

**Example 3**

- Input: `students = []`
- Output: `0`
