# Students With Invalid Departments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1350 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/students-with-invalid-departments/) |

## Problem Description

### Goal

The `Departments` table identifies each existing department by its primary-key ID and records its name. Each row of `Students` similarly has a unique student ID and name, together with the `department_id` currently assigned to that student. A recorded department reference is invalid when its ID is absent from `Departments`.

Return the ID and name of every student with such an invalid reference. Students assigned to an existing department must be excluded, and the result may be returned in any order.

### Function Contract

**Inputs**

- `Departments(id, name)`: one row per existing department; `id` is its primary key.
- `Students(id, name, department_id)`: one row per student; `id` is the student primary key and `department_id` is the recorded department reference.
- Let $D$ and $S$ be the row counts of `Departments` and `Students`, and let $N = D + S$.

**Return value**

- Return columns `id` and `name` for precisely those student rows with no matching department ID.

### Examples

**Example 1**

- Departments: IDs `1`, `7`, and `13`.
- Students: Alice references `1`; Bob references `7`; Charlie references `13`; David, Eve, and Frank reference absent IDs.
- Output: the IDs and names of David, Eve, and Frank.

**Example 2**

- Input: every student's `department_id` appears in `Departments`.
- Output: no rows.

**Example 3**

- Input: `Departments` is empty and `Students` contains two rows.
- Output: both students.
