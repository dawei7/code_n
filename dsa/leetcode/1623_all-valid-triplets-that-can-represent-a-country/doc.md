# All Valid Triplets That Can Represent a Country

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1623 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/all-valid-triplets-that-can-represent-a-country/) |

## Problem Description
### Goal
Tables `SchoolA`, `SchoolB`, and `SchoolC` list students by `student_id` and `student_name`. Form a country-representing triplet by choosing exactly one student from each school.

A triplet is valid only when its three student IDs are pairwise different and its three student names are also pairwise different. Return every valid combination, showing the chosen names from schools A, B, and C as `member_A`, `member_B`, and `member_C` respectively.

### Function Contract
**Inputs**

- `SchoolA(student_id, student_name)`: candidate members from school A.
- `SchoolB(student_id, student_name)`: candidate members from school B.
- `SchoolC(student_id, student_name)`: candidate members from school C.
- Let $a$, $b$, and $c$ be the respective table row counts.

**Return value**

Return one row per valid cross-school triplet with columns `member_A`, `member_B`, and `member_C`. Row order is not semantically significant.

### Examples
**Example 1**

- Input: `SchoolA = [[1,"Alice"],[2,"Bob"]]`, `SchoolB = [[3,"Tom"]]`, `SchoolC = [[3,"Tom"],[2,"Jerry"],[10,"Alice"]]`
- Output: `[ ["Alice","Tom","Jerry"], ["Bob","Tom","Alice"] ]`

**Example 2**

- Input: one student in each school with distinct IDs and names
- Output: the one corresponding triplet

**Example 3**

- Input: every possible choice repeats an ID or a name
- Output: no rows
