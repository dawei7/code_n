# Employee Importance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 690 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/employee-importance/) |

## Problem Description
### Goal
Each employee record contains a unique identifier, an importance value, and the identifiers of that employee's direct subordinates. Given the collection of employee records and one requested `id`, consider the complete reporting hierarchy beginning at that employee.

Return the total importance of the requested employee together with all direct and indirect subordinates. Count each employee in that hierarchy once, follow subordinate identifiers through as many levels as necessary, and do not include managers or employees outside the requested employee's descendant structure.

### Function Contract
**Inputs**

- `employees`: employee records with fields `id`, `importance`, and `subordinates`; local cases encode the platform objects as JSON records
- `id`: the employee ID whose complete subordinate hierarchy should be totaled

**Return value**

- The sum of importance values for the requested employee and all reachable subordinates

### Examples
**Example 1**

- Input: `employees = [{id:1, importance:5, subordinates:[2,3]}, {id:2, importance:3, subordinates:[]}, {id:3, importance:3, subordinates:[]}], id = 1`
- Output: `11`

**Example 2**

- Input: `employees = [{id:1, importance:2, subordinates:[2]}, {id:2, importance:4, subordinates:[]}], id = 2`
- Output: `4`

**Example 3**

- Input: `employees = [{id:1, importance:-5, subordinates:[2]}, {id:2, importance:2, subordinates:[]}], id = 1`
- Output: `-3`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Index records by employee ID**

Subordinate relationships contain IDs rather than direct record references. Build a hash map from each ID to its employee record so every relationship can be followed in constant expected time instead of rescanning the employee list.

**Traverse only the requested hierarchy**

Start a stack with the requested ID. Pop an ID, add that employee's importance, and push all direct subordinate IDs. Continue until the stack is empty. Employees outside this reachable hierarchy do not affect the result.

**Why every required importance is counted once**

The organization data forms a subordinate hierarchy, so each reachable employee has one management path from the requested root. The traversal follows every subordinate edge on those paths, reaching all direct and indirect subordinates. Because no reachable employee has two parents within the hierarchy, each ID is pushed once, and the accumulated total contains every required importance exactly once.

#### Complexity detail

Building the map visits all `N` employee records. Traversing the selected hierarchy visits at most `N` employees and its subordinate links, for $O(N)$ time under the tree-shaped contract. The map and traversal stack use $O(N)$ space.

#### Alternatives and edge cases

- **Breadth-first traversal:** use a queue with the same ID map; it has identical $O(N)$ time and space bounds.
- **Recursive DFS:** closely matches the hierarchy definition, but a deep management chain can exhaust recursion depth.
- **Linear search for every subordinate ID:** avoids the map but can take $O(N^2)$ time on a long chain.
- Importance values may be negative and must be added without filtering.
- Requesting a leaf employee returns only that employee's importance.
- Employees not reachable from the requested ID are intentionally excluded.

</details>
