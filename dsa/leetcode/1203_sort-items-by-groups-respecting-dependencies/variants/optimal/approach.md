## General

Two independent ordering levels must be satisfied:

- dependencies between items inside the same group determine their internal order;
- dependencies crossing group boundaries determine the order of whole group blocks.

Sorting only items can interleave groups. Sorting only groups cannot resolve dependencies among items in one group. The exact solution builds one directed graph for internal item edges and another for cross-group edges, topologically sorts the groups, and then topologically sorts the items of each group.

**Give every ungrouped item its own group**

An item with group `-1` has no contiguity relationship with any other ungrouped item. The code assigns each such item a new unique group ID beginning at `m`. This allows the same group-level logic to handle it as a singleton block.

`group_items` has `n + m` slots, enough for the original groups plus at most `n` unique new ones. Original groups with no items and unused extra slots remain empty. The loop mutates the input `group` list while assigning IDs and records every item in its group’s list.

**Separate internal and cross-group dependencies**

For each item `i` and every prerequisite `j` in `beforeItems[i]`, the directed requirement is `j -> i`.

If `group[j] == group[i]`, both items will live in the same final block. The code adds `i` to `item_graph[j]` and increments `item_degree[i]`. This edge will be enforced by that group’s internal topological sort.

If their groups differ, every item in `j`’s group block must appear before every item in `i`’s group block for `j` to precede `i` while groups stay contiguous. The code adds a directed edge from `group[j]` to `group[i]` and increments the destination group’s indegree.

The same pair of groups may receive several edges from different item dependencies. The code retains those duplicate graph edges and increments indegree for each. During traversal, each stored edge produces one matching decrement, so correctness is preserved even without deduplicating group edges.

**Topological sorting with indegrees**

The helper receives a degree array, adjacency graph, and iterable of nodes to sort. It enqueues every supplied node whose indegree is zero. Removing such a node is safe because no unprocessed prerequisite remains. For each outgoing edge, it decrements the destination degree and enqueues that destination when the degree reaches zero.

If every supplied node is removed, `res` is a valid topological order. If fewer are removed, the remaining nodes participate in or depend on a directed cycle, so no valid ordering exists and the helper returns an empty list.

First, the solution topologically sorts all `n + m` possible group IDs. Empty groups simply behave as zero-indegree nodes with no output items. If the group graph has a cycle, contiguity makes the requirements impossible: each group in the cycle would need its whole block before the next.

**Sort items separately inside each ordered group**

The solution visits groups in `group_order`. For group `gi`, it calls the same helper only on `group_items[gi]`, using the internal item graph and degrees. Because item edges were added only when endpoints share a group, processing one group cannot decrement degrees belonging to another group.

If the internal result length differs from the number of group items, that group contains an item-dependency cycle and the method returns an empty list.

Otherwise, `ans.extend(item_order)` appends the entire internal order before moving to the next group. This construction guarantees contiguity by design.

**Why every dependency is respected**

For an internal dependency `j -> i`, the two items are in the same block and their group’s topological order places `j` before `i`.

For a cross-group dependency, the group graph contains `group[j] -> group[i]`. Group topological order places the entire prerequisite group block before the dependent group block, so `j` necessarily appears before `i` regardless of their internal positions.

Every dependency belongs to exactly one of these cases. Every item appears in exactly one group list and is appended exactly once. Therefore, a successful result contains all items, keeps each group contiguous, and honors every prerequisite.

Conversely, an internal directed cycle can never be linearized, and a cross-group cycle cannot be resolved while each group remains one block. The two cycle checks correctly reject impossible instances.

## Complexity detail

Let $G=n+m$ be the number of allocated group slots and let $E$ be the total number of dependency entries across `beforeItems`.

Assigning groups and populating item lists takes $O(n)$. Building graphs examines every dependency once and takes $O(E)$. Group topological sorting visits $G$ vertices and every cross-group edge. Across all per-group item sorts, every item and every internal edge is visited once. Total time complexity is $O(n+G+E)$.

The group and item adjacency lists store one entry per dependency, including duplicates between the same group pair. Degree arrays, queues, group-item lists, orders, and output store $O(n+G)$ values. Total space complexity is $O(n+G+E)$.

The helper destructively decrements degree arrays. This is safe because the group degrees are sorted once, and each item belongs to exactly one per-group sort.

## Alternatives and edge cases

- **Topologically sort all items then bucket by group:** This can also work when combined with a separate group order, but the exact solution avoids storing cross-group edges in the item graph because group ordering already enforces them.
- **Deduplicate group edges:** A set of group-pair edges can reduce repeated adjacency entries and indegree counts, potentially improving constants when many item edges connect the same groups.
- **Treat all ungrouped items as one group:** This is incorrect because it would force unrelated items to be contiguous. Each receives its own group.
- **Empty original groups:** They appear in group topological order but contribute no items, so they do not affect the final sequence.
- **Internal item cycle:** The per-group topological sort processes too few items and the method returns an empty list.
- **Cross-group cycle:** The group topological sort fails even if every group’s internal dependencies are acyclic.
- **No dependencies:** All indegrees are zero. Any group order and any internal item order are valid, and the method still emits contiguous groups.
- **Duplicate group-level edges:** They are safe because every increment has a corresponding stored edge and later decrement.
- **Input mutation:** Ungrouped assignments overwrite `-1` entries in `group`. Copy the list first if caller-visible preservation is required.
- **Any valid order accepted:** Queue order among simultaneously available nodes only chooses one of potentially many correct topological results.
- **Unused allocated group slots:** The `n + m` capacity simplifies indexing. Empty unused slots add only linear overhead and append nothing.
