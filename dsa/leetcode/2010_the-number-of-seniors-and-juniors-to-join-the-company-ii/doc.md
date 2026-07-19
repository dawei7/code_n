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

### Required Complexity

- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Compute the cost of every salary prefix.** Partition candidates by
`experience`, order each partition by `salary`, and use a windowed cumulative
sum. A candidate's `running_salary` is therefore the exact cost of hiring that
candidate together with every cheaper candidate from the same category.

**Reserve the senior spending before filtering juniors.** Among senior rows
whose cumulative salary does not exceed $70{,}000$, the maximum cumulative
value is the amount committed to seniors; use zero when no senior qualifies.
Return all such senior rows. A junior qualifies when its own cumulative salary
does not exceed `70000 - senior_spending`.

Because salaries are unique, ascending order defines one unambiguous prefix
per category. The company rules hire exactly the longest affordable senior
prefix, then the longest junior prefix under the remainder. The two cumulative
conditions select precisely those prefixes, so every returned ID is hired and
every omitted candidate is either beyond the first unaffordable prefix or
belongs to no affordable prefix.

#### Complexity detail

Here $R$ is the number of candidate rows. Partitioned ordering for the window
sum takes $O(R\log R)$ time; the remaining aggregation and filtering are
linear. The ranked intermediate relation contains $R$ rows and uses $O(R)$
space.

#### Alternatives and edge cases

- **Correlated prefix sums:** Recomputing the total of every cheaper candidate
  for each row is correct but can require $O(R^2)$ row comparisons.
- **Procedural salary loop:** Repeatedly querying the next cheapest candidate
  mirrors the story but introduces unnecessary iterative database round trips.
- If no senior fits, senior spending is zero and juniors use the entire
  budget.
- If seniors spend exactly $70{,}000$, no junior can be returned.
- The result may be empty when neither category has an affordable first
  candidate.

</details>
