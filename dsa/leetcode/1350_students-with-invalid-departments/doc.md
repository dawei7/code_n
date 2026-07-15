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

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(D)$

<details>
<summary>Approach</summary>

#### General

**Preserve every student with a left join.** Join `Students` to `Departments` on the recorded department ID. A valid reference produces the matching department row, while an invalid reference still preserves the student but supplies `NULL` for every column from the department side.

**Keep only unmatched rows.** Filter for `d.id IS NULL`. Because `Departments.id` is a primary key and therefore cannot itself be null, this condition distinguishes an absent join partner without confusing it with stored data. Select the student-side `id` and `name`; ordering by student ID is optional for the problem contract but makes local results deterministic.

The left join examines every student. A row survives exactly when no department has the referenced ID, which is precisely the requested invalid-department condition.

#### Complexity detail

With an index or hash table on the department primary key, constructing or reading the lookup structure costs $O(D)$ and checking all students costs $O(S)$, for $O(N)$ time and $O(D)$ lookup space in the general model. Database indexes may already provide that lookup storage.

#### Alternatives and edge cases

- **`NOT EXISTS` anti-subquery:** A correlated existence test is semantically equivalent and often optimized to the same plan, but an unindexed nested scan can cost $O(DS)$.
- **`NOT IN` subquery:** This is concise, but nullable values in the subquery can make SQL's three-valued logic reject every row; the primary key is non-null here, though the anti-join remains clearer.
- **No invalid students:** The query correctly returns an empty result.
- **No departments:** Every student is unmatched and must be returned.
- **Repeated names:** Student identity comes from `id`; equal names remain separate output rows.

</details>
