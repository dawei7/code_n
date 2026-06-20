# 8-Puzzle (Branch and Bound)

| | |
|---|---|
| **ID** | `bb_04` |
| **Category** | branch_and_bound |
| **Complexity (required)** | $O(b^d)$ Worst Case |
| **Difficulty** | 8/10 |
| **Interview relevance** | 5/10 |
| **Wikipedia** | [15 puzzle](https://en.wikipedia.org/wiki/15_puzzle) |

## Problem statement

Given a 3 x 3 grid with 8 numbered tiles and one empty space, find the minimum number of moves to reach the target configuration. A move consists of sliding an adjacent tile into the empty space.
This is exactly the same as finding the shortest path in an unweighted graph, which you *could* do with standard BFS. However, the state space for the 15-puzzle is 10^{13}, and BFS would instantly run out of memory.
You must solve this using **Branch and Bound** with a Priority Queue (which, in this specific pathfinding context, is mathematically identical to the **A* Search algorithm**).

**Input:** A 3 x 3 matrix representing the start state, and a target state matrix.
**Output:** The minimum number of moves required (or the sequence of moves).

## When to use it

- To solve grid-sliding puzzles, Rubik's Cubes, or any deterministic pathfinding problem with a massive state space where the optimal sequence length is required.

## Approach

In Branch and Bound (or A*), we prioritize exploring states that have the lowest **total estimated cost**, denoted as f(x) = g(x) + h(x).
1. **g(x) - The "Branch" Cost:** The number of moves we have made so far from the start state to reach the current state.
2. **h(x) - The "Bound" (Heuristic):** The estimated *minimum* number of remaining moves required to reach the target.
   - For the puzzle, we use the **Manhattan Distance heuristic**. For every tile, calculate how many rows and columns it is away from its correct target position. The sum of these distances is our absolute lower bound! (Because a tile can only move 1 square at a time, it physically cannot reach its destination in fewer moves than its Manhattan distance).
   - *Note: A heuristic is valid for B&B/A* only if it is "admissible" (it never overestimates the true cost).*

**Algorithm:**
1. Insert the start state into a Min-Heap (Priority Queue), ordered by f(x) = g(x) + h(x).
2. While the Heap is not empty:
   - Pop the state with the lowest f(x).
   - If the state exactly matches the target state, you are done! Return g(x). (Because the heuristic is admissible, the first time we pop the target, it is mathematically guaranteed to be the shortest path).
   - Generate all valid next moves (sliding adjacent tiles into the blank space).
   - For each child state, calculate its new g(x) = parent\_g + 1 and its new h(x).
   - Insert child states into the Min-Heap.
   - *(Optimization: Track visited states in a HashSet so you don't loop endlessly).*

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bb_04: 8-Puzzle (Branch and Bound).

Solve the 8-puzzle (3x3 sliding-tile puzzle with
"""


def solve(start, goal):
    """8-puzzle via B&B with misplaced-tiles heuristic.

    Return the minimum number of moves (depth) of the goal
    node, or -1 if no solution is found within the search
    budget.
    """
    import heapq
    N = 3
    # Flatten the goal to a tuple for O(1) hashing.
    goal_flat = tuple(sum(goal, []))

    def misplaced(board_flat):
        return sum(1 for i, v in enumerate(board_flat) if v != 0 and v != goal_flat[i])

    def neighbors(board, zr, zc, parent_z):
        """Yield (new_board, new_zr, new_zc, move_id) for the four
        possible moves of the blank, skipping the parent
        direction (encoded as the previous (zr, zc))."""
        out = []
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = zr + dr, zc + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) != parent_z:
                # Move blank from (zr, zc) to (nr, nc).
                new = list(board)
                bi = zr * N + zc
                ni = nr * N + nc
                new[bi], new[ni] = new[ni], new[bi]
                out.append((tuple(new), nr, nc))
        return out

    # Find the blank in start.
    start_flat = tuple(sum(start, []))
    try:
        z0 = start_flat.index(0)
    except ValueError:
        return -1
    zr0, zc0 = z0 // N, z0 % N

    # Each entry: (cost, counter, board_flat, zr, zc, depth, parent_z)
    # cost = depth + misplaced(board). We use a counter to break
    # ties so equal-cost nodes are processed FIFO.
    counter = 0
    pq = [(misplaced(start_flat), 0, start_flat, zr0, zc0, 0, None)]
    seen = {start_flat: 0}  # board_flat -> best depth seen
    while pq:
        cost, _, board, zr, zc, depth, parent_z = heapq.heappop(pq)
        if board == goal_flat:
            return depth
        if seen.get(board, float("inf")) < depth:
            continue
        for new_board, nr, nc in neighbors(board, zr, zc, parent_z):
            new_depth = depth + 1
            if seen.get(new_board, float("inf")) <= new_depth:
                continue
            seen[new_board] = new_depth
            counter += 1
            new_cost = new_depth + misplaced(new_board)
            heapq.heappush(pq, (new_cost, counter, new_board, nr, nc,
                                new_depth, (zr, zc)))
    return -1
```

</details>

## Walk-through

*(Conceptual)*
Target state is `[[1, 2, 3], [4, 5, 6], [7, 8, 0]]`.
Current State: `[[1, 2, 3], [4, 5, 6], [7, 0, 8]]`.

1. **Calculate h(x):** Tile 8 is at `(2, 2)` in target, but `(2, 1)` here. Distance = 1. Blank space is ignored. h(x) = 1.
2. **Current Node:** g(x)=0, h(x)=1 -> f(x)=1. Pop from Heap.
3. **Move Blank Space (0 at 2,1):**
   - **Move Right (Swap with 8):** State becomes Target! g(x)=1, h(x)=0. f(x)=1.
   - **Move Left (Swap with 7):** h(x) increases because 7 moved away from its target!
   - **Move Up (Swap with 5):** h(x) increases because 5 moved away from its target!
4. **Next Heap Pop:** The "Move Right" state has the lowest f(x)=1. It is popped.
5. **Check:** h(x) == 0. We found the target in exactly g=1 move! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(d)$ | $O(d)$ |
| **Average** | Much faster than BFS | $O(Nodes Generated)$ |
| **Worst** | $O(b^d)$ | $O(b^d)$ |

*Where b is the branching factor (average ~3 moves per state) and d is the depth of the optimal solution.*
In the absolute worst case (e.g., if you use a useless heuristic like h(x)=0), the algorithm degenerates into standard Dijkstra's/BFS, generating the entire tree $O(b^d)$.
However, with a strong heuristic like Manhattan Distance, the algorithm heavily prunes the search space, diving directly toward the solution. Space complexity is often the bottleneck as the Priority Queue and Visited Set hold millions of states in memory for deep puzzles (like the 15-puzzle).

## Variants & optimizations

- **Linear Conflict Heuristic:** Manhattan distance assumes tiles can slide through each other. If Tile A and Tile B are in the correct row, but A is to the right of B, they must physically move out of the row to bypass each other! You can add +2 to the Manhattan heuristic for every linear conflict, making the bound much tighter and drastically reducing node expansions.
- **IDA* (Iterative Deepening A*):** To fix the massive memory usage of the Priority Queue, IDA* runs standard Depth-First Search with a strict cut-off limit on the f(x) bound. It uses $O(d)$ memory!

## Real-world applications

- **Robot Path Planning:** Safely navigating drones around physical obstacles to a destination coordinates in 3D space.

## Related algorithms in cOde(n)

- **[bb_03 - Least Cost B&B Knapsack](bb_03_0-1-knapsack-least-cost-b-b.md)** — The exact same Priority Queue exploration mechanism applied to an array instead of a grid.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
