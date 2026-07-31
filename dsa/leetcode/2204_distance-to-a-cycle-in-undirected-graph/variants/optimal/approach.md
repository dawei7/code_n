## General

**Peel away every attached tree**

No degree-one node can belong to a cycle. Put all current leaves in a queue, remove them conceptually, and decrement the degrees of their still-active neighbors. Whenever a neighbor becomes a leaf, enqueue it as well. This is the undirected analogue of topological trimming.

Every node outside the unique cycle belongs to a tree attached to that cycle, so repeated leaf removal eventually deletes it. A cycle node retains its two cycle neighbors and never falls below degree two during trimming. The nodes with positive remaining degree are therefore exactly the cycle.

**Measure from the entire cycle at once**

Set every surviving cycle node's distance to zero and place all of them in one BFS queue. Expand through the original graph. The first time BFS reaches a removed tree node, assign one more than its predecessor's distance.

Multi-source BFS is equivalent to adding a virtual source connected to every cycle node by a zero-cost edge. Because every original edge has unit distance, first discovery gives the shortest route to any cycle node. Cycle nodes start at zero, and every other node receives precisely its required minimum distance.

## Complexity detail

Building adjacency lists costs $O(n)$ because a unicyclic graph has exactly $n$ edges. Leaf trimming processes every node and edge a constant number of times, and the multi-source BFS does the same. Total time is $O(n)$.

The adjacency lists, degree and distance arrays, and queues use $O(n)$ space.

## Alternatives and edge cases

- **BFS from every node:** Once cycle nodes are known, launching an independent search for each answer is correct but can require $O(n^2)$ time.
- **DFS cycle reconstruction:** Parent tracking can locate the unique cycle, but careful handling of the first back edge and cycle boundaries is more intricate.
- **Pure cycle:** When every node lies on the cycle, trimming removes nothing and every answer is zero.
- **Long attached path:** Multi-source BFS assigns increasing distances along the path without restarting a search.
- **Several attached trees:** All cycle nodes enter the queue together, so each branch is measured from its nearest attachment point.
