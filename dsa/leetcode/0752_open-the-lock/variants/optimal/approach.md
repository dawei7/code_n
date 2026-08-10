## General

**Model lock combinations as an unweighted graph**

Each four-digit display is a graph vertex. Turning one wheel one slot produces an edge to another display. Every move costs exactly one turn, so the minimum number of turns is an unweighted shortest-path distance from `"0000"` to `target`.

Breadth-first search is the correct tool because it explores vertices by increasing edge distance.

**Generate exactly eight neighbors**

For each of four wheel positions, the helper creates two states:

- One after rotating the digit down by one.
- One after rotating it up by one.

The wrap rules are explicit: zero rotated downward becomes nine, and nine rotated upward becomes zero.

The helper temporarily changes one character in a list, joins it into a string for each neighbor, then restores the original character before moving to the next wheel. Therefore every returned state differs from the input at exactly one wheel.

**Treat deadends and visited states together**

The set `s` begins with all deadend combinations. A state in this set must never be enqueued.

After the starting-state checks, `"0000"` is added to the same set, and every newly enqueued state is added immediately. The set thus means “blocked or already discovered.” These two categories need the same BFS action: never enter them again.

Marking at enqueue time prevents the same combination from being added through multiple parents in one layer.

**Handle the start before BFS**

If the target is `"0000"`, zero turns are required. The problem guarantees the target is not a deadend.

If the start itself is a deadend, the wheels cannot turn at all, so every non-start target is impossible and the method returns `-1`.

**Count BFS layers as moves**

The queue begins with the start at distance zero, while `ans` begins at zero. At the beginning of each layer, `ans` is incremented. Every neighbor generated from nodes in that layer is exactly `ans` moves from the start.

If a generated neighbor equals the target, returning `ans` therefore returns its shortest distance.

After processing the fixed current queue length, all newly enqueued states form the next layer.

**Why the current queue length must be captured**

New neighbors are appended to the same deque that is being consumed. Iterating only `range(len(q))` as measured at the start of the layer prevents those newly appended states from being processed immediately. Without this boundary, a single loop pass could mix several distances and `ans` would no longer describe the states being expanded.

Every original layer node is removed exactly once during that fixed number of iterations. What remains afterward is precisely the next frontier.

**A wraparound example**

From `"0000"`, rotating the final wheel downward produces `"0009"` in one move, not nine moves. The neighbor helper’s explicit zero-to-nine rule adds this state to the first BFS layer, so a target of `"0009"` is returned with distance one.

**Why finding the target before the visited check is safe**

The code tests `t == target` before checking membership in `s`. The target is guaranteed not to be a deadend. If it had already been visited, BFS would have returned when it was first generated, so execution could not reach a later duplicate first. The ordering is therefore safe under the contract.

**Why BFS is correct**

Every legal single-wheel move appears among the generated neighbors, and no generated neighbor changes more than one wheel. Excluding deadends removes exactly the forbidden vertices.

BFS dequeues states in nondecreasing move count. The first generated occurrence of the target lies on a shortest legal path, so the returned layer number is minimal. If the queue empties, every reachable nondeadend state has been explored and the target is unreachable, justifying `-1`.

## Complexity detail

For `w` wheels there are at most `10^w` displays, plus `d` deadends. Each visited display considers `2w` moves.

Under the standard fixed-width state model, time is `O(d + 10^w w)` and space is `O(d + 10^w)` for the set and queue.

In literal Python character-copy terms, constructing each of `2w` neighbor strings costs `O(w)`, so neighbor generation is `O(w^2)` per state. Here `w = 4` is fixed, making both descriptions constant work per display.

## Alternatives and edge cases

- **Bidirectional BFS:** Search simultaneously from start and target and expand the smaller frontier. It can greatly reduce explored states while preserving shortest paths.

- **Depth-first search:** DFS can find a route but does not naturally guarantee the minimum number of moves.

- **Dijkstra’s algorithm:** It works, but all edges have equal weight, so a priority queue is unnecessary overhead.

- **Start is a deadend:** No move can be made, so return `-1`.

- **Target is the start:** Return zero without entering the search.

- **Wheel wraparound:** Both `0 -> 9` and `9 -> 0` are one legal move.

- **Duplicate discovery paths:** Adding a state to the set when enqueued prevents repeated queue entries.

- **Unreachable target:** Exhausting the finite state graph proves impossibility.
