## General

**Follow one deterministic path at a time.** Because each node has at most one
outgoing edge, a walk can only terminate, enter a previously processed
component, or revisit a node from its own current traversal. Start from every
globally unvisited node and record each newly visited node's step number in a
map local to that traversal.

**Distinguish a new cycle from an old component.** Mark nodes globally as soon
as the current walk reaches them. When the walk stops, a cycle has been found
only if the stopping node also occurs in the current traversal's local map.
A node visited by an earlier traversal may belong to a cycle, but that cycle
was already measured and the current path merely feeds into it.

If the current walk has taken $d$ steps and revisits a node first seen at step
$s$, the repeated suffix contains exactly $d-s$ nodes. Maximize this length
over all starts. Every node is assigned to one traversal, and every cycle is
encountered from at least one of its nodes, so the maximum is complete.

## Complexity detail

Every node becomes globally visited once, making all walks together $O(n)$
time. The global marks and traversal-distance storage use $O(n)$ space.

## Alternatives and edge cases

- **Indegree pruning:** Remove zero-indegree nodes with Kahn's algorithm; only
  cycles remain, and each remaining component can then be counted in $O(n)$.
- **Restart from every node:** Detecting a cycle independently from every
  starting node is correct but takes $O(n^2)$ time on one large cycle.
- **Previously processed cycle:** A walk entering an old component must not
  count the tail leading into that cycle.
- **Terminating edge:** Reaching `-1` proves the current path contains no new
  cycle.
- **Multiple components:** Track the maximum across all components rather than
  stopping after the first cycle.
- **No cycle:** Preserve the initial answer `-1` when every walk terminates or
  enters an already processed acyclic path.
