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

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Translate maximum count into cheapest prefixes.** Within one experience group, hiring the cheapest salaries first maximizes how many candidates fit any fixed budget. Order each group by `salary`, using `employee_id` only as a deterministic tie-breaker, and compute a cumulative salary with a partitioned window function.

**Reserve the senior budget first.** Among senior rows, every cumulative total at most $70{,}000$ represents an affordable prefix. Count those rows and take the largest qualifying cumulative total as senior spending. Aggregating this filtered set still returns one row when no senior qualifies; `COALESCE` converts its missing spending total to zero.

**Apply only the remainder to juniors.** Cross join the one-row senior summary to the ranked candidates. Count junior rows whose own cumulative salary is at most `70000 - senior_spending`. Emit the senior count and junior count with `UNION ALL`, guaranteeing both required experience rows even when either count is zero.

The senior result is maximal because no set of the same size can cost less than the cheapest prefix. Once that prefix is fixed, the identical argument makes the affordable junior prefix maximal under the remaining budget.

#### Complexity detail

Partition ordering for the window calculation takes $O(N\log N)$ time in the general database execution model. The filtered aggregates and final union scan the ranked rows linearly. Materializing window state and sorted partitions may use $O(N)$ space.

#### Alternatives and edge cases

- **Correlated cumulative subquery:** Recomputing the cheaper-prefix sum for every candidate is correct but can require $O(N^2)$ row comparisons.
- **Maximize total hires across both groups:** This violates the required senior-first priority; juniors may be considered only after the senior count is maximal.
- A salary equal to the remaining budget is affordable because spending must not exceed $70{,}000$.
- When no senior fits, all $70{,}000$ remains available to juniors.
- When seniors consume the full budget, the junior result must still appear with count zero.
- Equal salaries do not change the maximum count; the unique employee identifier supplies stable window ordering.

</details>
