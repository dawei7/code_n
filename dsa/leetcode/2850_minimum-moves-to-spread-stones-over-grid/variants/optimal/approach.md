## General

**Convert movement into an assignment cost.** Every cell must finish with one stone. Keep one stone in each nonempty cell, expand every remaining stone into an entry in `extras`, and record every zero-valued cell in `empty`. Since the grid has nine cells and exactly nine stones, these two lists have the same length $k$.

Moving a stone from `(source_row, source_col)` to `(target_row, target_col)` costs their Manhattan distance. A route of that length exists by taking the necessary vertical and horizontal steps. Conversely, each move changes the row or column by only one, so no route can use fewer steps. Intermediate cells do not impose capacity restrictions, which means one stone's route does not interfere with another's. The problem is therefore exactly a minimum-cost one-to-one matching from the $k$ surplus stones to the $k$ empty cells.

**Build the matching one surplus stone at a time.** A bitmask records which empty cells have already received a stone. For a mask with $i$ set bits, the first $i$ entries of `extras` have been assigned, so the next source is `extras[i]`. Try every unselected target, add its Manhattan distance, and relax the state with that target bit set.

Each transition adds one distinct target and assigns exactly one new surplus stone. Thus every full-mask path represents a valid bijection. Conversely, any bijection appears as one sequence of these target choices. The dynamic program keeps the least cost among all paths reaching each mask, so the full-mask value is the minimum over every legal redistribution.

## Complexity detail

There are $2^k$ masks. From each nonterminal mask, at most $k$ empty cells are considered, giving $O(k \cdot 2^k)$ time. The one-dimensional dynamic-programming table uses $O(2^k)$ auxiliary space. The coordinate lists use $O(k)$ additional space and are dominated by the table. Here $k \le 8$ because the grid has only nine cells.

## Alternatives and edge cases

- **Backtracking over target permutations:** Trying every unused empty cell for each surplus stone is correct, but it can explore $k!$ complete assignments and repeats equivalent subproblems that share the same set of filled cells.
- **Search over whole grid states:** Breadth-first search can move stones until it reaches the all-ones matrix, but it stores and revisits many intermediate configurations that the direct assignment formulation avoids.
- **Greedy nearest pairing:** Sending each source to its currently nearest empty cell can consume a target needed by another source and produce a nonminimal global matching.
- **Already balanced grid:** When $k=0$, the only mask is the full mask and its cost remains `0`.
- **Repeated source coordinates:** A cell containing several extra stones contributes the same coordinate multiple times. Treating those entries separately is necessary because each one fills a different empty cell.
- **Passing through occupied cells:** A stone may traverse any side-adjacent cells; only the final configuration requires one stone per cell, so Manhattan distance remains the exact transfer cost.
