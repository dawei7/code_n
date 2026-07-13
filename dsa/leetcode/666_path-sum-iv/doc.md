# Path Sum IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 666 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/path-sum-iv/) |

## Problem Description
### Goal
A binary tree of depth at most four is encoded as three-digit integers. In each number, the hundreds digit gives the node's one-based depth, the tens digit gives its one-based position within that level as if the tree were full, and the units digit gives the node's value.

Decode the connected tree described by the input and compute every root-to-leaf path sum. Return the sum of all those path sums. A node contributes separately to every leaf path passing through it, and only nodes present in the encoding belong to the tree.

### Function Contract
**Inputs**

- `nums`: a sorted list of unique three-digit encodings; the hundreds digit is depth, the tens digit is the 1-based position within that level, and the ones digit is the node value

**Return value**

- The sum of the value sums along all root-to-leaf paths

### Examples
**Example 1**

- Input: `nums = [113, 215, 221]`
- Output: `12`

**Example 2**

- Input: `nums = [113, 221]`
- Output: `4`

**Example 3**

- Input: `nums = [111]`
- Output: `1`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Decode positions into a direct lookup**

For each encoded integer, extract `(depth, position)` as its structural key and the ones digit as its value. Store these pairs in a hash map. A node at `(d, p)` has possible children $(d + 1, 2p - 1)$ and $(d + 1, 2p)$.

**Carry the path sum through existing nodes only**

Start at key `(1, 1)` with accumulated sum zero. At each node, add its value to the running path sum. If neither child key exists, the node is a leaf, so add the completed running sum to the answer. Otherwise visit each child that is present.

**Why every path contributes exactly once**

The encoding assigns every real node one unique structural key, and the child formulas reproduce the binary-tree parent relation. Traversal therefore reaches every encoded node through its unique parent. Every root-to-leaf path ends at one leaf and contributes when that leaf is visited; internal nodes never contribute prematurely. Summing those leaf contributions is exactly the requested total.

#### Complexity detail

Decoding and traversal each process all `N` encoded nodes once, giving $O(N)$ expected time. The lookup map and traversal stack use $O(N)$ space.

#### Alternatives and edge cases

- **Bottom-up leaf-count propagation:** count leaf descendants below each node and add `value * leaf_count`; this is also linear but less directly mirrors path sums.
- **Reconstruct every leaf path by scanning the input:** is correct but repeatedly searches for ancestors and can take $O(N^2)$ time.
- **Build explicit node objects:** works, but the positional keys already provide all required relationships without allocation overhead.
- A one-node tree has one path consisting of the root value.
- Node values may be zero and still define real nodes.
- A missing left or right child does not prevent the other child from continuing a path.
- The tens digit is a level-relative position, not a global heap-array index.

</details>
