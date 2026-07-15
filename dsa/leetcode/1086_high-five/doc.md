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

### Required Complexity

- **Time:** $O(N+S\log S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Keep only scores that can still matter:** Associate each student with a min-heap containing at most five scores. Push until the heap reaches five entries. For every later score, replace the heap minimum only when the new score is larger.

**Why discarding the minimum is safe:** Once six candidate scores have been seen for one student, the smallest cannot belong to the best five among those candidates. Removing it leaves exactly the five greatest scores seen so far. This property remains true after every later replacement.

**Compute and order the output:** After processing all records, each heap contains exactly that student's global top five. Sum it, evaluate `sum(heap) // 5`, and emit students in sorted identifier order.

The heap invariant proves that no discarded score can improve the final five and every retained score belongs to the greatest five seen. At the end all of a student's scores have been seen, so the retained set is precisely the required top five and its integer quotient is the requested average.

#### Complexity detail

Each of the $N$ records performs a heap operation on at most five values, which is $O(\log 5)=O(1)$. Sorting the $S$ identifiers costs $O(S\log S)$, for $O(N+S\log S)$ total time. At most five scores are stored for each student, so auxiliary space is $O(S)$.

#### Alternatives and edge cases

- **Sort every student's scores:** It is straightforward but stores all $N$ scores and can take $O(N\log N)$ total time rather than retaining only five per student.
- **Repeatedly select the next minimum:** A quadratic sorting implementation is correct but scales poorly as one student's record count grows.
- **Average all scores:** It is incorrect when a student has more than five records; lower scores must be excluded.
- **Exactly five scores:** All five contribute to the average.
- **Duplicate top scores:** Treat each score record independently; equal values can occupy several top-five positions.
- **Non-divisible sum:** Use integer division, discarding the fractional part.
- **Input order:** It does not determine output order; sort by student id explicitly.

</details>
