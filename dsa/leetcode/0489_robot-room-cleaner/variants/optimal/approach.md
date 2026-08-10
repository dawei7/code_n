## General

The robot cannot inspect the room grid, learn its absolute row and column, or teleport back to an earlier cell. It can only sense whether a forward move succeeds. The solution nevertheless performs an ordinary depth-first search by creating its own coordinate system relative to the starting position.

The starting cell is called `(0, 0)`, regardless of its hidden grid coordinates. Direction numbers are

- `0` for up,
- `1` for right,
- `2` for down,
- `3` for left.

The tuple `dirs = (-1, 0, 1, 0, -1)` stores all four movement vectors compactly. For direction `d`, the row change is `dirs[d]` and the column change is `dirs[d + 1]`. This yields `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)` in clockwise order.

These coordinates never need to match the room's real indices. They only need to be consistent: taking one step up from a relative coordinate and later taking one step down must return to the same relative coordinate. The initial orientation is guaranteed to be up, so the first call `dfs(0, 0, 0)` aligns the virtual direction system with the physical robot.

**The recursive entry contract.** Whenever `dfs(i, j, d)` begins, two facts hold:

1. the physical robot is standing on the cell represented by relative coordinate `(i, j)`;
2. the robot is physically facing direction `d`.

The function adds `(i, j)` to `vis` and calls `robot.clean()`. Marking before exploring prevents a cycle from recursively entering the same cell again. Cleaning immediately guarantees that every reached open cell is cleaned even if all four neighboring moves fail.

**Explore four directions in physical and virtual lockstep.** The loop uses `k = 0, 1, 2, 3`. It computes `nd = (d + k) % 4`, so the attempted directions are the entry direction, then one right turn from it, then two, then three. At the beginning of iteration `k`, the physical robot also faces `nd`. That correspondence is maintained because every iteration ends with exactly one `robot.turnRight()`.

The prospective coordinate is

`x, y = i + dirs[nd], j + dirs[nd + 1]`.

If `(x, y)` is already visited, the algorithm treats it as a virtual obstacle and does not move there. If it is unvisited, `robot.move()` attempts the physical step. A failed move identifies a wall and leaves the robot on `(i, j)`. A successful move establishes that the neighbor is open and places the robot exactly where the recursive call expects: at relative coordinate `(x, y)` facing `nd`.

**Physically backtrack after recursion.** Returning from a normal software DFS call does not move the robot. After `dfs(x, y, nd)` finishes, the robot is still standing in the child cell. The parent must restore both position and orientation before trying its next direction.

The four operations

`turnRight(), turnRight(), move(), turnRight(), turnRight()`

perform that restoration. Two right turns rotate `180` degrees, so the robot faces back toward the parent. `move()` crosses the same open edge used to enter the child and therefore succeeds. Two more right turns restore the original child-entry orientation `nd`. The unconditional right turn at the bottom of the parent's loop then changes the facing direction to `nd + 1`, ready for the next iteration.

This orientation accounting is essential. Omitting the final two turns after moving back would leave the robot facing opposite the virtual direction. Omitting the one turn at the end of every iteration would make the computed `nd` disagree with the direction in which `move()` actually tries to travel.

**Why a recursive call returns in the expected orientation.** Inside any call, the four loop iterations make four right turns in total. Four quarter-turns complete a full rotation. Every recursive excursion restores the cell and the direction that existed immediately before that excursion. Therefore `dfs(i, j, d)` returns with the robot again on `(i, j)` facing `d`. This is the induction property that makes the parent's backtracking sequence valid at every depth.

**Why every accessible cell is reached.** Treat each open cell as a graph vertex and each shared open side as an edge. At every visited vertex, the loop considers all four possible edges. A successful move along an edge to an unvisited vertex launches DFS there. The visited set prevents infinite cycling but never blocks the first entry to an open vertex. Since the contract guarantees all empty cells are connected to the start, ordinary DFS reachability implies every empty cell is eventually visited and cleaned.

Walls do not need entries in `vis`. A failed move costs only a constant operation and does not recurse. The same wall may be sensed from nearby cells, but every open cell has only four sides, so the total number of failed and successful directional attempts remains linear in the number of cleaned cells.

For a one-cell room, the initial call marks and cleans `(0, 0)`. All four moves fail against surrounding walls, with a right turn after each failure. After four turns the robot again faces up, and the function returns. No special case is necessary.

The method returns `None` because the result is the physical side effect: every reachable cell has received a `clean` command. Neither the relative coordinate map nor the final robot position is part of the requested output.

## Complexity detail

Let $c$ be the number of accessible cells. Each accessible cell enters `dfs` once because it is added to `vis` before neighbors are explored. Each call checks exactly four directions, and every check performs a constant number of robot operations apart from a recursive traversal charged to another cell. Total time is therefore $O(c)$.

The visited set stores one relative coordinate per accessible cell, using $O(c)$ space. In a path-shaped room, recursive DFS can reach depth `c`, so the call stack also uses $O(c)$ space. The combined auxiliary-space bound remains $O(c)$.

## Alternatives and edge cases

- **Iterative DFS with an explicit stack:** It can avoid Python recursion depth, but each stack frame must preserve both exploration direction and the physical route needed to restore the robot. The recursive entry/exit contract expresses that bookkeeping naturally.
- **Breadth-first search:** A queue can plan graph exploration, but the physical robot still has to travel between queued cells and cannot teleport. DFS matches physical backtracking much more directly.
- **Wall-following alone:** Always turning at walls can traverse some boundaries but does not reliably explore every branch in an arbitrary connected room. The visited-coordinate DFS explicitly returns to branch points.
- **Unknown absolute location:** Relative `(0, 0)` coordinates are sufficient. Translation of every coordinate by the hidden start position would describe the same adjacency graph.
- **Unknown dimensions:** The algorithm stops by exhausting reachable neighbors, so it never needs `m` or `n`.
- **Failed move:** The robot remains in place, exactly as the parent loop assumes before its unconditional right turn.
- **Previously visited neighbor:** The algorithm does not physically enter it. It simply rotates to the next direction, avoiding cycles.
- **Single-cell room:** The cell is cleaned once, four wall checks fail, and four right turns restore the initial orientation.
- **Long corridor:** Recursion depth can be linear in the number of cells. The asymptotic space bound includes this stack depth, and a language recursion limit may motivate an explicit-stack implementation.
- **Backtracking move must succeed:** It traverses the same open edge by which the child was entered; room geometry does not change, so no obstacle can appear on that return edge.
- **Clean exactly once versus at least once:** `vis` ensures each cell's DFS call and `clean()` occur once. The requirement only needs every cell cleaned, but avoiding repeated cleaning also limits work.
