# The Score of Students Solving Math Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2019 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, String, Dynamic Programming, Stack, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [the-score-of-students-solving-math-expression](https://leetcode.com/problems/the-score-of-students-solving-math-expression/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/the-score-of-students-solving-math-expression/).

### Goal
Grade answers to an arithmetic expression containing digits, `+`, and `*`. The correct answer gets full credit, while answers possible from incorrect parenthesization get partial credit.

### Function Contract
**Inputs**

- `s`: the expression string.
- `answers`: submitted integer answers.

**Return value**

Return the total score across all answers.

### Examples
**Example 1**

- Input: `s = "7+3*1*2", answers = [20,13,42]`
- Output: `7`

**Example 2**

- Input: `s = "3+5*2", answers = [13,0,10,13,13,16,16]`
- Output: `19`

**Example 3**

- Input: `s = "6+0*1", answers = [12,6,6,6,6]`
- Output: `10`

---

## Solution
### Approach
Evaluate the expression normally for the correct value. For partial values, use interval DP over operands: combine possible left and right results for every operator, keeping only values within the allowed answer bound. Score each answer by membership in those sets.

### Complexity Analysis
- **Time Complexity**: `O(n^3 * V^2)` in the worst case for expression DP value combinations.
- **Space Complexity**: `O(n^2 * V)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
