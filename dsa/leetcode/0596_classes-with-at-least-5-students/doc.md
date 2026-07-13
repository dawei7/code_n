# Classes With at Least 5 Students

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 596 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/classes-with-at-least-5-students/) |

## Problem Description
### Goal
Given a `Courses` table in which each row associates a student with a class, find all classes that have at least five students enrolled. The `(student, class)` pair is unique, so one student contributes at most once to the count for a particular class.

Return the qualifying class names in a column named `class` and in any order. The threshold is inclusive: a class with exactly five students must be included, while a class with four or fewer students must be excluded.

### Function Contract
**Inputs**

- `Courses(student, class)`: student-to-class enrollment rows

**Return value**

- A one-column result grid named `class`
- Include a class when its distinct student count is at least five

### Examples
**Example 1**

- Input: Math has five enrolled students
- Output: `Math`

**Example 2**

- Input: Art has four enrolled students
- Output: no row for Art

**Example 3**

- Input: one student attends both Physics and Music
- Output: count that student once within each class independently

### Required Complexity

- **Time:** $O(n \log c)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Form one group per class**

Group enrollment rows by the `class` value. Each group then contains exactly the student associations relevant to that class.

**Count students and apply the threshold**

Use `COUNT(DISTINCT student)` and retain groups with a count of at least five through `HAVING`. Distinct counting states the semantic quantity directly and prevents repeated enrollment data from inflating a total.

**Why every returned class qualifies**

All rows for one class enter the same group, and no row from another class can enter it. The distinct aggregate therefore equals that class's enrolled-student count. The inclusive `HAVING` predicate keeps exactly counts five or greater.

**Order only for deterministic local output**

The platform permits any row order. Sorting class names stabilizes local fixtures without changing which groups qualify.

#### Complexity detail

For `n` enrollments and `c` classes, grouping and distinct counting generally use hashing or sorting in $O(n \log c)$ time and up to $O(n)$ working space. The final ordering of at most `c` class names fits within that bound.

#### Alternatives and edge cases

- **Deduplicate enrollments in a subquery first:** then use `COUNT(*)` per class; it has the same general complexity.
- **Correlated count per enrollment:** can rescan all courses for many rows and take $O(n^2)$ time.
- **Filter with `WHERE COUNT(...)`:** is invalid because aggregate filters belong in `HAVING`.
- **Exactly five students:** qualifies because the threshold is inclusive.
- **Four students:** does not qualify.
- **Student in several classes:** contributes independently to each class group.
- **Distinct counting:** prevents duplicate associations from changing the semantic count.
- **Several qualifying classes:** return every one of them.

</details>
