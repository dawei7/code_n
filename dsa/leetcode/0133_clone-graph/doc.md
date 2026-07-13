# Clone Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 133 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/clone-graph/) |

## Problem Description
### Goal
Given a reference to a node in a connected undirected graph, create a deep copy of the entire reachable graph. Every node has a unique value and must correspond to exactly one newly allocated clone with that same value, even when cycles or several paths lead back to it.

Preserve every neighbor relationship and its listed order in the copied structure, including self-links when present, but do not reuse any original node object. Mutating the clone must therefore have no effect on the source graph. The app contract represents the graph as a one-based adjacency list and returns independent adjacency data; the native artifact performs the equivalent operation on linked `Node` objects.

### Function Contract
**Inputs**

- `adj_list`: the app encoding of the graph, where row `i` lists the 1-based neighbors of node $i + 1$; `[]` encodes a null root

**Return value**

A structurally independent deep copy of the adjacency data. The native LeetCode artifact clones `Node` objects directly.

### Examples
**Example 1**

- Input: `adj_list = [[2,4],[1,3],[2,4],[1,3]]`
- Output: `[[2,4],[1,3],[2,4],[1,3]]`

**Example 2**

- Input: `adj_list = [[]]`
- Output: `[[]]`

**Example 3**

- Input: `adj_list = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(V + E)$
- **Space:** $O(V + E)$

<details>
<summary>Approach</summary>

#### General

**Node identity—not value—is the key to a true graph clone**

In the native graph form, create a clone on first discovery and store `original -> clone` in a hash map keyed by node identity. Values are not a safe key in a general graph because different nodes may share a value. The map also acts as the visited structure, stopping cycles from recursing forever.

Insert the mapping before traversing neighbors. Then an edge back to the current node can immediately reuse its already-created clone instead of creating a duplicate.

**Reproduce adjacency entries using mapped clone endpoints**

Depth-first or breadth-first traversal visits each original node. For every neighbor entry, obtain or create that neighbor's clone, recursively or iteratively ensure its adjacency is processed, and append the clone to the current clone's neighbor list. Processing entries rather than unique unordered pairs preserves neighbor-list ordering and any permitted parallel references.

**The app adapter deep-copies the serialized adjacency form**

The app represents the already-labeled graph as nested neighbor rows rather than runtime `Node` objects. Copying the outer list alone would still alias its rows; cloning every row preserves the same serialized topology while making mutations independent. The native artifact performs the identity-map algorithm on actual nodes.

**Every discovered original has exactly one reusable clone**

Every mapped original has exactly one distinct clone, and all processed neighbor entries point to the mapped clones of the corresponding original neighbors.

**Original-to-clone identity preserves sharing and cycles**

The map allocates exactly one clone for each reached original, so multiple edges to the same node reuse one clone rather than duplicating it, and cycles terminate at already mapped nodes. Traversal reaches the entire connected component.

For every original adjacency entry, processing appends the mapped clone of that neighbor, reproducing edge order and multiplicity. All mapped objects are newly allocated and contain only clone references, so the resulting component is structurally identical and deeply independent.

#### Complexity detail

Each of `V` nodes and `E` adjacency entries is visited once, giving $O(V+E)$ time. The map, traversal state, and cloned adjacency use $O(V+E)$ space including output.

#### Alternatives and edge cases

- **Clone recursively without a map:** loops forever on cycles and duplicates shared nodes.
- **Return the original graph:** matches values but violates deep-copy identity.
- **Copy only node values:** loses neighbor topology.
- A null input returns null. A single isolated node still requires a distinct clone with an empty neighbor list.
- Self-loops and cycles are handled because the original is mapped before its outgoing edges are explored.

</details>
