# Sum Root to Leaf Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 129 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-root-to-leaf-numbers/) |

## Problem Description
### Goal
Given a binary tree whose node values are decimal digits from `0` through `9`, interpret every complete root-to-leaf path as one base-ten number. Reading downward supplies the digits from most significant to least significant, so the path $1 \to 2 \to 3$ represents `123`.

Return the sum of the numbers represented by all root-to-leaf paths. Shared prefixes contribute independently to every path that continues from them, and only leaves terminate numbers; an internal prefix is not an additional value. Leading zero digits are valid and simply do not change the numeric value. An empty tree contributes no paths and returns `0`.

### Function Contract
**Inputs**

- `root`: a `TreeNode` whose values are digits `0..9`, encoded as a level-order list in app cases

**Return value**

The sum of the numbers represented by every root-to-leaf path.

### Examples
**Example 1**

- Input: `root = [1, 2, 3]`
- Output: `25`

**Example 2**

- Input: `root = [4, 9, 0, 5, 1]`
- Output: `1026`

**Example 3**

- Input: `root = [0]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Appending a digit is one arithmetic state transition**

When descending from prefix value `p` to node digit `d`, compute $10 \cdot p + d$. Multiplication shifts every existing decimal digit one place left, and addition fills the new units place. No path string or digit list is needed.

**Only leaves terminate numbers in the sum**

At a node with neither child, add its accumulated value to the total. A node with one child is not a leaf, and an internal prefix is not a separate number. Push each existing child with the newly computed prefix.

**Every pending value belongs to one unique root path**

Every stack pair `(node, value)` stores exactly the decimal number formed by that node's unique root-to-node digit sequence. Different branches carry independent integer values, so no mutable path restoration is required.

**Trace two numbers sharing a prefix**

Path `1 -> 2` forms `12`, and path `1 -> 3` forms `13`. Both end at leaves, so the returned sum is $12 + 13 = 25$.

**The base-ten update is the exact path prefix value**

If the parent path represents `p`, appending child digit `d` produces $10p + d$, exactly the decimal value of the extended root path. Carrying that value downward therefore keeps every prefix exact.

DFS reaches each leaf through its unique root path once. Adding only at leaves contributes each complete root-to-leaf number exactly once, so their accumulated sum matches the contract.

#### Complexity detail

Each of `n` nodes is processed once, giving $O(n)$ time. Depth-first pending work is bounded by $O(h)$, where `h` is tree height.

#### Alternatives and edge cases

- **Store digit paths then parse:** uses additional path memory and conversion work.
- **Breadth-first traversal:** is correct but can store $O(w)$ nodes in a wide tree.
- **Sum internal prefixes:** double-counts incomplete root-to-leaf paths.
- A root digit zero and leading zeroes on a path are handled naturally by arithmetic; they do not create a separate textual representation issue.
- Empty input conventionally contributes sum zero. A single node contributes exactly its digit.

</details>
