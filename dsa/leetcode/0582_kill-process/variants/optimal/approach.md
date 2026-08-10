## General

The two input lists encode a rooted tree, but they do so as parent-child pairs rather than as a structure that can be traversed downward efficiently. At index `i`, process `pid[i]` has parent `ppid[i]`. Killing one process means returning exactly the subtree rooted at `kill`: the root itself, all direct children, all grandchildren, and so on.

The solution therefore has two phases:

1. convert the parallel lists into an adjacency list mapping each parent ID to its direct children;
2. run depth-first search from `kill` and collect every reachable process.

This avoids repeatedly scanning all parent entries whenever a new descendant is found.

**Building the parent-to-children map**

`g = defaultdict(list)` creates a mapping whose missing values automatically become empty lists. The loop

```python
for i, p in zip(pid, ppid):
    g[p].append(i)
```

reads corresponding entries together. Here `i` is a process ID, not a list index, and `p` is that process’s parent ID. Appending `i` to `g[p]` records one directed edge from parent `p` to child `i`.

For the sample pairs, the relation includes `3 -> 1`, `0 -> 3`, `5 -> 10`, and `3 -> 5`. Parent 0 is a sentinel meaning “no real parent.” Recording the root under `g[0]` is harmless because the search starts at the requested positive process ID, not at 0. There is no need for a special case while building the map.

The tree guarantees are important. Every process ID is unique and every process has only one parent, so a process is appended as a child exactly once. There is only one root and no cycles in the intended structure. Those facts mean downward traversal cannot reach a process along two different paths.

**Depth-first traversal**

The nested function `dfs(i)` performs preorder traversal:

```python
ans.append(i)
for j in g[i]:
    dfs(j)
```

It first appends the current process because killing `i` always kills `i` itself. It then recursively visits every direct child listed in `g[i]`. Each child call repeats the rule, so descendants at every depth are reached.

When `i` is a leaf, it may not yet be a key in `g`. Accessing `g[i]` through a `defaultdict(list)` creates and returns an empty list, the loop has no iterations, and recursion stops naturally. No separate “if key exists” branch is required.

The result order is preorder according to the children’s input order, but the problem accepts any order. The algorithm does not spend time sorting because ordering conveys no required meaning.

**Tracing the sample**

For `kill = 5`, `dfs(5)` first appends 5. The adjacency list for 5 contains 10, so it calls `dfs(10)`. That call appends 10 and finds no children. The resulting list is `[5, 10]`.

Notice that process 3 is an ancestor of 5 and process 1 is in a different branch under 3. Traversal follows only edges from a process to its children. It never moves upward to 3, so it never crosses into sibling branch 1. That is exactly the meaning of killing a subtree rather than the entire process tree.

**Why the algorithm is correct**

First, every ID appended by the search must be killed. The initial appended ID is `kill` itself. Every later appended ID is reached by following one or more parent-to-child edges from `kill`, so it is a direct or indirect descendant. The rule says all such descendants die.

Second, every process that must be killed is appended. Consider a descendant at depth $d$ below `kill`. At depth zero, `kill` is appended by the first call. Assume every descendant at depth $d$ is visited. The construction placed all of each visited node’s direct children in its adjacency list, and the loop calls `dfs` on every one. Therefore, every descendant at depth $d+1$ is visited and appended. By induction, all depths in the subtree are covered.

Finally, no ID is appended twice. The input forms a tree, so each non-root process has one parent and there is one unique downward path from `kill` to any descendant. The recursion therefore reaches each subtree node exactly once. Together, these facts prove that `ans` contains exactly the required set.

It is useful to distinguish the cost of preparing the whole tree from traversing the killed subtree. Even if `kill` is a leaf, the solution still reads all input pairs to build `g`. That up-front cost supports constant-expected-time child lookup during traversal.

## Complexity detail

Let $n$ be the total number of processes, let $k$ be the number of processes in the subtree rooted at `kill`, and let $h$ be that subtree’s height.

Building the adjacency list processes $n$ pairs and performs expected $O(1)$ hash-map/list work per pair, so it takes expected $O(n)$ time. DFS visits each of the $k$ killed processes once and scans exactly the child edges inside that subtree, taking $O(k)$ time. Since $k\le n$, total time is $O(n+k)=O(n)$.

The adjacency lists store $n$ child entries, including the root under sentinel parent 0, so they use $O(n)$ space. The returned list uses $O(k)$ output space. Recursive calls use $O(h)$ stack space, with $h$ as large as $n$ for a chain. Overall auxiliary storage is $O(n)$, matching the manifest.

Hash-map operations are expected constant time. A theoretical collision-heavy implementation could be worse, but standard interview analysis uses expected hashing cost.

## Alternatives and edge cases

- **Breadth-first search:** After building the same adjacency list, use a queue starting with `kill`. It has the same $O(n)$ time and space and avoids recursive call-stack depth.
- **Iterative depth-first search:** A manual stack preserves DFS behavior while safely handling a chain of tens of thousands of processes.
- **Repeated scans of `ppid`:** For every killed process, scan the full arrays to find children. It needs no adjacency map but can take $O(n^2)$ time when most processes are killed.
- **Explicit node objects:** Building a node instance and child list for every process works but stores more structure than the ID-to-child-list map needs.
- **Killing a leaf:** Its adjacency list is empty, so the answer contains only `kill`.
- **Killing the root:** Every process is a descendant, so all $n$ IDs are returned.
- **Sibling processes:** Killing one subtree never reaches a sibling because traversal only follows child edges.
- **Sentinel parent 0:** The real root is stored in `g[0]`, but 0 is not traversed unless explicitly used as a start; `kill` is guaranteed to be a real `pid`.
- **Guaranteed target:** Because `kill` occurs in `pid`, the search always starts from a valid process.
- **Any-order output:** Preorder is acceptable; sorting would add unnecessary $O(k\log k)$ time.
- **Deep-chain recursion:** With $n$ up to $5\cdot10^4$, the exact recursive Python code can exceed Python’s default recursion limit on a highly skewed tree. An iterative stack or queue is the robust production choice even though the recurrence itself is correct.
- **Why no visited set:** A valid rooted tree has no cycles and each node has one parent, so duplicate visits cannot occur. For arbitrary graph input, a visited set would be necessary.
- **`defaultdict` side effect:** Reading `g[i]` for a leaf creates an empty entry. This does not affect correctness or the $O(n)$ bound.
