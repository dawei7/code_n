# Count Student Number in Departments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 580 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/count-student-number-in-departments/) |

## Problem Description
### Goal
Given a `Department` table containing the complete department catalog and a `Student` table whose `dept_id` identifies each student's department, count how many students belong to every department. A department must still appear when no student row refers to it, with its count reported as zero.

Return the columns `dept_name` and `student_number`. Order the result by `student_number` in descending order so departments with more students appear first; when two departments have the same count, order their names in ascending lexicographical order.

### Function Contract
**Inputs**

- `Student(student_id, student_name, gender, dept_id)`: students and their department identifiers
- `Department(dept_id, dept_name)`: the complete department catalog

**Return value**

- Columns `dept_name` and `student_number`
- Include one row for every department, using zero when no student belongs to it
- Order by `student_number` descending, then `dept_name` ascending

### Examples
**Example 1**

- Input: Engineering has three students and History has one
- Output: Engineering with `3`, then History with `1`

**Example 2**

- Input: Music has no students
- Output: Music with `0`

**Example 3**

- Input: Art and Biology have the same student count
- Output: Art before Biology

### Required Complexity

- **Time:** $O((D + S) \log D)$
- **Space:** $O(D + S)$

<details>
<summary>Approach</summary>

#### General

**Start from the complete department catalog**

Use `Department` as the left side of a left join to `Student`. This preserves a department even when no student row matches its identifier.

**Count a nullable student column**

Group by the department identifier and name. Count `student_id`, not `COUNT(*)`: an empty department still produces one null-extended joined row, and counting all rows would incorrectly report one student. `COUNT(student_id)` ignores that null and returns zero.

**Apply both ordering keys**

Sort by the aggregate count descending so larger departments appear first. Then sort equal counts by department name ascending, as required.

**Why every department receives the right count**

The left join creates one joined row for each matching student and retains one null-extended row only when there are no matches. Counting non-null student identifiers therefore equals the number of students for populated departments and zero for empty ones. Grouping produces exactly one output row for every preserved department.

#### Complexity detail

For `D` departments and `S` students, joining and grouping process $O(D + S)$ rows with suitable hashing or indexes. Ordering the `D` result groups costs $O(D \log D)$, for $O((D + S) \log D)$ time in the general bound and $O(D + S)$ working space.

#### Alternatives and edge cases

- **Preaggregate students before joining:** count students by `dept_id`, left join those totals to departments, and replace a missing total with zero; it has the same asymptotic behavior.
- **Correlated count per department:** is concise but may scan all students for each department and take $O(DS)$ time.
- **Inner join:** omits empty departments and violates the contract.
- **`COUNT(*)` after a left join:** reports one for an empty department because it counts the null-extended row.
- **Empty department:** must appear with `student_number = 0`.
- **Equal counts:** use ascending department name as the tie-breaker.
- **Duplicate department names:** group by identifier as well as name so distinct departments are not merged.
- **Student attributes:** names and genders do not affect the count.

</details>
