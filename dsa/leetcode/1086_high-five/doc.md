# High Five

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1086 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/high-five/) |

## Problem Description

### Goal

Each entry in `items` has the form `[student_id, score]` and records one exam score for that student. Every represented student has at least five recorded scores.

For each student, select that student's five highest scores and compute their sum divided by five using integer division. Return one `[student_id, top_five_average]` row per student, ordered by `student_id` in ascending order. Scores outside the top five must not affect the average.

### Function Contract

**Inputs**

- `items`: $N$ pairs `[student_id, score]`; every one of the $S$ distinct students occurs at least five times.

**Return value**

- A list of $S$ rows `[student_id, average]` in ascending `student_id` order.
- Each `average` is the integer quotient of the student's five highest scores divided by 5.

### Examples

**Example 1**

- Input: `items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]`
- Output: `[[1, 87], [2, 88]]`

Student 1's top five sum to 435, while student 2's top five sum to 443; integer division produces 87 and 88.

**Example 2**

- Input: `items = [[1, 100], [1, 90], [1, 80], [1, 70], [1, 60]]`
- Output: `[[1, 80]]`
