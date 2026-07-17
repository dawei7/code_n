# Find Center of Star Graph

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/find-center-of-star-graph/) |
| Frontend ID | 1791 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An undirected star graph has $n$ nodes labeled from $1$ through $n$. It contains one center node and exactly $n-1$ edges, each connecting that center to one of the other nodes. Every non-center node is therefore a leaf incident to only its edge with the center.

You are given the graph as `edges`, where each pair `edges[i] = [u_i, v_i]` represents an undirected edge between its two endpoints. The input is guaranteed to describe a valid star graph. Return the label of its center node.

### Function Contract

**Inputs**

- `edges`: a list of exactly $n-1$ two-element integer lists, where $3 \le n \le 10^5$.
- Every endpoint is a node label from $1$ through $n$, the endpoints of an edge differ, and all edges together form a valid undirected star graph.

**Return value**

- Return the integer label of the unique center node.

### Examples

**Example 1**

- Input: `edges = [[1, 2], [2, 3], [4, 2]]`
- Output: `2`

Node `2` is incident to every edge.

**Example 2**

- Input: `edges = [[1, 2], [5, 1], [1, 3], [1, 4]]`
- Output: `1`

Every other node has its sole connection to node `1`.

**Example 3**

- Input: `edges = [[1, 3], [2, 3]]`
- Output: `3`

The minimum valid star has two edges, and their shared endpoint is the center.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Use two edges as a complete certificate**

A valid star with at least three nodes has at least two distinct edges. Its center belongs to every edge, while each leaf belongs to exactly one. Consequently, the first two edges must share the center and cannot share a leaf. Their unique common endpoint is already the answer; inspecting later edges cannot reveal a different candidate under the validity guarantee.

**Handle all endpoint orientations**

Write the first two edges as `[a, b]` and `[c, d]`. If `a` equals either `c` or `d`, then `a` is their shared endpoint and must be the center. Otherwise, `a` is a leaf. The first edge must still contain the common endpoint, so `b` is necessarily equal to either `c` or `d` and is the center.

This comparison covers the center appearing first in both edges, second in both, or in opposite positions. Because edges are undirected, their stored orientation has no semantic effect.

**Stop once uniqueness is established**

The graph guarantee rules out malformed inputs, repeated leaf-to-leaf connections, and multiple possible centers. After the shared endpoint of two edges is identified, every remaining valid edge must contain it. Returning immediately is therefore both sufficient and correct, regardless of the number or ordering of later edges.

#### Complexity detail

The method reads two edges and performs a constant number of endpoint comparisons, so its running time is $O(1)$ even though `edges` may contain $n-1$ pairs. It stores only four endpoint values and uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Count every node degree:** Scanning all $n-1$ edges and returning the node of degree $n-1$ is correct, but it takes $O(n)$ time and $O(n)$ storage.
- **Intersect endpoint sets:** Building sets for the first two edges and taking their intersection also uses only two edges, but direct comparisons avoid set allocation.
- **Scan for a repeated endpoint:** A frequency map or repeated linear search eventually finds the center, yet both do unnecessary work after the first two edges have proved it.
- **Minimum graph:** Since $n \ge 3$, `edges` always contains at least two entries, so both decisive edges are available.
- **Endpoint orientation:** The center may occur at either index independently in each edge; all four orientation combinations must work.
- **Edge order:** No ordering promise is needed because any two distinct edges in a valid star share exactly the center.
- **Input validity:** The constant-time conclusion relies on the guarantee that `edges` represents a valid star graph; validating an arbitrary graph would require examining all edges.

</details>
