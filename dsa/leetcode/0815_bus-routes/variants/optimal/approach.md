## General

**The number of buses, not the number of stops, is the distance**

Traveling to any stop on one bus route costs exactly one boarded bus. Moving between two stops on the same route does not add another bus, because each route repeats forever. A transfer at a shared stop adds one when the next route is boarded.

This suggests breadth-first search, but the search level must represent buses taken rather than physical stop-to-stop movements. The exact solution stores queue entries as `(stop, bus_count)`. From a stop reached with `bus_count` buses, boarding one previously unused route generates all stops on that route with `bus_count + 1`.

Because each transition has the same cost of one newly boarded bus, breadth-first order guarantees that the first time the target stop is reached uses the fewest buses.

**Handle the zero-bus journey first**

If `source == target`, the traveler is already at the destination and needs zero buses. The function returns 0 before building any graph.

This special case matters even if the shared stop does not appear in any route. Being at the destination requires no bus-service availability.

**Build the stop-to-routes index**

The original input is organized from route to stops: `routes[i]` lists all stops served by bus route `i`. During search, however, we stand at a stop and need to know which routes can be boarded there.

The dictionary `g` reverses the relationship:

$$
\texttt{g[stop]}=\text{all route indices containing that stop}.
$$

The nested loops visit every route-stop occurrence once and append its route index to the stop's list. For routes `[1,2,7]` and `[3,6,7]`, for example, `g[7]` becomes `[0,1]`, revealing that stop 7 permits a transfer between the two buses.

If either `source` or `target` is absent from `g`, no bus can depart from the source or no bus can arrive at the target. Since the equal-stop case was already handled, the function safely returns `-1`.

**The growing list acts as a FIFO queue**

The queue begins as `q = [(source, 0)]`. Rather than repeatedly removing index zero, which would be expensive for a Python list, the code iterates with

`for stop, bus_count in q`.

Python's list iterator continues over items appended while the iteration is in progress. Every newly reached stop is appended at the end, so entries are processed in first-in, first-out order. All entries with a smaller bus count were appended before entries with a larger count. This gives the same breadth-first ordering as a conventional deque with `popleft()`, while avoiding front deletions.

When the current `stop` equals `target`, the function returns its stored `bus_count`. The queue order is the reason this count is minimal.

**Why both buses and stops need visited sets**

The solution tracks two different kinds of completed work.

`vis_bus` records routes that have already been boarded and expanded. The first time a route is available, the algorithm scans all of its stops. Boarding the same repeating route again from another stop would reveal exactly the same stops and cannot produce a shorter path, so it should never be expanded twice.

`vis_stop` records stops already added to the BFS queue. It begins with `source`. When expanding a bus route, each `next_stop` is appended only if it has not previously been discovered.

Both sets are important:

- without `vis_bus`, every shared stop could cause a large route to be scanned repeatedly;
- without `vis_stop`, the same stop could be enqueued through many buses, creating duplicate work and cycles.

The route is marked visited before its stops are scanned. The stop is marked visited before it is appended. Marking at discovery time prevents another path in the same BFS layer from adding the same object again.

**How one BFS expansion corresponds to boarding a bus**

At `stop` with count `b`, the loop examines every route in `g[stop]`. For each unvisited `bus`:

1. mark that route in `vis_bus`;
2. inspect every stop served by `routes[bus]`;
3. append each newly discovered stop with count `b + 1`.

Every appended stop is reachable by boarding that one bus at the current stop, remaining aboard as long as needed, and exiting at the appended stop. The bus loops forever, so the ordering of stops inside a route does not restrict which listed stop can be reached.

For `routes = [[1,2,7],[3,6,7]]`, source 1 first discovers route 0 and reaches stops 2 and 7 with one bus. Processing stop 7 reveals route 1 and reaches stops 3 and 6 with two buses. When stop 6 is later processed, the function returns 2.

**Why first discovery is optimal**

Suppose a stop is first appended with count `b`. It came from a stop that was processed with count `b-1`, and BFS processes all smaller counts first. If there were a way to reach it using fewer than `b` buses, the preceding stop and route on that journey would have been expanded in an earlier layer, causing this stop to be discovered earlier. Therefore, the first stored count for a stop is minimal.

Similarly, the first time a route is boarded is through the minimum-bus route to one of its stops. Re-expanding it later cannot improve any destination on that same bus. These facts justify both visited sets and prove that the first target count returned is the answer.

If the growing queue is exhausted, every stop reachable through any chain of bus routes from `source` has been processed. If `target` was not encountered, no valid trip exists, so the function returns `-1`.

## Complexity detail

Let

$$
S=\sum_i \lvert\texttt{routes}[i]\rvert,
$$

the total number of route-stop occurrences in the input.

Building `g` visits and stores each occurrence once, taking `O(S)` time and `O(S)` space.

During BFS, every route is expanded at most once because of `vis_bus`. Across all route expansions, scanning `routes[bus]` therefore visits at most `S` occurrences. Every stop is dequeued at most once because of `vis_stop`. When that stop is processed, scanning `g[stop]` visits its route incidences; summed over all discovered stops, there are at most `S` such incidences. Thus, total BFS time is `O(S)`, and complete time remains `O(S)`.

The reverse index stores `O(S)` route indices. The queue and `vis_stop` contain at most the number of distinct stops, no more than `S`. `vis_bus` contains at most the number of routes, also no more than `S`. The total auxiliary space complexity is `O(S)`.

Using a list as an append-only queue is important to this bound. Deleting from the front of a list would shift later elements and could introduce quadratic overhead; iterating by a growing index does not.

## Alternatives and edge cases

- **Route-node BFS:** Treat each route as a graph node and connect routes sharing a stop. A direct all-pairs route graph can be expensive to construct. The stop-to-routes index discovers exactly the needed transfers without materializing every route pair.

- **Stop-node graph with all pairwise edges:** Connecting every pair of stops on the same route may require quadratic edges for one long route. Expanding a route only once represents the same reachability in linear total input size.

- **Dijkstra's algorithm:** Every bus boarding costs one, so the graph is unweighted at the relevant level. BFS is sufficient and simpler.

- **Conventional deque:** A `deque` with `popleft()` is an equally valid FIFO implementation. The exact source uses an append-only list whose iterator observes appended entries.

- **`source == target`:** The answer is 0 even when the stop appears in no route.

- **Source absent from all routes:** No bus can be boarded, so the result is `-1`.

- **Target absent from all routes:** No route can arrive there, so the result is `-1`.

- **Source and target on the same route:** Expanding that route appends the target with count 1, so one bus is returned.

- **Shared transfer stop:** Every route listed in `g[stop]` can be boarded there. Already expanded routes are skipped; new routes add one to the count.

- **Repeated stop across routes:** The reverse index intentionally stores every containing route. `vis_stop` prevents multiple queue entries for that physical stop, while `vis_bus` still permits each distinct route to be expanded once.

- **Cycle of routes:** The two visited sets prevent endless movement around the cycle.

- **Route order:** Because a bus repeats forever, any listed stop on a boarded route is reachable regardless of its position in the route array.

- **Unreachable target despite appearing in `g`:** Existence in some route is not enough; that route may be in a disconnected component. Exhausting BFS correctly returns `-1`.

- **No input mutation:** The route lists are read when building and expanding the index; their contents and ordering are not changed.
