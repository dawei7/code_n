# Tree of Coprimes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1766 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Tree, Depth-First Search, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/tree-of-coprimes/) |

## Problem Description

### Goal

A connected, undirected, acyclic graph contains $n$ nodes numbered from $0$ through $n-1$ and is rooted at node $0$. The array `nums` assigns a positive integer value to each node, and every pair in `edges` joins two nodes of the tree.

Two values are coprime when their greatest common divisor is $1$. An ancestor of node `i` is another node on the unique shortest path from `i` to the root; a node is not its own ancestor.

For every node, find its closest ancestor whose value is coprime with the node's value. Return `-1` for a node having no such ancestor.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 50$.
- `edges`: exactly $n-1$ pairs `[u, v]`, each joining distinct node indices with $0 \le u,v<n$.
- Together, the edges form one connected tree rooted at node `0`.

**Return value**

- Return an integer array `answer` of length $n$.
- `answer[i]` is the index of the deepest proper ancestor of node `i` whose value has greatest common divisor $1$ with `nums[i]`, or `-1` if no such ancestor exists.

### Examples

**Example 1**

- Input: `nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]`
- Output: `[-1,0,0,1]`
- Explanation: Node `2` skips its value-`3` parent and uses node `0`; node `3` is coprime with its parent.

**Example 2**

- Input: `nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]`
- Output: `[-1,0,-1,0,0,0,-1]`
- Explanation: Each entry selects the nearest qualifying node on that node's path to root `0`.

**Example 3**

- Input: `nums = [7], edges = []`
- Output: `[-1]`
- Explanation: The root has no proper ancestors.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Exploit the bounded value universe**

Node values are restricted to the fixed set $\{1,\ldots,50\}$. Precompute, for every possible value, the list of values with which it is coprime. A node then needs to inspect possible values rather than an unbounded number of ancestors.

**Represent the current root path by value**

During a depth-first traversal, maintain one stack for each value. Its top entry stores the deepest active node on the current root-to-node path having that value. Older entries remain underneath so that the previous state can be restored after leaving a subtree.

**Select the deepest coprime entry**

Before adding the current node to the path state, inspect the precomputed coprime values for `nums[node]`. Each nonempty value stack contributes its deepest active node. Choose the candidate with greatest depth; it is precisely the closest coprime ancestor because depth orders all ancestors on one root path.

**Enter and leave each node exactly once**

After computing the answer, push `(node, depth)` onto the stack for its value and visit its children. On exit, pop that entry. This backtracking is essential: without it, a node from a completed sibling subtree could be mistaken for an ancestor.

**Use explicit entry and exit events**

An iterative DFS stack can store both entry and exit events. Push the exit event before the child entry events so the current node remains active throughout every descendant traversal, then is removed afterward. This preserves recursive backtracking semantics without risking Python's recursion limit on a chain of up to $10^5$ nodes.

For every entry event, the value stacks contain exactly the proper ancestors of that node and no other vertices. The deepest compatible entry is therefore the required answer. The push, descendant traversal, and matching pop preserve the same statement for every child and every later subtree.

#### Complexity detail

Let $V=50$ be the fixed value limit. Building the coprimality lists takes $O(V^2)$ time. Each of the $n$ nodes scans at most $V$ values and each edge is traversed a constant number of times, for $O(V^2+nV)=O(n)$ time because $V$ is constant.

The adjacency lists, answers, traversal events, and active path entries use $O(n)$ space. The coprimality table and $V$ value stacks add $O(V^2+n)$ entries overall, which remains $O(n)$.

#### Alternatives and edge cases

- **Scan the ancestor chain for every node:** Directly walking toward the root is simple and correct, but a chain can require $O(n^2)$ total work.
- **Copy a path map into every recursive call:** This avoids explicit restoration but can copy up to 50 states per node and creates unnecessary allocations.
- **Recursive depth-first search:** The same path-stack invariant works recursively, but a legal $10^5$-node chain can exceed Python's recursion depth.
- **Single node:** Root node `0` has no ancestor, so its answer is always `-1`.
- **Equal values:** A value greater than `1` is not coprime with itself; value `1` is coprime with every value, including `1`.
- **Nearest versus earliest:** The valid ancestor with greatest depth must be selected, not the first matching value considered.
- **Sibling subtrees:** Exit events must restore value stacks before traversal moves into a sibling branch.
- **Arbitrary edge order:** Rooting the undirected tree during traversal determines parent and child relationships.
- **No qualifying ancestor:** If every compatible value stack is empty, retain `-1`.

</details>
