## General

**Model the maze as an unweighted graph**

Each empty cell is a graph vertex. Two empty cells share an edge when they are adjacent vertically or horizontally, because one legal move connects them. Every edge costs exactly one step. The task is therefore to find the shortest graph distance from the entrance to any border cell other than the entrance.

Breadth-first search is the natural shortest-path method for an unweighted graph. It visits all cells at distance $0$, then all cells at distance $1$, then distance $2$, and so on. Consequently, the first newly reached exit has the smallest possible distance.

The exact solution initializes `q = deque([(i, j)])` with the entrance and immediately changes `maze[i][j]` to `"+"`. Reusing the wall marker means “not available for another visit.” This serves two purposes: the entrance can never be enqueued again through a cycle, and an entrance already on the border is never mistaken for an exit.

**Process one distance layer at a time**

The variable `ans` starts at zero. At the start of each while-loop iteration, the queue contains exactly the cells at one common distance from the entrance. The code increments `ans`, records the current queue length, and removes exactly that many cells. Their unvisited neighbors are one step farther away, so those neighbors all have distance `ans`.

This ordering explains why the code returns `ans` when it discovers a border neighbor rather than storing a distance beside every queue entry. On the first loop iteration, it expands the distance-zero entrance after changing `ans` to one, so its neighbors are correctly labeled distance one. New cells appended during the loop are not processed in the same layer because `range(len(q))` evaluates the old queue size once. They wait for the next while iteration.

For each popped cell, the four direction pairs `[0, -1]`, `[0, 1]`, `[-1, 0]`, and `[1, 0]` produce left, right, up, and down neighbors. A neighbor is usable only if its row and column remain within the grid and `maze[x][y] == "."`. Walls and already visited cells both contain `"+"` and are skipped.

If a usable neighbor lies on row $0$, row $m-1$, column $0$, or column $n-1$, it is an exit. The method returns the current layer distance immediately. Otherwise it enqueues the neighbor and marks it as `"+"`.

**Why marking happens when a cell is enqueued**

A cell can be adjacent to several cells in the current BFS layer. If it remained `"."` until it was later removed from the queue, several parents could enqueue it, wasting work and breaking the simple one-visit bound. Marking immediately reserves the cell for the first path that reaches it. Because BFS reaches cells in nondecreasing distance, the first such path is already a shortest path, so ignoring later routes cannot lose a better answer.

The method modifies the supplied `maze` rather than allocating a separate visited matrix. After it returns, every cell discovered by BFS, including the entrance, has become `"+"`. That side effect is part of the exact implementation and should be understood by callers.

**Why the first exit is nearest**

Maintain the invariant that every cell removed during a layer is at distance `ans - 1`, while every newly discovered neighbor is at distance `ans`. The invariant is true initially because the entrance is at distance zero. FIFO order and the fixed layer size preserve it from one iteration to the next.

When the code finds an exit neighbor, it has constructed a legal path of length `ans` to that exit. Any path shorter than `ans` would end at a cell from an earlier BFS layer. All usable neighbors of all earlier layers were already examined, so such an exit would already have caused a return. The found exit is therefore nearest.

If the queue becomes empty, every empty cell reachable from the entrance has been examined and none of its newly reached border cells qualified as an exit. Any unvisited empty cell is separated by walls and cannot be reached. Returning `-1` is then correct.

## Complexity detail

Let $R$ be the number of rows and $C$ the number of columns.

Each reachable empty cell is marked when first enqueued, so it enters and leaves the deque at most once. Processing a cell checks exactly four directions, each in constant time. In the worst case all $RC$ cells are reachable, giving $O(RC)$ time.

The deque can hold many frontier cells. A safe worst-case bound is $O(RC)$, matching the manifest. Because visited state is stored inside `maze`, no separate $R$-by-$C$ boolean matrix is allocated. Aside from the queue, the algorithm uses constant scalar state. The mutation does not count as a new allocation, although it does destroy the original empty-cell markings.

Deque operations at both ends used here, `append` and `popleft`, take $O(1)$ amortized time. Using a Python list with removal from the front would introduce shifting costs and could make the traversal unnecessarily slow.

## Alternatives and edge cases

- **Depth-first search:** DFS can determine reachability, but the first exit it encounters need not be the closest. Finding a shortest path would require exploring more routes and maintaining best distances.
- **Dijkstra's algorithm:** Dijkstra also finds shortest paths, but every move has unit cost, so its priority queue is unnecessary overhead. BFS is the specialized optimal method.
- **Separate visited set or matrix:** This avoids changing `maze` and still gives $O(RC)$ time and space. The exact solution chooses in-place marking to save that additional structure.
- **Entrance on the border:** It is explicitly not an exit. Marking it before the search and testing only newly discovered neighbors enforces this rule naturally.
- **Exit one move away:** The first layer increments `ans` to one and returns one as soon as it sees the adjacent border cell.
- **One-row or one-column maze:** Every cell is on a border, but the entrance is excluded. Any different reachable empty neighbor is an exit at its BFS distance; if none exists, the method returns `-1`.
- **Maze containing only the entrance:** The queue expands once, finds no valid neighbor, empties, and returns `-1`.
- **Several equally near exits:** BFS may return upon finding any one of them. Only the distance is requested, so direction order does not affect correctness.
- **Unreachable border cells:** A border opening behind walls is never enqueued and correctly does not influence the result.
- **Cycles in open corridors:** Immediate marking ensures each cell is visited once, preventing endless movement around a cycle.
- **Input mutation:** The exact method replaces visited `"."` cells with `"+"`. If the caller needs the original maze later, it must pass a copy or use a separate visited structure.
- **No exit:** Exhausting the deque proves that no reachable non-entrance border opening exists, so `-1` is the required sentinel.
