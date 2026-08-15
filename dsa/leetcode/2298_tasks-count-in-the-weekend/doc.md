# Tasks Count in the Weekend

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2298 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/tasks-count-in-the-weekend/) |

## Problem Description

### Goal

The `Tasks` table stores submitted work. Each row identifies a task with its
unique `task_id`, records the responsible `assignee_id`, and gives the calendar
date on which it was submitted.

Classify every task by its submission day. Saturday and Sunday are weekend
days; Monday through Friday are working days. Return one row containing the
number of weekend submissions as `weekend_cnt` and the number of working-day
submissions as `working_cnt`. The assignee does not affect either count.

### Function Contract

**Inputs**

- `Tasks`: Rows with unique integer `task_id`, integer `assignee_id`, and date-valued `submit_date`.

Let $r$ be the number of task rows.

**Return value**

One row with columns `weekend_cnt` and `working_cnt`, partitioning all tasks by
the day of week of `submit_date`.

### Examples

#### Example 1

- **Input:** tasks submitted on Monday, Tuesday, Wednesday, Saturday, Sunday, and Sunday
- **Output:** `weekend_cnt = 3, working_cnt = 3`

#### Example 2

- **Input:** three tasks submitted from Monday through Friday
- **Output:** `weekend_cnt = 0, working_cnt = 3`

#### Example 3

- **Input:** tasks submitted on one Saturday and one Sunday
- **Output:** `weekend_cnt = 2, working_cnt = 0`
