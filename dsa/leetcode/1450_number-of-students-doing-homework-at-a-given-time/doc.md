# Number of Students Doing Homework at a Given Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1450 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/) |

## Problem Description
### Goal

Two equal-length arrays describe the homework interval for each student.
Student $i$ starts at `startTime[i]` and finishes at `endTime[i]`. Both moments
belong to the interval: the student is still doing homework at the exact finish
time, as well as at the exact start time.

Given a particular `queryTime`, count how many students have an interval that
contains that time. Each student contributes independently and at most once.

### Function Contract
**Inputs**

- `startTime`: a list of $n$ integer start times.
- `endTime`: a list of $n$ integer finish times aligned by student with
  `startTime`.
- The arrays have the same length, with $1 \le n \le 100$.
- For every index $i$,
  $1 \le \texttt{startTime[i]} \le \texttt{endTime[i]} \le 1000$.
- `queryTime`: an integer satisfying $1 \le \texttt{queryTime} \le 1000$.

**Return value**

Return the number of indices $i$ for which
$\texttt{startTime[i]} \le \texttt{queryTime} \le \texttt{endTime[i]}$.

### Examples
**Example 1**

- Input: `startTime = [1, 2, 3], endTime = [3, 2, 7], queryTime = 4`
- Output: `1`
- Explanation: Only the third student's interval `[3, 7]` contains time `4`.

**Example 2**

- Input: `startTime = [4], endTime = [4], queryTime = 4`
- Output: `1`
- Explanation: A zero-duration interval still contains its shared start and
  finish time.

**Example 3**

- Input: `startTime = [1, 2, 5], endTime = [2, 5, 6], queryTime = 5`
- Output: `2`
- Explanation: Time `5` is the inclusive finish of the second interval and the
  inclusive start of the third.
