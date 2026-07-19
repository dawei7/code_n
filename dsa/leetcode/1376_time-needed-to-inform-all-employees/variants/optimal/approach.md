## General
**Turn manager links into downward edges.** The input points from each employee to a manager, but information travels in the opposite direction. Build a list of direct reports for every manager in one pass.

**Carry each employee's receipt time.** Start an iterative depth-first traversal with the head at time zero. If a manager receives the news at time `elapsed`, every direct report receives it at `elapsed + informTime[manager]` because those notifications occur simultaneously. Push each report with that arrival time and track the greatest arrival seen.

Every employee has exactly one path from the head. Summing the manager delays along that path therefore gives its unique receipt time, and the traversal computes that sum once per edge. The maximum receipt time is exactly the first moment at which nobody remains uninformed.

## Complexity detail
Building the report lists and traversing the organization each touch all `n` employees once, so time is $O(n)$. The adjacency lists and traversal stack together use $O(n)$ space.

## Alternatives and edge cases
- **Search for reports repeatedly:** Scan the full `manager` array whenever an employee is processed. This avoids stored adjacency lists but takes $O(n^2)$ time.
- **Walk upward from every employee:** Sum manager delays separately for each employee. Shared chains are repeated and can also take $O(n^2)$ time.
- **Breadth-first traversal:** A queue carrying receipt times is equally correct and has the same asymptotic bounds.
- **Recursive depth-first search:** The recurrence is natural, but a long management chain can exceed the language recursion limit.
- **Single employee:** The head already knows the news, so the result is zero.
- **Simultaneous reports:** A manager's delay is paid once along each path, not multiplied by the number of direct reports.
- **Leaf employees:** Their `informTime` does not extend the answer because they have nobody else to notify.
