# Path In Zigzag Labelled Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1104 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/) |

## Problem Description

### Goal

Consider an infinite binary tree in which every node has two children. Nodes are labelled one row at a time. Odd-numbered rows—the first, third, fifth, and so on—are labelled from left to right, while even-numbered rows are labelled from right to left.

Given one node's `label`, return the sequence of labels on the unique path from the root to that node, including both endpoints.

### Function Contract

**Inputs**

- `label`: the target label $L$, where $1 \leq L \leq 10^6$.

The zero-based depth of the target is $d = \lfloor \log_2 L \rfloor$.

**Return value**

A list of $d+1$ labels ordered from the root to the node labelled $L$.

### Examples

**Example 1**

- Input: `label = 14`
- Output: `[1, 3, 4, 14]`

**Example 2**

- Input: `label = 26`
- Output: `[1, 2, 6, 10, 26]`

### Required Complexity

- **Time:** $O(\log L)$
- **Space:** $O(\log L)$

<details>
<summary>Approach</summary>

#### General

**Identify the current level's numeric range.** A label $x$ at zero-based depth $h=\lfloor\log_2 x\rfloor$ belongs to the ordinary row range

$$
[2^h,\;2^{h+1}-1].
$$

Zigzag ordering reverses positions on alternating rows, but the same labels remain in that range.

**Mirror before moving to the parent.** Within a row whose endpoints are `start` and `end`, the mirror of `x` is `start + end - x`. In ordinary left-to-right labelling, the mirrored node's parent is obtained by integer division by two. Therefore the zigzag parent is computed directly as `label = (start + end - label) // 2`.

**Climb and reverse.** Append the current label, replace it by its zigzag parent, and repeat until the root has been appended. This produces the path from target to root; reversing it gives the requested order.

Mirroring maps the displayed zigzag position to the corresponding ordinary-tree label at the same position. Ordinary integer division then selects exactly that position's parent. Applying this transformation at every depth follows the unique tree edges to the root, so reversing the collected labels yields precisely the root-to-target path.

#### Complexity detail

Each parent step decreases the depth by one, so there are $d+1=O(\log L)$ iterations. The returned path stores one label per level and therefore uses $O(\log L)$ space; all other state is constant-size.

#### Alternatives and edge cases

- **Materialize labelled rows:** Building every row through the target preserves tree positions but costs $O(L)$ time and space.
- **Convert the entire path to ordinary labels:** Mirror the target based on row parity, compute ordinary ancestors, then mirror selected levels back; it has the same asymptotic complexity but more parity bookkeeping.
- **Root label:** For `label = 1`, the loop records only `[1]`.
- **Level endpoints:** The leftmost and rightmost numeric labels mirror to one another, so both powers of two and values just below them test the formula's boundaries.
- **Alternating direction:** The endpoint-sum formula works on every row without a separate odd/even branch.

</details>
