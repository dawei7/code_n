# A* Search Algorithm

| | |
|---|---|
| **ID** | `graph_18` |
| **Category** | graphs |
| **Complexity (required)** | $O(E)$ Time, $O(V)$ Space (Highly variable) |
| **Difficulty** | 7/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) |

## Problem statement

Given a weighted graph, a starting vertex `S`, and a specific target vertex `T`.
Find the absolute shortest path from `S` to `T`.
*Optimization:* You are provided with a heuristic function h(n) that estimates the remaining distance from any node n to the target `T`.

**Input:** An adjacency list `adj`, a start node `S`, a target node `T`, and a heuristic function `h(node)`.
**Output:** The shortest distance to `T`, and the path taken.

## When to use it

- **Targeted Pathfinding:** When you don't need the shortest path to *every* node (like Dijkstra computes), but only care about finding a specific target as fast as possible.
- Extremely common in grid-based maze/video game AI problems where you know the physical (X, Y) coordinates of nodes.

## Approach

**1. The Flaw of Dijkstra:**
Dijkstra's algorithm is a "blind" search. It expands perfectly radially outward in all directions from the source, equally exploring paths going completely backward just in case they loop around.
If you are driving from New York to Los Angeles, Dijkstra will explore routes leading into the Atlantic Ocean with the exact same priority as roads heading West!

**2. The A* Equation:**
A* guides Dijkstra by giving it a sense of direction.
In Dijkstra, the Priority Queue sorts nodes strictly by g(n): the exact accumulated distance from the start to node n.
In A*, the Priority Queue sorts nodes by f(n) = g(n) + h(n).
- g(n): The exact cost from Start to n.
- h(n): The *Heuristic* (an educated guess of the cost from n to Target).
- f(n): The estimated total cost of the complete journey from Start \rightarrow n \rightarrow Target.

**3. Admissibility:**
For A* to mathematically guarantee finding the absolute shortest path, the heuristic function h(n) MUST be "admissible".
An admissible heuristic NEVER OVERESTIMATES the true cost to reach the target.
- *Example:* On a 2D grid, the Euclidean straight-line distance is admissible because you can't possibly travel faster than a straight line. The Manhattan distance is also admissible if diagonal movement is illegal.
If h(n) overestimates the distance, A* will act scared of valid paths and might confidently return a sub-optimal path!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_18: A* Search on a 2D grid.

Manhattan-distance heuristic. Walk the grid with 4-neighbour
moves; a priority queue keyed on f = g + h (cost so far plus
Manhattan distance to goal) drives the expansion order.
Return the shortest path length in steps, or -1 if no path.
"""


def solve(grid, start, goal, size):
    from heapq import heappush, heappop
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return -1
    if start == goal:
        return 0

    def heuristic(p):
        return abs(p[0] - goal[0]) + abs(p[1] - goal[1])

    open_heap = []
    heappush(open_heap, (heuristic(start), 0, start))
    g_score = {start: 0}
    while open_heap:
        f, g, current = heappop(open_heap)
        if current == goal:
            return g
        if g > g_score.get(current, float("inf")):
            continue
        row, col = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0:
                nbr = (nr, nc)
                tentative = g + 1
                if tentative < g_score.get(nbr, float("inf")):
                    g_score[nbr] = tentative
                    heappush(open_heap, (tentative + heuristic(nbr), tentative, nbr))
    return -1
```

</details>

## Walk-through

Grid graph. Start `S(0,0)`, Target `T(2,0)`. Edges cost 1.
h(n) is Manhattan distance.
`g_score = {S: 0}`.
`pq = [(f=2, g=0, S)]`. (Because h(S, T) = |0-2| + |0-0| = 2).

1. `heappop()` -> `curr = S`.
   - Evaluate neighbor `A(1,0)` (moving Right).
     - `tentative_g = 0 + 1 = 1`.
     - `h(A, T) = |1-2| + |0-0| = 1`.
     - `f_score = 1 + 1 = 2`.
     - Push `(2, 1, A)`.
   - Evaluate neighbor `B(0,1)` (moving Up).
     - `tentative_g = 0 + 1 = 1`.
     - `h(B, T) = |0-2| + |1-0| = 3`.
     - `f_score = 1 + 3 = 4`.
     - Push `(4, 1, B)`.
2. `pq` state: `[(2, 1, A), (4, 1, B)]`.
   - `A` is sorted to the front! Notice how A* completely ignores moving Up (which is the wrong direction) because its f-score is worse!
3. `heappop()` -> `curr = A(1,0)`.
   - Evaluate neighbor `T(2,0)` (moving Right).
     - `tentative_g = 1 + 1 = 2`.
     - `h(T, T) = 0`.
     - `f_score = 2 + 0 = 2`. Push `(2, 2, T)`.
4. `heappop()` -> `curr = T(2,0)`.
   - `curr == T`. TARGET REACHED! Terminate!
   - (Node `B` was completely ignored, saving precious computation cycles).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(E)$ | $O(V)$ |
| **Average** | Highly dependent on heuristic | $O(V)$ |
| **Worst** | $O(E log V)$ | $O(V)$ |

The complexity of A* is notoriously difficult to pin down because it depends entirely on the quality of the heuristic h(n).
In the worst case (where h(n) is always exactly 0), A* mathematically degrades into standard Dijkstra's algorithm, expanding radially in all directions, yielding $O(E log V)$ time.
In the best case (where h(n) perfectly models the exact distance to the target), A* marches directly to the target in a straight line without checking a single incorrect branch! The time complexity becomes roughly proportional to the length of the path $O(\text{Path Length})$ ~= $O(E_{optimal})$.
Space complexity is $O(V)$ for the Priority Queue and `g_score` dictionary.

## Variants & optimizations

- **IDA* (Iterative Deepening A*):** A* stores the massive "frontier" in its Priority Queue, which can consume hundreds of megabytes of RAM in complex game states (like Rubik's Cube solving). IDA* throws away the Priority Queue and uses an iterative deepening DFS bounded by the f-score. It vastly reduces space complexity to $O(\text{Path Length})$ at the cost of slightly more time.

## Real-world applications

- **Video Game AI:** 99% of pathfinding in strategy games (Starcraft, Civilization) or RPGs is done using A* combined with a grid map. The heuristic effortlessly guides units around large obstacles without scanning the entire map.

## Related algorithms in cOde(n)

- **[graph_04 - Dijkstra's Algorithm](graph_04_dijkstra.md)** — The exact same algorithm, just with h(n) = 0.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
