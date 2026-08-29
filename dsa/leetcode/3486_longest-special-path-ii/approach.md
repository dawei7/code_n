## General

**Every downward path is a suffix of one root-to-node path.** Root the undirected tree at node zero. During depth-first search, the current recursion stack lists exactly the nodes from the root to the current node. Any ancestor-to-current downward path is obtained by choosing a left depth within this stack.

Because all edge lengths are positive, for a fixed ending node the longest valid suffix uses the earliest left depth that satisfies the value-frequency rule. The algorithm's main job is to maintain that minimum legal depth in constant time.

**Track occurrence depths for every value on the active path.** `positions[value]` is a stack of depths where that value appears on the current root-to-node path. Before exploring a node's children, its depth is appended; after all children, it is popped. This backtracking makes sibling subtrees see only their own ancestor paths.

The special-path rule has two parts:

- no value may appear three or more times; and
- at most one distinct value may appear twice.

The source maintains separate boundary information for these two restrictions.

**Exclude every third occurrence.** Before appending the current node, if its value already has at least two path occurrences, `value_positions[-2]` will become the third-most-recent occurrence once the current copy is included. A valid suffix containing that depth, the later previous occurrence, and the current node would contain the value three times.

Therefore, its left boundary must be strictly after `value_positions[-2]`. `largest_third` stores the greatest such forbidden depth seen for any value. Taking the maximum is sufficient because starting after the latest forbidden occurrence also starts after every earlier one.

For occurrences at depths $2,5,8$, when processing depth eight the forbidden third-from-last depth is two, so a legal suffix must start at depth three or later. It may then include the copies at five and eight, but not all three.

**Allow duplication for at most one value.** For each value that appears at least twice in the candidate suffix, consider the latest previous occurrence before its newest occurrence. If the suffix begins at or before that depth, that value is duplicated.

The algorithm tracks the two largest such depths belonging to distinct values:

- `largest_second = (depth, value)` is the largest duplicate threshold;
- `next_second = (depth, value)` is the second largest.

The suffix may keep the duplicated value associated with `largest_second`, but it must start after `next_second[0]` so every other value appears at most once. Starting after the second-largest threshold leaves at most the one largest threshold inside the suffix.

When the current value has a previous occurrence, `new_second = value_positions[-1]` becomes that value's newest duplicate threshold. The update carefully handles whether the same value is already first, already second, or absent from both. If updating the second entry makes it larger than the first, the tuples swap. This preserves the two greatest thresholds for distinct values.

Sentinel tuples `(-1,-1)` and `(-1,-2)` use impossible negative values, since actual node values are nonnegative.

**Combine the two restrictions into one earliest legal depth.** After updating trackers and appending the current occurrence, the source computes

`left_depth = max(largest_third, next_second[0]) + 1`.

Starting here excludes every forbidden third occurrence and excludes the duplicate threshold of every value except possibly the one represented by `largest_second`. Hence the suffix is special. Starting any earlier would include either three copies of some value or duplicated copies of at least two distinct values, so this is the earliest legal boundary.

Notice that `largest_second` itself is not part of the maximum. The definition explicitly permits one value to occur twice; forcing the start after the largest threshold would incorrectly require all values to be distinct.

**Compute weighted length and node count from depths.** `prefix_distance[d]` stores the root-to-node distance at active path depth $d$. For current cumulative `distance`, the edge length from the ancestor at `left_depth` to the current node is

$$
distance-\texttt{prefix\_distance}[left\_depth].
$$

The node count is `depth - left_depth + 1`. If the suffix contains only the current node, both cumulative distances are equal, giving length zero and one node.

For every current endpoint, the earliest legal start maximizes length because moving the start downward removes positive-length edges. The code compares this best suffix with the global `best_length`. A strictly longer one replaces both result fields; an equal-length one updates `best_nodes` only when it uses fewer nodes.

This tie rule matters because different edge weights can give equal total lengths over different numbers of edges.

**Why the tracker state can be passed without undoing it.** Tuples and integers are immutable values in Python. Each recursive child receives its own references to the updated scalar tracker values, and modifications inside that child rebind only its local parameters. `positions` is the mutable shared structure and is explicitly backtracked with `pop`. `prefix_distance` positions below the current depth remain correct for the active path; deeper entries may be overwritten by siblings only after they are no longer queried as ancestors.

**Why every optimal path is considered.** Take any downward special path ending at node $v$. It is a suffix of the DFS path when $v$ is visited. The computed `left_depth` is the earliest valid suffix boundary, so its length is at least that of the chosen special path. Conversely, the two boundary conditions prove the computed suffix itself is special. Thus the best suffix evaluated at each endpoint dominates every special path ending there, and maximizing across all endpoints yields the global longest length. Tracking the minimum node count among equal lengths completes both requested outputs.

The source raises Python's recursion limit to $100{,}000$, exceeding the maximum tree depth of $50{,}000$ for a chain-shaped input.

## Complexity detail

The adjacency list stores both directions of each of the $n-1$ edges and is built in $O(n)$ time. DFS visits every node and edge once. Occurrence-stack operations, tracker comparisons, and result updates take constant time per node. Total time is $O(n)$.

The graph, occurrence stacks, prefix-distance array, and recursion stack use $O(n)$ space. Across all `positions` lists, only the current root-to-node path is stored at once, so their total active entries are at most $n$. These bounds match the manifest.

Dictionary operations on `positions` have expected constant time. The global recursion-limit change is an operational accommodation for worst-case depth and does not alter asymptotic space.

## Alternatives and edge cases

- **Start a path from every ancestor:** Examining every ancestor-descendant pair costs $O(n^2)$ on a chain.
- **Sliding window with only last occurrences:** It can enforce all-distinct values, but this problem permits one duplicate and needs both second- and third-occurrence information.
- **Forbid the largest duplicate threshold too:** That solves the stricter all-distinct version and may discard valid longer paths.
- **Ignore third occurrences:** Allowing one duplicated value does not allow it three times; `largest_third` is essential.
- **Track the top two thresholds without their values:** Updating a repeated value could occupy both slots incorrectly; value identities keep the slots distinct.
- **All values distinct:** Both restrictions remain at sentinel depths, so the entire root-to-current path is valid.
- **Exactly one duplicated value:** `largest_second` may remain inside the suffix while `next_second` stays at $-1$.
- **Two duplicated values:** Starting after the second-largest duplicate threshold removes at least one occurrence of all but one.
- **Three copies of one value:** Starting after the third-from-last occurrence leaves at most its last two copies.
- **Single-node path:** It has weighted length zero and node count one, providing the initial valid result.
- **Equal maximum weighted lengths:** The code keeps the path with fewer nodes as required.
- **Sibling subtrees:** Popping the current value depth prevents one sibling's occurrences from contaminating another.
- **Chain-shaped tree:** Recursion depth reaches $O(n)$, and the explicit limit of $100{,}000$ covers the declared maximum.
