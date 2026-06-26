# Reward Top K Students

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2512 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting, Heap (Priority Queue) |
| Official Link | [reward-top-k-students](https://leetcode.com/problems/reward-top-k-students/) |

## Problem Description & Examples
### Goal
Calculate the total score for each student based on their feedback reports. Positive words add 3 points, negative words subtract 1 point, and neutral words have no effect. Return the IDs of the top K students, sorted by score in descending order. If scores are tied, the student with the smaller ID comes first.

### Function Contract
**Inputs**

- `positive_feedback`: A list of strings representing words that increase a student's score.
- `negative_feedback`: A list of strings representing words that decrease a student's score.
- `report`: A list of strings where each string contains space-separated words for a specific student.
- `student_id`: A list of integers representing the unique ID for each student corresponding to the `report` index.
- `k`: An integer representing the number of top-scoring students to return.

**Return value**

- A list of integers containing the IDs of the top `k` students, ordered by score (descending) and then by ID (ascending).

### Examples
**Example 1**

- Input: `positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2`
- Output: `[1,2]`

**Example 2**

- Input: `positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2`
- Output: `[2,1]`

**Example 3**

- Input: `positive_feedback = ["f"], negative_feedback = ["f"], report = ["f"], student_id = [1], k = 1`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
The solution utilizes a Hash Set for O(1) average-time lookups of feedback words. The core logic involves mapping each student to a calculated score and then performing a custom sort (or using a heap) based on the primary key (score descending) and secondary key (ID ascending).

---

## Complexity Analysis
- **Time Complexity**: O(N * M + S log S), where N is the number of reports, M is the average number of words per report, and S is the number of students. We iterate through all words once, and then sort the student list.
- **Space Complexity**: O(P + N), where P is the number of unique feedback words stored in the hash sets and N is the number of students stored in the results list.
