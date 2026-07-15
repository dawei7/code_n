# Find Elements in a Contaminated Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1261 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/) |

## Problem Description

### Goal

A binary tree has been contaminated so that every node value is `-1`, but its shape is unchanged. Recover its intended values using these rules: the root has value `0`; a node with value `x` gives its left child `2 * x + 1` and its right child `2 * x + 2` whenever those children exist.

Design `FindElements` to recover the tree during construction and answer whether a requested `target` value occurs in the recovered tree. The app-local contract receives the contaminated root plus a sequence of targets and returns the result of each `find` query in order.

### Function Contract

**Inputs**

- `root`: the nonempty root of a contaminated binary tree containing $N$ nodes and height at most `20`.
- `queries`: $Q$ nonnegative target values, each at most $10^6$.

**Return value**

- Return a Boolean list of length $Q$ indicating whether each target occurs after recovery.

### Examples

**Example 1**

- Input: `root = [-1, null, -1]`, `queries = [1, 2]`
- Output: `[false, true]`

**Example 2**

- Input: `root = [-1, -1, -1, -1, -1]`, `queries = [1, 3, 5]`
- Output: `[true, true, false]`

**Example 3**

- Input: `root = [-1, null, -1, -1, null, -1]`, `queries = [2, 3, 4, 5]`
- Output: `[true, false, false, true]`

### Required Complexity

- **Time:** $O(N+Q)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

Traverse the existing tree once from the root. Assign value `0` to the root, and whenever a node with recovered value `x` has a child, compute the child's value from the stated left or right formula before adding it to the traversal stack.

**Index interpretation of recovered values**

The formulas are exactly the zero-based array indices of a binary heap. Therefore, the path from the root uniquely determines every recovered value, and no two nodes can receive the same value. Induction on depth proves the traversal assigns the required value to every existing node.

**Precompute membership for repeated queries**

Insert each recovered value into a hash set during traversal. A `find(target)` call then needs only a set-membership lookup rather than walking the tree again. The app wrapper constructs one recovered tree and reuses its set for every target in `queries`, preserving the stateful platform behavior.

Because the set contains exactly one value for every existing node and no value for a missing position, membership is true exactly for targets present in the recovered tree.

#### Complexity detail

Recovery visits the $N$ nodes once, and $Q$ expected constant-time hash lookups answer the queries, for $O(N+Q)$ total expected time. The traversal stack and recovered-value set use $O(N)$ space.

#### Alternatives and edge cases

- **Derive the target path per query:** The binary form of `target + 1` identifies left and right steps, allowing $O(h)$ query time and $O(1)$ preprocessing, but repeated queries cost more.
- **Linear recovered-value list:** It is easy to build, but each membership query may scan all $N$ values and produce $O(NQ)$ total time.
- **Single-node tree:** Only target `0` is present.
- **Sparse tree:** A numeric target is absent when any required child along its heap-index path is missing.
- **Repeated query:** It returns the same Boolean without changing recovered state.
- **Large absent target:** Hash lookup rejects it without traversing nonexistent levels.

</details>
