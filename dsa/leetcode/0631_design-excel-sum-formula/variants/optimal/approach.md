## General
**Store exact direct formulas**

Represent each cell by zero-based row and column indices. Expand every individual reference and inclusive range into a `Counter` from source cells to multiplicities. The counter preserves duplicate and overlapping references while storing each distinct source coordinate once.

**Maintain reverse dependency edges**

For each source cell, also keep the formula cells that directly depend on it. Replacing a formula removes its old reverse edges before a literal or new formula is installed. Downstream formulas that reference the overwritten cell remain connected because only that cell's incoming formula is replaced.

**Refresh each affected formula once**

After a cell's numeric value changes, follow reverse edges to collect the distinct downstream cells that can be affected. Within that induced acyclic subgraph, count each cell's affected formula dependencies. Process zero-indegree cells with a queue; once all changed predecessors of a formula are current, recompute that formula directly from its source values and enqueue it. The no-cycles guarantee ensures every affected cell is eventually processed.

This topological schedule is essential for reconverging dependencies. If two paths from `A1` meet again at a later formula, that formula waits for both paths and is recomputed once. Recursive path-by-path delta forwarding would instead revisit it once per path and can take exponential time on a legal layered diamond.

**Why stored values remain current**

Construction initializes every literal value to zero. A new formula is evaluated from source cells that are already current. On every later change, the topological refresh orders all affected formulas after their changed predecessors and recomputes their exact weighted sums. Induction along that order shows that every stored value is current, so `get` can return it immediately.

## Complexity detail
Let $N$ be the number of distinct affected cells and let $F$ be the total formula-reference work touched by an operation, including expanded input references and stored source relationships in the affected subgraph. Parsing or replacing a formula and refreshing its downstream cells take $O(N + F)$ worst-case time, while `get` takes $O(1)$ time. Across the sheet, cell values, formula counters, reverse edges, and temporary traversal state occupy $O(N + F)$ space.

## Alternatives and edge cases
- **Recursive evaluation on every read:** Storing formulas and expanding them only in `get` is simpler, but repeated reads or reconverging dependencies can retraverse the same subgraph exponentially many times.
- **Recursive delta propagation:** Forwarding each change immediately along every path keeps reads constant-time, but a downstream cell is revisited for every reconverging path and violates the required $O(N + F)$ update bound.
- **Full-sheet recomputation:** Rebuilding every formula after each assignment is correct but spends work on cells unrelated to the change.
- **Blank cells:** Every cell is `0` until a literal or formula assigns it.
- **Inclusive ranges:** A range contains both corners and every row and column between them.
- **Reference multiplicity:** Duplicate entries and overlapping ranges contribute once per occurrence, never once per distinct cell.
- **Overwrite semantics:** Both `set` and `sum` remove the target's previous incoming formula edges while preserving formulas that depend on the target.
- **Acyclicity:** The input excludes circular sum references, which makes the affected dependency subgraph topologically orderable.
