# Happy Students

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2860 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/happy-students/) |

## Problem Description

### Goal

A class contains $n$ students, described by the 0-indexed integer array `nums`. A teacher chooses some of them to form a group. Whether a student is happy depends on the final number of selected students and on that student's value in `nums`.

If student $i$ is selected, the group must contain strictly more than `nums[i]` students. If student $i$ is not selected, the group must contain strictly fewer than `nums[i]` students. Count how many groups make every student happy at the same time.

### Function Contract

**Inputs**

- `nums`: The happiness thresholds for the students.

Let $n$ be the length of `nums`. The input satisfies $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} < n$.

**Return value**

- Return the number of groups for which every selected and unselected student satisfies the corresponding strict inequality.

### Examples

**Example 1**

- Input: `nums = [1, 1]`
- Output: `2`
- Explanation: Selecting nobody works because $0 < 1$ for both unselected students. Selecting both students also works because $2 > 1$. Selecting exactly one student satisfies neither student's required condition.

**Example 2**

- Input: `nums = [6, 0, 3, 3, 6, 7, 2, 7]`
- Output: `3`
- Explanation: The valid group sizes are $1$, $4$, and $8$. For each size, the students with smaller thresholds are selected and all remaining thresholds are strictly larger than the group size.
