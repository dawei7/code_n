## General

**Store both current values and dependency information.** A formula cell cannot be treated as a one-time sum. If one of its sources changes later, the formula cell and anything depending on it must change too. The exact class maintains three synchronized structures:

- `values` is the rectangular matrix of current integer values;
- `formulas[target]` is a `Counter` mapping every direct source cell to how many times it appears in the target's formula;
- `dependents[source]` is the reverse mapping from a source to formula targets that use it, again with multiplicity.

The forward formula answers “what does this target read?” The reverse graph answers “which targets must change when this source changes?” Keeping both directions makes overwriting formulas and propagating updates efficient.

Cells are represented internally as zero-based tuples `(row, column)`. `cell("F7")` converts the row text to 6 and the letter to column offset 5. Public methods translate their one-based row and letter column in the same way.

**Expand formula references without losing multiplicity.** `references(numbers)` accepts both single cells and rectangles. Splitting on `":"` produces one endpoint for a single reference and two for a range. Using `endpoints[0]` and `endpoints[-1]` therefore handles both forms uniformly.

The nested loops include every row from top through bottom and every column from left through right. Each encountered cell increments a `Counter` entry. Multiplicity matters:

- `["A1", "A1"]` means twice the value of A1;
- `["A1", "A1:B2"]` includes A1 once directly and once through the range, so its coefficient is 2;
- overlapping ranges similarly add their contributions.

Replacing the counter with a set would silently produce incorrect sums.

**Remove an old formula before assigning a new meaning.** `remove_formula(cell)` pops the target's old forward map. For every old source and multiplicity, it subtracts the same amount from `dependents[source][cell]`. Zero-count target entries are deleted, and an empty reverse bucket is deleted too.

This cleanup is required for both `set` and `sum`. Once a formula cell is overwritten, changes to its former sources must no longer propagate into it. Merely changing the value while leaving reverse edges would create stale dependencies.

**Propagate value differences rather than recomputing whole formulas.** Suppose source cell `x` changes by `difference`. If target `y` references `x` with multiplicity `m`, then `y` changes by

$$
\texttt{difference}\cdot m.
$$

`propagate` applies that amount directly to the stored target value and recursively propagates the target's own change to its dependents. This works because every supported formula is linear addition: a change in one input causes exactly the same coefficient-scaled change in the sum.

The call uses `list(...items())` to take a snapshot of the current dependent entries. The method itself does not normally edit those edges, but a snapshot prevents iteration from being coupled to dictionary-view mutation.

If the difference is zero, no stored result changes, so returning immediately is both safe and efficient.

**How `set` changes a cell.** The method:

1. saves the target's old current value;
2. removes any formula and its reverse edges;
3. writes the literal `val`;
4. propagates `val - old_value`.

Removing the formula does not erase the target's old value first. That old value is exactly what is needed to compute the delta seen by downstream formulas. After the call, the target is a literal cell and no longer reacts to former sources.

**How `sum` installs a persistent formula.** The method also saves the old value and removes any former formula. It then expands `numbers` into a source counter and evaluates

`source current value * multiplicity`

for every distinct source. It stores the forward formula and adds matching reverse edges from each source to the target. Finally, it writes the new sum, propagates the difference from the target's old value, and returns the new value.

Registering reverse dependencies is what makes the formula persist. If a referenced cell changes later, propagation reaches this target automatically.

In the sample, C3's formula contains A1 twice and B1, A2, B2 once. With A1 equal to 2 and the other cells zero, C3 is 4. When B2 changes from 0 to 2, the reverse graph says C3 depends on B2 once, so C3 receives a delta of 2 and becomes 6.

**Why recursive propagation is correct.** The problem guarantees no circular references, so the dependency graph is a directed acyclic graph. At every direct edge, the method sends exactly the source's value change multiplied by that edge's coefficient. If a target is reachable by several dependency paths, it receives the contribution from every path; linear sums require those contributions to add. Recursing onward sends each received target delta through the next coefficients. Therefore every stored cell remains equal to the formula evaluated from current source values.

`get` can consequently return the matrix entry in constant time. It never needs to evaluate a formula lazily.

## Complexity detail

Let $N$ be the number of sheet cells, $F$ the number of stored distinct direct dependency entries, $E$ the number of cell occurrences expanded by one new formula, and $D$ the maximum dependency depth.

Construction allocates $O(N)$ value storage. Parsing and evaluating a new formula costs $O(E)$ before propagation. Removing an old formula costs time proportional to that target's direct-source count. `get` is $O(1)$.

If every affected node and edge is processed once, update propagation is $O(N+F)$, which is the intent of the manifest bound. The exact recursive delta implementation can revisit a cell through multiple dependency paths and then traverse its outgoing edges again. Its honest cost is proportional to the number of affected path-edge traversals, which can exceed $O(N+F)$ and can be exponential in a densely converging DAG's path count. The small sheet and call limits contain this risk, but the distinction should not be hidden.

Persistent storage is $O(N+F)$ for values plus forward and reverse dependency counters. A propagation chain uses $O(D)$ recursion stack. Counters store multiplicity as an integer rather than duplicating an edge once per occurrence.

## Alternatives and edge cases

- **Topological recomputation:** After a change, collect affected cells and evaluate each once in dependency order. This gives a firmer $O(N+F)$ affected-subgraph bound and avoids repeated work from converging paths.
- **Lazy formula evaluation:** Store formulas but calculate on `get`. It simplifies updates but can repeatedly traverse large dependency graphs and needs cycle protection.
- **Scan all formulas after every change:** The editorial approach can discover dependents without reverse edges, but repeated whole-sheet scans are expensive.
- **Overlapping ranges:** Counter multiplicities ensure a cell included twice contributes twice.
- **Formula overwritten by `set`:** Old reverse edges are removed, so former sources stop affecting the target.
- **Formula overwritten by another `sum`:** The old graph links are removed before the new formula is registered.
- **Reference to a zero cell:** It contributes zero initially but remains connected, so a later change propagates.
- **Difference zero:** Downstream values do not change, and propagation stops immediately.
- **Diamond-shaped dependencies:** A downstream cell receives deltas along both paths, which is numerically correct but may cause repeated traversal.
- **Circular formulas:** The contract forbids them. Without that guarantee, recursive propagation could loop forever and values would be ill-defined.
- **Inclusive rectangles:** Both endpoint rows and columns are included by the `+ 1` loop bounds.
- **Multi-digit rows:** `reference[1:]` correctly parses rows such as `A26` rather than assuming one digit.
