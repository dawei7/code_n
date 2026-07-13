# Binary Tree Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 257 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Backtracking, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-paths/) |

## Problem Description
### Goal
Given the root of a binary tree, enumerate every complete path that begins at the root and ends at a leaf. A leaf is a node with no left or right child, so paths must not stop early at internal nodes.

Return each path as a string containing its node values in traversal order, separated by `"->"`. Include every root-to-leaf branch once and return the path strings in any order. Negative and repeated node values should be formatted normally and do not merge distinct structural paths. A one-node tree returns that value alone without an arrow because the root is also a leaf.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

All root-to-leaf paths formatted with `->` between node values; path order is unrestricted.

### Examples
**Example 1**

- Input: `root = [1,2,3,null,5]`
- Output: `["1->2->5","1->3"]`

**Example 2**

- Input: `root = [1]`
- Output: `["1"]`

**Example 3**

- Input: `root = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(n + output)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Carry one root prefix down the DFS**

Append each visited value to the current textual prefix. At a leaf, store that complete path; otherwise recurse into every existing child.

On entry to a node, the prefix lists exactly the values from the root through that node in order. Each recursive call extends it with precisely one child.

**Leaves are the only complete paths**

DFS reaches each tree node once and hence reaches every leaf once. At a leaf, the carried prefix contains exactly its unique root-to-leaf chain, so emitting there produces a required path. Internal nodes do not emit, and every emitted endpoint is a leaf; the result therefore contains all and only the requested paths.

#### Complexity detail

Traversal visits `n` nodes and constructing returned strings costs their output length. Recursion stores one path of height `h`, excluding returned strings.

#### Alternatives and edge cases

- **Search from the root separately for every leaf:** repeats traversal and can take $O(n^2)$.
- An empty tree returns no paths; negative and multi-digit values use their normal decimal form.

</details>
