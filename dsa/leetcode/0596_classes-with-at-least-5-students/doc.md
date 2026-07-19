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
