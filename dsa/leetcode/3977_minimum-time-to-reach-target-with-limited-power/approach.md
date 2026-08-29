## General

Reaching the same node with different remaining power amounts creates different future possibilities. A route arriving with five power may be able to leave a node whose cost is four, while a route arriving with only three cannot. One shortest-time value per node is therefore insufficient.

The source expands the state to:

$$
(\texttt{node},\texttt{remainingPower}).
$$

For every node `u` and power `p` from zero through the initial `P`, `dist[u][p]` stores the smallest travel time discovered for reaching exactly that state.

This turns the constrained problem into an ordinary nonnegative shortest-path problem on at most `n(P+1)` states.

**Departure consumes power, arrival does not**

From state `(u,p)`, no outgoing edge is legal if

$$
p<\texttt{cost}[u].
$$

If departure is legal, every outgoing edge uses the same remaining amount:

$$
p'=p-\texttt{cost}[u].
$$

The destination and edge travel time do not affect power. The source subtracts `cost[u]` once before iterating over all outgoing edges, accurately modeling one alternative departure rather than several simultaneous departures.

When the signal arrives at target, it stops. It does not pay `cost[target]` because that cost is charged only if it later leaves target.

**Building only original adjacency**

For directed edge `[u,v,t]`, the source appends `(v,t)` to `g[u]`. It does not add the reverse direction.

It also does not materialize every power-state edge. When state `(u,p)` is processed, it scans `u`'s original outgoing edges and creates transitions to `(v,p-cost[u])` on demand.

**Initialization**

The signal begins at `source` with all initial power and time zero:

```python
dist[source][power] = 0
pq = [(0, -power, source)]
```

No source-node power cost is paid at initialization. It is paid only if an edge is actually taken.

If `source == target`, the initial state is already a complete route. It should return `[0,power]`, and the source does so on the first heap pop without subtracting `cost[source]`.

**Why the heap stores negative power**

Python's min-heap orders tuples lexicographically. The source stores:

```python
(time, -remaining_power, node)
```

Smaller time is popped first. Among entries with equal time, a larger actual power has a more negative second tuple component and is popped first.

This exactly matches the output priority:

1. minimize total time;
2. among minimum-time target routes, maximize remaining power.

The node field only breaks ties after both required quantities are equal.

**Relaxing a legal transition**

After a non-target state with enough departure power is popped, the source subtracts the node cost. For each outgoing edge to `v` with travel time `t`, it computes:

$$
nd=d+t.
$$

The successor power is the already reduced `p`. If `nd` improves `dist[v][p]`, the table is updated and `(nd,-p,v)` is pushed.

All travel times are positive, so Dijkstra's greedy ordering applies: once a state is popped with its smallest recorded distance, no later route can improve its time.

**Stale entries**

The implementation pushes a new tuple whenever a state improves rather than removing the older tuple. Consequently the heap can contain stale entries.

The check

```python
if d > dist[u][p]:
    continue
```

discards a tuple whose state has since received a smaller time. A popped tuple cannot have `d<dist[u][p]`, so `>` is sufficient even though many implementations write `!=`.

The source tests `u == target` before this stale check. That ordering is still safe. If a target tuple were stale, a smaller-time tuple for the exact same target-power state must already have been pushed, and the min-heap would pop that smaller time first and return before reaching the stale one.

**Why the first target tuple has the right tie-break**

When a target state is popped, its time is minimum among every queued state because time is the tuple's first field.

Could another target route with the same time but greater power remain undiscovered? No. Every edge time is at least one, so such a target route's predecessor has strictly smaller time. Dijkstra processes all states with time below the target time before any state at the target time, meaning all equal-minimum-time target candidates have already been inserted.

Among those candidates, negative power makes the greatest remaining power pop first. Therefore:

```python
if u == target:
    return [d, p]
```

returns both required components at once.

Testing target before `p < cost[u]` is also correct: insufficient power prevents leaving target, not arriving there.

**Why exact remaining power is preserved**

A route with more power and no greater time may dominate another state at the same node, but the source does not implement dominance pruning. It retains one time for every exact power amount.

This larger state representation is simple and safe. Different power states cannot be merged merely by keeping the fastest arrival, because a slightly slower high-power arrival might enable a much faster continuation that a low-power state cannot take.

Cycles do not create infinitely many states: power never increases and each departure consumes a positive cost. Dijkstra's distance table also prevents non-improving repetitions for an exact state.

If the priority queue empties without popping target, every reachable legal state has been exhausted and `[-1,-1]` is returned.

**The stored source has four unresolved names**

The exact file contains no imports even though it uses:

- `List` in annotations;
- `inf` to initialize the distance table;
- `heappop` to remove queue entries;
- `heappush` to add improved states.

Normal module loading first raises `NameError` for `List`. If that name is injected, a call fails at `inf`. Supplying both reaches the loop and fails at `heappop`. Supplying that as well reaches a successful relaxation and then fails at `heappush`.

The conventional dependencies would come from `typing`, `math`, and `heapq`. Once only these names are supplied, the represented state-space Dijkstra logic matches independent full target-state evaluation. The missing dependencies remain genuine defects of the stored source.

## Complexity detail

Let `P` be the initial power. There are at most `n(P+1)=O(nP)` exact node-power states.

For every power value, an original directed edge can be examined from its source state, giving at most `O(mP)` generated transitions. Initializing the table costs `O(nP)`. Under the standard expanded-graph binary-heap analysis, time is

$$
O\bigl(P(n+m)\log(nP)\bigr),
$$

which is the manifest's stated time bound.

The exact lazy heap can contain multiple entries for one state. A fully literal heap-size logarithm gives

$$
O\bigl(P(n+m)\log(nP+mP)\bigr).
$$

Under the usual simple-graph or polynomial-edge assumptions, this logarithm is asymptotically equivalent to `O(\log(nP))`.

The adjacency lists use `O(n+m)` space and the distance table uses `O(nP)`. If a decrease-key heap or one-entry-per-state queue were available, queue storage could be bounded by `O(nP)`, yielding the manifest's `O(nP+m)` space description.

Python's exact push-new-entry implementation may retain stale tuples. Up to `O(mP)` successful relaxations can create heap entries in a conservative worst case, so a source-literal space bound is

$$
O(nP+m+mP)=O(P(n+m)).
$$

The source does not modify the input edges or cost array. These runtime bounds describe the algorithm after all four missing names are supplied.

## Alternatives and edge cases

- **One best time per node:** Remaining power affects future departures and the secondary objective, so node-only distances lose necessary information.

- **Breadth-first search:** Edge times vary and can be as large as `10^9`. BFS minimizes edge count rather than total travel time.

- **Optimize power before time:** The contract is lexicographic in the opposite order. Heap time must be the primary key.

- **Store positive power as the second heap field:** A min-heap would then prefer lower power on equal times. Negating it implements the required maximum-power tie-break.

- **Charge destination cost on arrival:** Costs are paid when forwarding from a node. A route that stops at target keeps its arrival power.

- **Charge source cost immediately:** If source equals target, no departure occurs and no cost should be paid. Initialization correctly preserves full power.

- **Power exactly equal to node cost:** Departure is legal, leaving zero power. The source rejects only `p < cost[u]`.

- **Zero remaining power at target:** This is a valid answer because no further departure is required.

- **Zero remaining power at a non-target:** All costs are positive, so that state cannot leave and is skipped.

- **Source equals target:** The initial heap entry returns `[0,power]`.

- **Unreachable target:** Emptying the heap returns `[-1,-1]`.

- **Directed edges:** Reverse travel is unavailable unless a separate reverse edge appears in the input.

- **Cycles:** Positive time and non-increasing power prevent a cycle from improving indefinitely. Exact-state distances discard worse repeats.

- **Equal-time target routes:** All predecessors have smaller times because edge times are positive, so every tied target candidate is queued before the first target pop. Negative power selects the best one.

- **Stale target entry:** A better tuple for the same state must pop first, making the early target check safe despite preceding the stale check.

- **Dominance pruning:** It could reduce states by discarding arrivals worse in both time and power, but careful frontier maintenance is more complex. The source uses the full bounded state table.

- **Missing dependencies:** `List`, `inf`, `heappop`, and `heappush` are all required for normal execution; supplying only some exposes the next failure.

- **Manifest space qualification:** `O(nP+m)` describes table, graph, and a bounded-state heap. The exact lazy heap may hold `O(mP)` stale or competing entries, so the conservative source-level bound is larger.
