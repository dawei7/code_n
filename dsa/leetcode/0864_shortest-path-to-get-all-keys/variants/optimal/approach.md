## General
**Position alone does not describe progress**

Reaching the same cell with different collected keys can enable different future moves through locks. A search state must therefore be `(row, column, key_mask)`. Bit $i$ of `key_mask` records whether key `chr(ord("a") + i)` has been collected. Scanning the grid locates `@` and constructs the mask whose bits represent all keys.

When moving to a lowercase cell, set its bit in the mask. When considering an uppercase cell, reject the move unless the corresponding bit is already set. Walls and out-of-bounds coordinates are always rejected.

**Breadth-first search gives the shortest route**

Place the starting position with mask zero into a queue and mark that full state visited. Breadth-first search expands states by move count, so the first state that owns the complete key mask uses the fewest moves among all legal routes.

Marking only coordinates would be wrong because a later visit with more keys may pass a lock that an earlier visit could not. Conversely, revisiting the same coordinate with the same mask cannot help: it has identical future options and, under breadth-first order, cannot arrive in fewer moves. Deduplicating complete states preserves every potentially optimal route while making the search finite.

There are at most $mn$ positions and $2^c$ masks. Every legal route corresponds to a path through this state graph, and every state-graph edge corresponds to one legal grid move. Breadth-first distance is therefore exactly the requested move count.

## Complexity detail
At most $mn2^c$ distinct states are enqueued. Each examines four directions in constant time, so total time is $O(mn2^c)$. The queue and visited set can both hold $O(mn2^c)$ states, giving the same auxiliary-space bound.

## Alternatives and edge cases
- **Visit each coordinate once:** This loses valid routes that revisit a cell after obtaining a key and can incorrectly report impossibility.
- **Depth-first search over paths:** It can eventually find a route, but repeated paths and cycles make shortest-path discovery expensive without breadth-first ordering.
- **Store visited states in a list:** It remains correct, but linear membership tests can make state deduplication quadratic in the number of reachable states.
- **Compress to key-to-key distances:** This can reduce the grid, but locks make pairwise reachability depend on the current mask and require careful state-aware preprocessing.
- **Key before its lock:** The lock becomes passable on all subsequent visits, including after returning to an earlier cell.
- **Lock before its key:** The move is blocked, but another route may reach the key first.
- **Key adjacent to the start:** The answer may be `1`, even if its matching lock is never opened.
- **Unreachable key:** When the queue empties before the complete mask appears, return `-1`.
