## Examples

**Example 1**

- Input: `n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2`
- Output: `false`
- Explanation: A path can stop at node `1` as well as at node `2`. Because node `1` is a reachable terminal other than `destination`, not every path has the required endpoint.

The source illustration shows the two terminal branches:

```mermaid
flowchart TD
    accTitle: Source reaches two different terminal nodes
    accDescr: Directed edges run from source node 0 to terminal node 1 and from source node 0 to destination node 2.

    n0["0<br/>source"] --> n1["1"]
    n0 --> n2["2<br/>destination"]
```

**Example 2**

- Input: `n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3`
- Output: `false`
- Explanation: One choice reaches node `3`, but another enters the directed cycle between nodes `1` and `2` and can continue indefinitely.

The source illustration contrasts the destination branch with the reachable cycle:

```mermaid
flowchart TD
    accTitle: One branch reaches the destination while another cycles
    accDescr: Source node 0 points to destination node 3 and to node 1. Nodes 1 and 2 point to each other, forming a reachable directed cycle.

    n0["0<br/>source"] --> n1["1"]
    n0 --> n3["3<br/>destination"]
    n1 --> n2["2"]
    n2 --> n1
```

**Example 3**

- Input: `n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3`
- Output: `true`

Both acyclic branches in the source illustration converge at the same destination:

```mermaid
flowchart LR
    accTitle: Two acyclic branches converge at the destination
    accDescr: Source node 0 points to nodes 1 and 2, and each of those nodes points to destination node 3.

    n0["0<br/>source"] --> n1["1"]
    n0 --> n2["2"]
    n1 --> n3["3<br/>destination"]
    n2 --> n3
```
