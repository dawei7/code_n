# Time Needed to Inform All Employees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1376 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/time-needed-to-inform-all-employees/) |

## Problem Description

### Goal

A company has `n` employees numbered from `0` to `n - 1`. One employee, identified by `headID`, leads the company. For every other employee, `manager[i]` gives that employee's direct manager, while the head has manager `-1`. These relationships form a tree rooted at the head.

The head begins with urgent news. When employee `i` receives it, that employee needs `informTime[i]` minutes to notify all direct reports simultaneously; those reports can then repeat the process. Return the number of minutes until every employee has received the news.

### Function Contract

**Inputs**

- `n`: the number of employees, whose identifiers range from `0` through `n - 1`.
- `headID`: the identifier of the company's head.
- `manager`: an array where `manager[i]` is employee `i`'s direct manager and `manager[headID] == -1`.
- `informTime`: an array where `informTime[i]` is the simultaneous notification delay for employee `i`'s direct reports.

**Return value**

- The total time required for the news to reach every employee.

### Examples

**Example 1**

- Input: `n = 1, headID = 0, manager = [-1], informTime = [0]`
- Output: `0`

**Example 2**

- Input: `n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]`
- Output: `1`

**Example 3**

- Input: `n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]`
- Output: `21`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn manager links into downward edges.** The input points from each employee to a manager, but information travels in the opposite direction. Build a list of direct reports for every manager in one pass.

**Carry each employee's receipt time.** Start an iterative depth-first traversal with the head at time zero. If a manager receives the news at time `elapsed`, every direct report receives it at `elapsed + informTime[manager]` because those notifications occur simultaneously. Push each report with that arrival time and track the greatest arrival seen.

Every employee has exactly one path from the head. Summing the manager delays along that path therefore gives its unique receipt time, and the traversal computes that sum once per edge. The maximum receipt time is exactly the first moment at which nobody remains uninformed.

#### Complexity detail

Building the report lists and traversing the organization each touch all `n` employees once, so time is $O(n)$. The adjacency lists and traversal stack together use $O(n)$ space.

#### Alternatives and edge cases

- **Search for reports repeatedly:** Scan the full `manager` array whenever an employee is processed. This avoids stored adjacency lists but takes $O(n^2)$ time.
- **Walk upward from every employee:** Sum manager delays separately for each employee. Shared chains are repeated and can also take $O(n^2)$ time.
- **Breadth-first traversal:** A queue carrying receipt times is equally correct and has the same asymptotic bounds.
- **Recursive depth-first search:** The recurrence is natural, but a long management chain can exceed the language recursion limit.
- **Single employee:** The head already knows the news, so the result is zero.
- **Simultaneous reports:** A manager's delay is paid once along each path, not multiplied by the number of direct reports.
- **Leaf employees:** Their `informTime` does not extend the answer because they have nobody else to notify.

</details>
