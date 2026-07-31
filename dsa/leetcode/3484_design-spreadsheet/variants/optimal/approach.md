## General

**A formula is a query, not spreadsheet state**

The formula language contains only one addition and its result is returned immediately. No formula is assigned to a cell, so there are no dependencies to retain or propagate. The spreadsheet state is simply the current integer associated with each explicitly assigned cell.

Store those assignments in a hash map keyed by the complete cell reference. `setCell` writes the new value under that key. `resetCell` removes the key, making the cell indistinguishable from any cell that was never assigned. This sparse representation also satisfies the initial-zero rule without constructing all $26\cdot\texttt{rows}$ cells.

**Resolve the two operands independently**

Remove the leading `=` and split the remaining string once at `+`. An operand beginning with a decimal digit is a non-negative integer literal, so convert it to an integer. Otherwise it is a cell reference, and a hash lookup returns either its stored value or zero when the key is absent.

Adding the two resolved values gives exactly the requested formula result. The helper cannot confuse a reference with a number: valid references begin with an uppercase letter, while valid numeric operands begin with a digit.

**Why updates are immediately visible**

Every query reads the map at evaluation time. A later assignment replaces the value stored under the same reference, and a reset removes it. Consequently, the next formula observes the new value without any cached expression or dependent cell needing an update.

## Complexity detail

Let $q$ be the total number of method calls processed by the package adapter, and let $s$ be the maximum number of distinct cells that are assigned and not subsequently reset. Cell references and formulas have bounded length under the source constraints.

Each operation takes $O(1)$ expected time with hash-table access, so processing the complete operation list takes $O(q)$ expected time. The map contains at most $s$ entries and uses $O(s)$ auxiliary space. The constructor itself takes $O(1)$ time and space because zero-valued cells are implicit.

## Alternatives and edge cases

- **Dense matrix:** allocating all $26\cdot\texttt{rows}$ values also supports constant-time cell access, but eagerly spends $O(\texttt{rows})$ space and initialization time even when few cells are used.
- **List of assigned pairs:** preserves sparse storage but needs a linear search for reads, writes, or resets; across many operations this can degrade to $O(q^2)$ time.
- **Dependency graph:** is unnecessary because `getValue` returns a sum immediately and never stores a formula in a cell.
- **Unset and reset cells:** both must resolve to zero; removing keys makes the two states behave identically.
- **Operand classification:** numeric operands are non-negative, so checking the first character is sufficient; a letter always denotes a cell reference.
- **Repeated operands:** a formula such as `=A1+A1` performs two reads and correctly doubles the cell's current value.
