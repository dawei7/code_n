## General
**Index records by employee ID**

Subordinate relationships contain IDs rather than direct record references. Build a hash map from each ID to its employee record so every relationship can be followed in constant expected time instead of rescanning the employee list.

**Traverse only the requested hierarchy**

Start a stack with the requested ID. Pop an ID, add that employee's importance, and push all direct subordinate IDs. Continue until the stack is empty. Employees outside this reachable hierarchy do not affect the result.

**Why every required importance is counted once**

The organization data forms a subordinate hierarchy, so each reachable employee has one management path from the requested root. The traversal follows every subordinate edge on those paths, reaching all direct and indirect subordinates. Because no reachable employee has two parents within the hierarchy, each ID is pushed once, and the accumulated total contains every required importance exactly once.

## Complexity detail
Building the map visits all `N` employee records. Traversing the selected hierarchy visits at most `N` employees and its subordinate links, for $O(N)$ time under the tree-shaped contract. The map and traversal stack use $O(N)$ space.

## Alternatives and edge cases
- **Breadth-first traversal:** use a queue with the same ID map; it has identical $O(N)$ time and space bounds.
- **Recursive DFS:** closely matches the hierarchy definition, but a deep management chain can exhaust recursion depth.
- **Linear search for every subordinate ID:** avoids the map but can take $O(N^2)$ time on a long chain.
- Importance values may be negative and must be added without filtering.
- Requesting a leaf employee returns only that employee's importance.
- Employees not reachable from the requested ID are intentionally excluded.
