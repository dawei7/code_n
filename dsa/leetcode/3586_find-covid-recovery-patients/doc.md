# Find COVID Recovery Patients

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3586 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-covid-recovery-patients/) |

## Problem Description

### Goal

Identify patients who recovered from COVID according to their recorded tests. For each patient, begin with their earliest test whose result is `Positive`. The patient qualifies only when they later have a `Negative` result on a strictly later calendar date. Negatives before the first positive, negatives on that same date, and `Inconclusive` results do not establish recovery.

For every qualifying patient, select the earliest negative date after the first positive date and report the elapsed number of days as `recovery_time`. Include the patient's identifier, name, and age. Sort shorter recovery times first, then sort equal times by `patient_name` in ascending order.

### Function Contract

**Inputs**

The database provides these tables:

- `patients(patient_id, patient_name, age)`: One row per patient; `patient_id` is unique.
- `covid_tests(test_id, patient_id, test_date, result)`: One row per test; `test_id` is unique and `result` is `Positive`, `Negative`, or `Inconclusive`.

**Return value**

Return the columns `patient_id`, `patient_name`, `age`, and `recovery_time` for recovered patients, ordered by `recovery_time ASC, patient_name ASC`.

### Examples

**Example 1**

Given patients Alice Smith, Bob Johnson, Carol Davis, David Wilson, and Emma Brown, Alice's first positive-to-later-negative interval is 10 days, Bob's is 11 days, and Carol's is 10 days. David has no later negative, while Emma has no positive.

- Output rows: `(1, "Alice Smith", 28, 10)`, `(3, "Carol Davis", 42, 10)`, `(2, "Bob Johnson", 35, 11)`
- Explanation: The two 10-day recoveries appear first and are tied by ascending patient name.

---
