## General

**Model removals as edge costs**

View every cell as a graph vertex connected to its orthogonal neighbors.
Entering an empty cell costs zero. Entering an obstacle costs one because that
obstacle must be removed. The cost of a route is therefore exactly the number
of obstacle cells on it, so the requested answer is a shortest-path distance
from the first corner to the opposite corner.

**Exploit binary weights with a deque**

All edge weights are either zero or one. Maintain the best known removal count
for each cell and a deque of cells whose outgoing edges still need relaxation.
When a relaxation enters a zero cell, put that neighbor at the front because
its distance did not increase. When it enters an obstacle, put it at the back
because its distance increased by one.

This front/back rule processes distance layers in nondecreasing cost order,
which is the binary-weight specialization of Dijkstra's algorithm. A cell is
updated only when a strictly cheaper route is found. Once no relaxation
remains, every stored distance is minimal; in particular, the destination's
distance is the fewest obstacles any corner-to-corner route can use.

## Complexity detail

There are $mn$ cells and fewer than $4mn$ directed neighbor transitions.
Under 0-1 BFS, each successful binary-weight relaxation contributes constant
deque work, giving $O(mn)$ time. The distance matrix and deque contain
$O(mn)$ entries.

## Alternatives and edge cases

- **Heap-based Dijkstra:** A priority queue handles the weights correctly in $O(mn \log(mn))$ time, but binary weights allow the logarithmic factor to be removed.
- **Linear-selection Dijkstra:** Repeatedly scanning all unvisited cells for the next minimum is correct but can require $O((mn)^2)$ time.
- **Ordinary BFS by moves:** Minimizing the number of moves is not equivalent to minimizing removed obstacles because a longer zero-only path may be cheaper.
- **All-zero route:** If any empty-cell path joins the corners, the answer is zero even when shorter routes cross obstacles.
- **Single row or column:** The only route is straight, so every obstacle between the empty endpoints must be removed.
- **Revisiting a cell:** A newly found lower-cost route must replace its previous distance; merely marking a cell on first discovery is unsafe for weighted paths.
- **Endpoint cost:** Both endpoints are guaranteed empty, so neither adds to the removal count.
- **Cycles:** Strict distance improvement prevents cycles from causing endless processing.
