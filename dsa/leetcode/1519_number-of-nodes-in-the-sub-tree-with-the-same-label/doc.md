# Number of Nodes in the Sub-Tree With the Same Label

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1519 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/) |

## Problem Description
### Goal

An undirected tree has `n` nodes numbered from 0 through `n - 1`, exactly `n - 1` edges, and root node 0. The character `labels[i]` is the lowercase English label assigned to node `i`.

For every node `i`, consider the rooted subtree containing `i` and all descendants reached away from node 0. Count how many nodes in that subtree have the same label as `i`, including `i` itself, and return the $n$ counts in node-number order.

### Function Contract
**Inputs**

- `n`: The node count, where $1 \leq n \leq 10^5$.
- `edges`: Exactly $n-1$ pairs `[a, b]` describing a connected, acyclic, undirected graph over nodes 0 through `n - 1`.
- `labels`: A length-$n$ string of lowercase English letters; position `i` labels node `i`.
- Node 0 defines the root and therefore every parent-descendant relationship.

**Return value**

Return an integer list `answer` of length $n$, where `answer[i]` is the number of nodes labeled `labels[i]` in the rooted subtree of node `i`.

### Examples
**Example 1**

- Input: `n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"`
- Output: `[2,1,1,1,1,1,1]`
- Explanation: Node 0 and descendant node 2 share label `a`; every other node is the only occurrence of its own label in its subtree.

**Example 2**

- Input: `n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"`
- Output: `[4,2,1,1]`
- Explanation: Every node has label `b`, so each answer is its subtree size.

**Example 3**

- Input: `n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"`
- Output: `[3,2,1,1,1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn subtree counting into counter differences**

Maintain one 26-entry array `seen`, where each entry records how many nodes of that label have been entered during depth-first traversal. Immediately before entering node `u`, save the current counter for `labels[u]`; then increment it for `u`.

Depth-first traversal processes every node in `u`'s subtree between `u`'s entry and exit events. Consequently, at the exit event, the current counter minus the saved entry value is exactly the number of matching labels introduced by that contiguous subtree interval. Store this difference at `answer[u]`.

Counts from previously completed sibling subtrees do not contaminate the result: they are already present in both the entry snapshot and the exit total, so subtraction cancels them.

**Use explicit enter and exit events**

Build an adjacency list for the undirected edges. Each stack item stores a node, its parent, and whether the item represents entry or exit. On entry, record the snapshot, increment the label count, push the node's exit event, and then push every neighbor except its parent as a child entry.

Placing the exit event below all child entries ensures it is popped only after the entire rooted subtree has been visited. Tracking the parent orients the undirected tree without constructing separate child lists and prevents immediately traversing an edge backward.

This iterative formulation avoids Python recursion depth failures on a legal chain of up to $10^5$ nodes.

#### Complexity detail

Building adjacency lists touches $n-1$ edges twice. Every node receives one entry and one exit event, and all label operations are constant time over a fixed alphabet. Total time is $O(n)$.

The adjacency lists, answer and snapshot arrays, and explicit traversal stack each use $O(n)$ space. The 26-entry label counter is constant-sized.

#### Alternatives and edge cases

- **Postorder frequency vectors:** merge a 26-entry child vector into its parent. This is also linear for a fixed alphabet, but performs 26 additions per edge and stores more counter state.
- **One subtree search per node:** independently traversing every rooted subtree is correct but takes $O(n^2)$ time on a chain.
- **Recursive DFS:** conceptually concise, but a depth-$10^5$ tree exceeds ordinary Python recursion limits.
- **Single node:** its subtree contains itself, so the only answer is 1.
- **All labels equal:** every answer equals that node's rooted subtree size.
- **All relevant labels distinct:** every node counts only itself.
- **Edge order:** input pairs are undirected and may appear in any order; node 0 alone determines orientation.
- **Sibling labels:** equal labels in a sibling's subtree are outside the current subtree and cancel through the entry snapshot.

</details>
