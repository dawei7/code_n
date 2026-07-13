# Nth Highest Salary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 177 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/nth-highest-salary/) |

## Problem Description
### Goal
The `Employee` table stores employee identifiers and salaries that may repeat. For a positive one-based integer `N`, rank the distinct salary values from highest to lowest and select the value at rank `N`.

Implement the database function `getNthHighestSalary(N)` so it returns that distinct salary, or `NULL` when fewer than `N` different values exist. Duplicate employee salaries occupy one rank rather than several consecutive ranks. The app fixtures provide `N` through a request table while preserving the same result semantics, including $N = 1$ selecting the maximum salary and an empty employee table producing `NULL`.

### Function Contract
**Inputs**

- `Employee(id, salary)`: employee salary rows with possible duplicates
- `N`: positive one-based rank; app fixtures expose it as `Request(N)` while the native MySQL artifact receives a function parameter

**Return value**

The Nth-highest distinct salary as `getNthHighestSalary`, or null when that rank is absent.

### Examples
**Example 1**

- Salaries: `100, 200, 300`; $N = 2$
- Output: `200`

**Example 2**

- Salaries: `100`; $N = 2$
- Output: `null`

**Example 3**

- Salaries: `100, 100, 200`; $N = 2$
- Output: `100`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

The requested rank belongs to salary **values**, not employee rows. Begin by reducing the salaries to a distinct relation; otherwise three employees earning the maximum would incorrectly occupy the first three positions.

Order those distinct values from highest to lowest. In that sequence, one-based rank `N` is at zero-based offset $N - 1$. The native MySQL function can adjust its parameter to that offset and select one row with `LIMIT`. The app-local SQL fixture expresses the same operation using `Request(N)`.

The selected row should be evaluated as a scalar subquery. A scalar subquery returns `NULL` when it produces no row, which is exactly the required outcome when the number of distinct salaries is smaller than `N`. Without that wrapper, an offset beyond the data would produce an empty result set rather than one result row containing null.

For salaries `300, 300, 200, 100` and $N = 2$, deduplication gives `300, 200, 100`; descending offset one selects `200`. The duplicate maximum never changes any rank.

After `DISTINCT`, each salary value appears exactly once. Descending order places precisely $N - 1$ greater distinct salaries before the value at offset $N - 1$, so that value is the Nth-highest distinct salary. If the offset does not exist, fewer than `N` distinct values are present, and scalar-subquery null semantics return the specified fallback. Thus the query is correct in both the present and absent-rank cases.

#### Complexity detail

Without a supporting index, deduplicating and sorting `n` salaries requires $O(n \log n)$ logical work and up to $O(n)$ intermediate storage. A suitable salary index may let the engine obtain distinct values in descending order more efficiently; physical costs remain optimizer-dependent.

#### Alternatives and edge cases

- `DENSE_RANK()` expresses the definition directly, but the query must still isolate rank `N` and preserve one-row null behavior.
- Counting distinct greater salaries can avoid an explicit offset, though a correlated formulation may be quadratic without optimization.
- Repeated nested `MAX` queries work for a fixed small rank but do not generalize cleanly to arbitrary `N`.
- Omitting `DISTINCT` ranks employees rather than salary levels and is incorrect when salaries repeat.
- `N` is positive and one-based. $N = 1$ requests the maximum; an empty or undersized distinct set yields `NULL`.

</details>
