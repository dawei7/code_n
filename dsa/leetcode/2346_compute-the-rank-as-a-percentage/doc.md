# Compute the Rank as a Percentage

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2346 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/compute-the-rank-as-a-percentage/) |

## Problem Description

### Goal

The `Students` table records each student's department and exam mark. Rank students independently within their departments by descending mark, so the highest mark has rank 1. Students with the same mark share the same standard competition rank; later ranks retain the resulting gaps.

For a student in a department of size $d$, convert rank $r$ to the percentage

$$
\frac{(r-1)\cdot 100}{d-1}.
$$

Round the percentage to two decimal places and return it with the student and department identifiers. A department containing one student has percentage 0. Result rows may appear in any order.

### Function Contract

**Inputs**

- `Students`: A table with unique integer `student_id`, integer `department_id`, and integer `mark`.

**Return value**

Return `student_id`, `department_id`, and the student's department-relative `percentage`, rounded to two decimal places. Output order is unrestricted.

### Examples

#### Example 1

- **Input:** `Students = [(2,2,650),(8,2,650),(7,1,920),(1,1,610),(3,1,530)]`
- **Output:** `[(7,1,0.0),(1,1,50.0),(3,1,100.0),(2,2,0.0),(8,2,0.0)]`

Department 1 has three distinct ranks. Both students in department 2 share its highest mark and therefore both receive rank 1 and percentage 0.
