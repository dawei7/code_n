# Valid Arrangement of Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2097 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Graph Theory, Eulerian Circuit |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/valid-arrangement-of-pairs/) |

## Problem Description

### Goal

You are given distinct directed pairs. In a pair `[start, end]`, the first value is its starting vertex and the second value is its ending vertex.

Reorder all pairs so that the ending vertex of every pair equals the starting vertex of the following pair. Every input pair must appear exactly once in the returned arrangement. At least one valid arrangement is guaranteed to exist, and any valid one may be returned.

### Function Contract

Let $P$ be the number of directed pairs.

**Inputs**

- `pairs`: a list of $P$ distinct two-element integer lists `[start, end]`, where $1 \le P \le 10^5$, $0 \le \texttt{start}, \texttt{end} \le 10^9$, and the two endpoints of each pair differ.

**Return value**

Return any ordering of all input pairs in which each pair's end equals the next pair's start.

### Examples

**Example 1**

- Input: `pairs = [[5,1],[4,5],[11,9],[9,4]]`
- Output: `[[11,9],[9,4],[4,5],[5,1]]`

**Example 2**

- Input: `pairs = [[1,3],[3,2],[2,1]]`
- Output: `[[1,3],[3,2],[2,1]]`
- Explanation: This arrangement closes a directed cycle. Rotating that cycle would also be valid.

**Example 3**

- Input: `pairs = [[1,2],[1,3],[2,1]]`
- Output: `[[1,2],[2,1],[1,3]]`

### Required Complexity

- **Time:** $O(P)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Recognizing an Eulerian trail**

Interpret each pair `[start, end]` as one directed edge. Using every pair exactly once while matching consecutive endpoints is precisely the requirement for a directed Eulerian trail. The existence guarantee means the graph has the necessary connectivity and degree structure.

For every vertex, track its outdegree minus its indegree. If a non-cyclic trail exists, its first vertex is the unique one whose difference is $1$. If every difference is $0$, the edges form an Eulerian circuit and the first endpoint of any pair is a valid starting choice.

**Consuming edges without getting trapped**

Use an adjacency list and an explicit stack. From the vertex on top of the stack, consume any still-unused outgoing edge and push its ending vertex. When the top vertex has no remaining outgoing edge, pop it into a reverse vertex sequence.

This delayed placement is the crucial part of Hierholzer's algorithm. Reaching a temporary dead end does not discard other edges: the completed suffix is recorded, then the stack resumes from the earlier vertex where unused edges remain. Each directed edge is removed from exactly one adjacency list, so no pair can be used twice.

**Recovering the pair arrangement**

Reverse the recorded vertex sequence. Each two consecutive vertices now identifies one traversed directed edge. Emit those consecutive vertex pairs in order.

Every input edge was consumed once, so the output contains exactly $P$ pairs with the same directed-edge multiset as the input. Consecutive output pairs share the intermediate vertex by construction. Therefore the result uses every pair exactly once and satisfies the required chaining rule.

#### Complexity detail

Building degrees and adjacency lists takes $O(P)$ time. The traversal pushes and pops once per edge, and constructing the answer is also linear, so total time is $O(P)$. The adjacency lists, degree map, traversal stack, reverse sequence, and output use $O(P)$ space.

#### Alternatives and edge cases

- **Recursive Hierholzer traversal:** Postorder DFS expresses the same algorithm compactly, but a trail of up to $10^5$ edges can exceed the language recursion limit.
- **Repeated forward scanning:** Searching the full pair list for the next matching start can build a correct trail in favorable cases, but requires $O(P^2)$ time in the worst case.
- **Backtracking over arrangements:** Trying pair permutations is unnecessary and grows exponentially; the Eulerian structure determines a linear-time construction.
- A single pair is already a valid arrangement.
- In a directed cycle, several rotations and traversal choices may all be valid answers.
- Vertex values may repeat across many pair endpoints even though the directed pairs themselves are distinct.
- The first input pair need not begin the valid non-cyclic trail; the degree difference identifies the required start.

</details>
