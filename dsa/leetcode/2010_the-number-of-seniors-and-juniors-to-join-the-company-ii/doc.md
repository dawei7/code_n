# The Number of Seniors and Juniors to Join the Company II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2010 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company-ii/) |

## Problem Description

### Goal

The `Candidates` table records each applicant's unique `employee_id`,
experience category, and unique monthly salary. Experience is either `Senior`
or `Junior`.

The company has a salary budget of $70{,}000$. It first hires seniors in
ascending salary order until the next senior no longer fits. It then spends
the remaining budget on juniors, again taking the lowest salaries in order
until the next one is unaffordable. Return the employee IDs of every candidate
hired by this senior-first process. The result rows may appear in any order.

### Function Contract

Let $R$ be the number of rows in `Candidates`.

**Inputs**

- `Candidates(employee_id, experience, salary)`, where `employee_id` and
  `salary` are unique and `experience` is either `Senior` or `Junior`.

**Return value**

Return a one-column table named `employee_id` containing exactly the selected
senior and junior IDs.

### Examples

**Example 1**

- Input: seniors `(11, 16000)`, `(2, 20000)`, `(13, 50000)` and juniors
  `(1, 10000)`, `(9, 15000)`, `(4, 40000)`
- Output: employee IDs `11`, `2`, `1`, and `9`
- Explanation: The two seniors cost $36{,}000$; the remaining $34{,}000$
  admits the two cheapest juniors.

**Example 2**

- Input: all senior salaries exceed $70{,}000$; junior salaries are
  $10{,}000$, $25{,}000$, and $30{,}000$
- Output: all three junior employee IDs
- Explanation: No senior is affordable, so the juniors receive the full
  budget.

**Example 3**

- Input: senior salaries $30{,}000$ and $40{,}000$, plus a junior salary of
  $1$
- Output: the two senior employee IDs
- Explanation: The seniors consume the budget exactly, leaving nothing for the
  junior.
