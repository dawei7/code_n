## General

Represent an unvisited cell by `-1` and write `0` at the requested start. A depth-first search then extends the partial tour one visit number at a time. From the current cell, generate each of the eight possible knight offsets, discard destinations outside the board or already numbered, and tentatively write the next visit number. If the recursive branch cannot fill the board, restore that cell to `-1` before trying another move.

**Choosing constrained moves first**

For each candidate destination, count how many unvisited knight moves would remain from it. Explore candidates in increasing order of this onward degree. This Warnsdorff-style ordering does not discard any move, so it preserves the completeness of backtracking, but it tends to expose dead ends early and reaches a valid tour quickly on the guaranteed-solvable boards.

At every recursive call, the numbered cells form one simple legal knight path starting at `(r, c)`: the algorithm adds only an unvisited cell reached by a valid offset, and backtracking removes additions in reverse order. When the next visit number equals $mn$, the board contains every integer from $0$ through $mn-1$ exactly once, so the invariant proves the board encodes a full tour. Conversely, ordinary exhaustive backtracking considers every legal continuation; candidate sorting changes only their order. Therefore, the search will find a tour whenever the input guarantee says one exists.

## Complexity detail

In the worst case, each of the $mn$ visits can branch to as many as eight moves, giving the conservative time bound $O(8^{mn})$. Degree calculation and sorting involve at most eight candidates and therefore contribute only constant work per search state. The board and recursion stack use $O(mn)$ space.

Because $m,n \le 5$, the legal workload contains at most 25 cells and cannot support honest asymptotic runtime tiers. A bounded-domain certificate replaces scaling with validation of every legal dimension/start tuple and every emitted knight transition.

## Alternatives and edge cases

- **Unordered backtracking:** Trying the eight moves in a fixed order remains correct, but it can spend far longer exploring avoidable dead ends.
- **Warnsdorff without backtracking:** Always committing to the least-degree move is fast but is only a heuristic; retaining backtracking is what guarantees a solution for every promised input.
- **Bitmask state search:** A visited-cell bitmask can memoize dead states, but the board matrix is still needed for the requested visit ordering and the state set can be exponential.
- A `1 x 1` board is already a complete tour and must return `[[0]]`.
- Rectangular boards require independent row and column bounds; swapping `m` and `n` changes the coordinate system.
- The start must remain numbered `0`, even if another valid tour would naturally be described from its opposite endpoint.
- Output is not unique; correctness depends on the visit permutation and knight transitions, not equality with one example matrix.
