## General

**Turn the question into a yes-or-no test**

The required answer is the greatest number of minutes that the person may remain at the starting cell before beginning to move. Trying every possible waiting time separately would be wasteful, but there is an important ordering property: if waiting `t` minutes is safe, then every shorter wait is also safe. Starting earlier cannot remove a route that was available after a longer delay. Conversely, if waiting `t` minutes is already too late, waiting even longer cannot make the fire retreat.

That monotonic behavior lets the solution use binary search. Its helper `check(t)` answers one precise question: after waiting exactly `t` minutes, can the person reach the safehouse while respecting the movement and fire timing rules? The outer search then finds the greatest `t` for which the answer is true.

**Represent one minute of fire growth**

The nested `spread(q)` helper receives a queue containing the current boundary of the fire. For every burning cell in that queue, it examines the four orthogonal neighbors. A neighbor becomes newly burning only when it is inside the grid, has not already burned, and has value zero in `grid`. Value zero denotes grass, while walls and the original fire markers are not traversable grass.

Every newly reached cell is marked immediately in the Boolean `fire` matrix and placed in a fresh queue `nq`. Immediate marking is important: two burning cells may both border the same grass cell, but that cell should be enqueued only once. Returning `nq` advances the simulation by exactly one minute because it contains precisely the cells ignited during this layer.

The direction tuple `(-1, 0, 1, 0, -1)` is a compact encoding of up, right, down, and left. Applying `pairwise` to it produces the four coordinate changes `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)` without maintaining two separate direction arrays.

**Rebuild the fire state for each proposed wait**

Each call to `check(t)` begins by setting every entry of `fire` to false. It then scans the grid, adds every initially burning cell to `q1`, and marks those positions as burning. A binary-search check must start from the original grid state; retaining fire from an earlier check would test a different scenario and make the result depend on the order in which midpoints happened to be tried.

The loop `while t and q1` calls `spread` once for each minute of waiting. If `q1` becomes empty early, the fire has reached a stable state and can never spread again, so stopping the loop is equivalent to simulating all remaining waiting minutes. After the waiting phase, `fire[0][0]` is tested. If the starting cell has already caught fire, the person cannot begin a route, and this waiting time immediately fails.

**Search the person's positions one minute at a time**

Once the wait is over, `q2` starts with the upper-left cell. The Boolean `vis` matrix records cells already reached by the person. The outer `while q2` loop represents successive minutes, and `for _ in range(len(q2))` processes exactly the positions reachable at the beginning of the current minute.

When a queued position is popped, the code first tests `fire[i][j]`. A cell may have been safe when it entered the queue but then caught fire at the end of the preceding minute. Such a state must not be allowed to move again, so it is skipped. From a still-safe position, the person considers every orthogonal neighbor. A neighbor is usable only if it is in bounds, has not been visited, is not currently burning, and is grass rather than a wall or an initial-fire cell.

Marking a position visited as soon as it is enqueued prevents duplicate work. It is safe to keep only the earliest visit to a cell: an earlier arrival gives the person at least as much time before future fire growth as any later arrival to that same location. A later copy cannot open an option that the earlier copy lacked.

**Preserve the special safehouse timing rule**

The order within a minute is the subtle center of this problem. The person moves first, and then the fire spreads. For an ordinary cell, arriving at the same minute that fire reaches it is fatal; that position will be burning when processed in the next layer and is therefore skipped. The safehouse is exceptional: reaching it counts as success even if fire spreads there immediately afterward.

The code implements that distinction exactly. When a valid neighbor is the bottom-right safehouse, `check` returns true immediately, before calling `spread(q1)` for that minute. For every other neighbor, it is enqueued normally. Only after all current person positions have moved does the code advance the fire by one layer. This is not an arbitrary implementation order; it directly models “person moves, then fire spreads,” including the destination's permitted simultaneous arrival.

**Why one feasibility check is correct**

The person queue contains all cells that can be occupied at the current minute without having already violated the fire rules. Initially that statement holds for the starting cell after the separate burned-start test. During a layer, every accepted neighbor is adjacent grass that is safe at the person's movement time, so every enqueued state corresponds to a legal move.

In the other direction, the loop examines all four neighbors of every viable current state. Therefore, it cannot overlook a legal next move. If fire reaches an ordinary newly occupied cell during the following spread, the pop-time fire test removes precisely that now-fatal state. If the newly occupied cell is the safehouse, the immediate return applies its special rule instead. By induction over the minute layers, the queue represents all and only viable positions. Consequently, returning true means a legal escape exists, while exhausting the queue means none exists for that waiting time.

**Find the last feasible waiting time**

The binary search uses `l = -1` and `r = m * n`. The artificial value minus one acts as a known lower sentinel; it allows the final result to remain minus one when even `check(0)` fails. The midpoint is rounded upward:

$$
\texttt{mid} = \left\lfloor \frac{\texttt{l} + \texttt{r} + 1}{2} \right\rfloor.
$$

If `check(mid)` succeeds, `mid` itself is feasible, so the lower boundary moves to it. If it fails, `mid` and all larger waits are impossible, so the upper boundary becomes `mid - 1`. The upward midpoint guarantees progress when the two boundaries are adjacent. When they meet, `l` is the greatest feasible tested waiting time.

**Why testing only through** `m * n` **detects an unlimited wait**

Fire growth is monotone: a cell changes from unburned to burning at most once. There are only `m * n` cells, and each successful spread layer burns at least one previously unburned cell. Thus, by `m * n` minutes the fire must have stopped changing. Walls may make it stabilize much earlier, but never later.

If waiting `m * n` minutes is still feasible, waiting any larger number produces the same stabilized fire layout. The person therefore can wait indefinitely under the problem's convention, and the required return value is `10^9`. If that endpoint is not feasible, the binary search has already found the greatest finite safe wait below it.

## Complexity detail

Let `M` be the number of rows, `N` the number of columns, and `C = M N` the number of grid cells.

One call to `check(t)` first clears a Boolean matrix and scans the grid for initial fire cells, both of which take `O(C)` time. During the fire simulation, a cell is marked burning at most once, enqueued at most once, and checks four neighbors. During the person's breadth-first search, a cell is marked visited at most once, enqueued at most once, and also checks four neighbors. Even though fire growth is interleaved with person layers, the total work of one check is therefore `O(C)`, not the number of minutes multiplied by the whole grid.

The outer binary search covers integer waits from zero through `C`. It makes `O(\log C)` feasibility checks, so the exact implementation runs in

$$
O(C \log C) = O(MN \log(MN))
$$

time.

This bound follows the code as written. Although an alternative design can precompute fire-arrival times once, this implementation deliberately resets and simulates the fire inside every `check` call, so its work must include that logarithmic repetition.

The `fire` and `vis` matrices each contain `C` Boolean entries. In the worst case, each deque can also contain `O(C)` positions across a broad breadth-first layer. The auxiliary-space complexity is `O(C)`, or `O(MN)`. Recursion is not used, so there is no call-stack growth with path length.

## Alternatives and edge cases

- **Precompute fire-arrival times:** A multi-source breadth-first search can assign the earliest fire time to every grass cell, followed by a person feasibility search for each binary-search wait. This avoids resimulating fire and can reduce repeated work, but the exact submitted solution instead performs the coupled simulation described above.
- **Derive the answer from two arrival-time grids:** One may compute earliest person and fire arrivals and reason carefully about slack along a path. This can reach linear time with a more involved destination-versus-intermediate-cell inequality; it is easier to make an off-by-one error around simultaneous arrival at the safehouse.
- **Depth-first search for the person:** DFS does not naturally preserve earliest arrival times. A later-discovered route to a cell may be unusable even when an earlier one works, so breadth-first layers are the natural representation of elapsed minutes.
- **Binary search with a downward midpoint:** Updating the feasible lower bound to `mid` can stall when the bounds are adjacent. The upward midpoint used here guarantees termination.
- **No route at time zero:** Every nonnegative wait fails, the sentinel `l` remains minus one, and the method returns `-1`.
- **Fire can never threaten the usable route:** The stabilized layout still permits escape after waiting `m * n` minutes, so the method returns `10^9` rather than the finite test bound.
- **Starting cell burns during the wait:** The explicit `fire[0][0]` test rejects the attempt before the person's BFS begins.
- **A queued ordinary cell burns after entry:** The pop-time fire test prevents the person from moving out of a cell that caught fire in the same minute as arrival.
- **Fire reaches the safehouse with the person:** Immediate success on entering the bottom-right cell implements the one location where equal arrival times are allowed.
- **Fire reaches an ordinary cell with the person:** The state may be enqueued before the fire spreads, but it is burning when popped and cannot continue, so equality is correctly rejected there.
- **Walls:** Grid value two is never accepted by either spread or person movement. Walls permanently block both processes.
- **Several initial fires:** Adding all of them to `q1` before any spread makes `spread` a multi-source BFS layer, so their growth happens simultaneously rather than one fire receiving an artificial head start.
- **Duplicate attempts to ignite a cell:** Immediate marking in `fire` ensures the cell enters the next frontier only once.
- **Fire becomes unable to spread while waiting:** An empty `q1` means the state is permanent. Skipping the remaining loop iterations does not change feasibility.
- **Person revisits:** The `vis` matrix rejects revisits because the first BFS arrival is never worse than a later arrival under monotonically spreading fire.
- **Narrow corridors:** The layer ordering remains exact even when the person and fire approach from opposite ends; no heuristic distance assumption is used.
- **Large requested answer:** The method never simulates one billion minutes. It recognizes stabilization using the `m * n` endpoint and converts that result to the required sentinel.
