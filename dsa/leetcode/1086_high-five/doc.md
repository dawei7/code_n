# High Five

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1086 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [high-five](https://leetcode.com/problems/high-five/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/high-five/).

### Goal
For each student, compute the integer average of that student's top five scores. Return results sorted by student id.

### Function Contract
**Inputs**

- `items`: List of `[student_id, score]` records.

**Return value**

List of `[student_id, top_five_average]` rows sorted by `student_id`.

### Examples
**Example 1**

- Input: `items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]`
- Output: `[[1, 87], [2, 88]]`

**Example 2**

- Input: `items = [[1, 100], [1, 90], [1, 80], [1, 70], [1, 60]]`
- Output: `[[1, 80]]`

**Example 3**

- Input: `items = [[3, 50], [3, 60], [3, 70], [3, 80], [3, 90], [3, 100]]`
- Output: `[[3, 80]]`

---

## Solution
### Approach
Group scores by student id. For each student, keep only the five largest scores, either by sorting all scores descending or by maintaining a small min-heap of size five. Sum the five retained scores and use integer division by `5`.

Finally, emit rows in ascending student id order.

### Complexity Analysis
- **Time Complexity**: `O(n log 5 + s log s)` with size-five heaps, where `n` is the number of score records and `s` is the number of students.
- **Space Complexity**: `O(s)` because each student stores at most five scores.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
