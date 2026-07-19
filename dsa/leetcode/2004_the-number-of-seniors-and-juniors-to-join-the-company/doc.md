# The Number of Seniors and Juniors to Join the Company

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2004 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company/) |

## Problem Description

### Goal

Table `Candidates` lists applicants, each classified as either `Senior` or `Junior`, together with a monthly salary. The company has a total salary budget of $70{,}000$.

Hiring follows a strict priority. First, select the largest possible number of senior candidates without exceeding the budget. Only after maximizing that senior count may the unspent portion be used to select the largest possible number of juniors. Report the number hired from both experience groups, including a zero when a group receives no hires.

### Function Contract

**Inputs**

- `Candidates(employee_id, experience, salary)`.
- `employee_id` is unique.
- `experience` is either `'Senior'` or `'Junior'`.
- `salary` is the candidate's monthly salary.
- Let $N$ be the number of candidate rows.

**Return value**

Return two rows with columns `experience` and `accepted_candidates`: one row for `'Senior'` and one for `'Junior'`. Row order is unrestricted.

### Examples

**Example 1**

- Input: seniors with salaries `20000, 20000, 50000`; juniors with salaries `10000, 10000, 40000`
- Output: `Senior | 2` and `Junior | 2`
- Explanation: The two cheapest seniors cost $40{,}000$. The remaining $30{,}000$ pays for the two cheapest juniors.

**Example 2**

- Input: three seniors each costing `80000`; juniors costing `10000, 10000, 40000`
- Output: `Senior | 0` and `Junior | 3`
- Explanation: No senior fits, leaving the entire budget for all three juniors.
