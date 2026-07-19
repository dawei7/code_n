# Maximum Average Pass Ratio

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-average-pass-ratio/) |
| Frontend ID | 1792 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A school has several classes whose students will take a final exam. For class $i$, `classes[i] = [pass_i, total_i]` states that `total_i` students belong to the class and exactly `pass_i` of them are expected to pass. Its pass ratio is therefore $pass_i / total_i$.

There are `extraStudents` additional students, each guaranteed to pass the exam of whichever class receives them. Every extra student must be assigned to one class, increasing both that class's passing count and total count by one.

The average pass ratio is the sum of all individual class ratios divided by the number of classes. Assign all extra students so this average is as large as possible, and return that maximum. A result within $10^{-5}$ of the exact value is accepted.

### Function Contract

**Inputs**

- `classes`: a list of $n$ pairs `[passed, total]`, where $1 \le n \le 10^5$ and $1 \le passed \le total \le 10^5$.
- `extraStudents`: the number $e$ of guaranteed-passing students to distribute, where $1 \le e \le 10^5$.

**Return value**

- Return the maximum possible average pass ratio as a floating-point number.

### Examples

**Example 1**

- Input: `classes = [[1, 2], [3, 5], [2, 2]], extraStudents = 2`
- Output: `0.78333`

Assigning both students to the first class gives ratios $3/4$, $3/5$, and $2/2$.

**Example 2**

- Input: `classes = [[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents = 4`
- Output: `0.53485`

The best recipient can change after each assignment because that class's next gain becomes smaller.

**Example 3**

- Input: `classes = [[5, 5]], extraStudents = 3`
- Output: `1.00000`

The only class remains at a perfect pass ratio after every assignment.
