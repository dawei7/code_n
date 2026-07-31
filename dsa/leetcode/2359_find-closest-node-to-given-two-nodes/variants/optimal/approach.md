## General

**Exploit the functional-graph structure.** From any start there is only one
possible forward walk: repeatedly follow `edges[current]` until reaching `-1`
or revisiting a node. Record the first distance at which every node is reached.
A first visit is the shortest directed distance because no alternative
outgoing choice exists; stopping on a revisit is safe because the remaining
walk would only repeat the same cycle.

**Compare the two distance maps.** Build one length-$n$ distance array for each
start, using `-1` for unreachable nodes. A node is a candidate exactly when
both recorded distances are non-negative. Its objective value is the maximum
of those two distances.

Scan candidate indices from 0 through $n-1$ and replace the answer only when
the objective value is strictly smaller than the best seen. The scan examines
every common reachable node, so it finds the minimum objective; refusing to
replace on equality preserves the smallest index required by the contract.
If no candidate is encountered, the initialized answer `-1` is correct.

## Complexity detail

Each forward walk visits at most $n$ nodes, and the final index scan visits
$n$ nodes, so the total time is $O(n)$. The two distance arrays use $O(n)$
auxiliary space.

## Alternatives and edge cases

- **Per-candidate path search:** Recomputing both distances separately for
  every node is correct but can take $O(n^2)$ time on a long chain.
- **Hash maps for visited distances:** Dictionaries avoid initializing full
  arrays and can help when both paths are short, but arrays give simple
  deterministic $O(1)$ lookups.
- **Cycles:** Stop a walk when its next node already has a recorded distance;
  otherwise traversal would never terminate.
- **No outgoing edge:** Reaching `-1` ends that start's reachable path.
- **Identical starts:** The shared starting node has objective zero and must be
  returned immediately by the comparison logic.
- **Equal objective values:** Scanning indices in ascending order and updating
  only on a strict improvement enforces the smallest-index tie-break.
