# Remove Methods From Project

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3310 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-methods-from-project/) |

## Problem Description

### Goal

A project contains `n` methods numbered from `0` through `n - 1`. Each pair `[a, b]` in `invocations` is directed: method `a` invokes method `b`. A known bug begins at method `k`, so `k` and every method reachable from it through one or more invocation edges are suspicious.

The entire suspicious group may be removed only when no method outside that group invokes a method inside it. If that condition holds, return all nonsuspicious methods. If even one outside-to-inside invocation exists, removing all suspicious methods is impossible and no method may be removed, so return every method. The returned methods may appear in any order.

### Function Contract

**Inputs**

- `n`: The number of methods, where $1\leq n\leq10^5$.
- `k`: The initially buggy method, where $0\leq k<n$.
- `invocations`: Up to $2\cdot10^5$ distinct directed pairs `[a, b]`, with $0\leq a,b<n$ and $a\neq b$.

**Return value**

Return all remaining method numbers after applying the all-or-nothing removal rule. Any output order is valid.

### Examples

#### Example 1

- **Input:** `n = 4, k = 1, invocations = [[1, 2], [0, 1], [3, 2]]`
- **Output:** `[0, 1, 2, 3]`

Methods 1 and 2 are suspicious, but methods 0 and 3 invoke that group, so nothing can be removed.

#### Example 2

- **Input:** `n = 5, k = 0, invocations = [[1, 2], [0, 2], [0, 1], [3, 4]]`
- **Output:** `[3, 4]`

The suspicious set is `{0, 1, 2}` and has no incoming invocation from methods 3 or 4.

#### Example 3

- **Input:** `n = 3, k = 2, invocations = [[1, 2], [0, 1], [2, 0]]`
- **Output:** `[]`

Every method is reachable from method 2, so all methods may be removed.
