# Find Largest Value in Each Tree Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 515 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-largest-value-in-each-tree-row/) |

## Problem Description
### Goal
Given the root of a binary tree, group node values by their zero-based row or depth. The root occupies row zero, its children occupy row one, and each later row contains the existing children of nodes in the preceding row.

Return an array containing the largest value in each occupied row, ordered from the root row downward. Negative values compare normally, missing children add no placeholders, and each row contributes exactly one maximum. If the tree is empty, return an empty array; the function returns values rather than the nodes or their positions.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, or `null`

**Return value**

- One maximum value per nonempty tree level, from shallowest to deepest

### Examples
**Example 1**

- Input: `root = [1, 3, 2, 5, 3, null, 9]`
- Output: `[1, 3, 9]`

**Example 2**

- Input: `root = [1, 2, 3]`
- Output: `[1, 3]`

**Example 3**

- Input: `root = [1]`
- Output: `[1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Make queue boundaries coincide with tree rows**

Begin with the root in a queue. At the start of each outer iteration, capture the queue length; those entries are exactly the current depth. Remove precisely that many nodes while appending their children for the next iteration.

**Aggregate one maximum before advancing**

Initialize the row maximum from the first value actually removed, rather than from zero, so all-negative rows work correctly. Compare every remaining node on that row and append the final maximum only after the captured row count is exhausted.

**Why every output entry covers exactly one row**

Children are enqueued only while their parents' row is being consumed, so they cannot enter the current row's fixed iteration count. Conversely, every non-null child is appended once and appears in the next appropriate boundary. Each node therefore contributes to exactly one row maximum, and the outer loop appends those maxima in increasing depth order.

#### Complexity detail

Each of `n` nodes is enqueued, inspected, and dequeued once, giving $O(n)$ time. The queue holds at most the tree's maximum width, which is $O(n)$ in the worst case; the returned list uses at most $O(n)$ entries.

#### Alternatives and edge cases

- **Depth-first search with a depth-indexed result:** updates an existing maximum or appends the first value at a new depth in $O(n)$ time and $O(h)$ traversal space.
- **Repeated search by requested depth:** returns correct rows but can take $O(n^2)$ time on a chain.
- **Materialize complete rows first:** is easy to inspect but stores more intermediate values than the running maximum needs.
- **Empty tree:** returns an empty list.
- **All-negative row:** requires initialization from a node value, not zero.
- **Single node:** produces a one-element result.
- **Uneven branches:** depth, rather than parent position, determines the aggregation row.

</details>
