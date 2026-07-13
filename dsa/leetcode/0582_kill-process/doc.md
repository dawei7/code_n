# Kill Process

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 582 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/kill-process/) |

## Problem Description
### Goal
You are given a list of unique process identifiers `pid` and a parallel list `ppid`, where `ppid[i]` is the parent of `pid[i]` and parent identifier `0` denotes a root process. Killing one process also kills every process descended from it through any number of parent-child links.

Given the identifier `kill`, return that process together with all of its direct and indirect descendants. Do not include ancestors, siblings, or processes from another root, and return each affected process identifier once; the result may be in any order.

### Function Contract
**Inputs**

- `pid: list[int]`: unique process identifiers
- `ppid: list[int]`: corresponding parent identifiers, where `ppid[i]` is the parent of `pid[i]` and zero denotes no parent
- `kill: int`: identifier of the process to terminate

**Return value**

- A list containing `kill` and every direct or indirect descendant of `kill`
- The identifiers may be returned in any order

### Examples
**Example 1**

- Input: `pid = [1, 3, 10, 5]`, `ppid = [3, 0, 5, 3]`, `kill = 5`
- Output: `[5, 10]` in any order

**Example 2**

- Input: the same process tree with `kill = 3`
- Output: `[3, 1, 5, 10]` in any order

**Example 3**

- Input: `pid = [1]`, `ppid = [0]`, `kill = 1`
- Output: `[1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reverse the parent relation**

The input directly maps each process to its parent, but termination must travel from a parent to its children. Scan the paired arrays once and build an adjacency map from every parent identifier to the list of its direct child identifiers.

**Traverse only the killed subtree**

Start an explicit stack with `kill`. Repeatedly remove one process, add it to the result, and push all children from the adjacency map. This depth-first traversal reaches descendants at every depth without recursion limits.

**Why the result is exact**

The killed process is inserted initially. Whenever a reached process is handled, every direct child is scheduled, so induction on tree depth shows that all descendants are eventually included. Conversely, the traversal follows only parent-to-child edges beginning at `kill`, so every added process is either `kill` itself or one of its descendants. Unique process identifiers and the process-tree structure prevent duplicate visits.

#### Complexity detail

For `n` processes, building adjacency examines `n` parent-child pairs. Traversal visits at most `n` processes and edges, so total time is $O(n)$. The adjacency map, stack, and output use $O(n)$ space.

#### Alternatives and edge cases

- **Breadth-first traversal:** a queue over the same adjacency map has identical asymptotic bounds and returns a different valid order.
- **Recursive depth-first search:** is concise but a deep process chain can exceed the language recursion limit.
- **Scan all parent entries for every killed process:** avoids adjacency storage but can take $O(n^2)$ time.
- **Kill a leaf:** returns only that process.
- **Kill a root:** returns the entire process tree rooted there.
- **Multiple children:** every child subtree must be traversed.
- **Deep chain:** use an explicit stack or queue rather than recursion.
- **Parent identifier zero:** marks a root and is not itself a real process.
- **Output order:** is unrestricted; correctness depends on membership, not traversal order.

</details>
