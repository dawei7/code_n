## General

**Store only cells that have been explicitly assigned.** Every spreadsheet cell begins at zero, so allocating all `rows * 26` positions is optional. The protected class keeps dictionary `self.d` from a cell-reference string such as `"A1"` to its current explicitly stored value.

The constructor accepts `rows` because the required interface includes it, but the source does not use the number to allocate storage or validate references. Valid cell references are guaranteed by the problem, so no runtime bounds check is needed.

**Setting a cell is a direct dictionary update.** `setCell(cell, value)` assigns `self.d[cell] = value`. Setting the same cell again replaces its previous mapping, which matches spreadsheet assignment semantics. The dictionary key is the complete reference string, so no row-and-column parsing is needed for storage.

The source also stores an explicit value of zero if `setCell` is called with zero. Such an entry behaves correctly, though it still occupies dictionary space until reset or overwritten.

**Reset by removing the explicit mapping.** `resetCell` calls

`self.d.pop(cell, None)`.

If the cell was present, its entry is deleted and future lookup falls back to the implicit default zero. If it was never set or was already reset, the default argument `None` prevents an exception. Resetting is therefore idempotent.

Deleting rather than storing another zero keeps reset cells out of the sparse representation.

**Parse the formula into its two operands.** A formula always starts with `=` and has form `=X+Y`. `formula[1:]` removes the equals sign, and `split("+")` separates the operands. The source loops over the two resulting tokens and accumulates their values in `ans`.

If `cell[0].isdigit()` is true, the token is a nonnegative integer literal and `int(cell)` converts it. Otherwise, the token starts with an uppercase column letter and is treated as a cell reference. `self.d.get(cell, 0)` returns its stored value or the required default zero.

The variable is named `cell` for both operand kinds, but its first character reliably distinguishes them under the input grammar. Negative integer literals do not need handling because values are nonnegative.

For `=5+7`, both tokens are numeric and the method returns twelve without touching the dictionary. After `setCell("A1", 10)`, `=A1+6` retrieves ten and adds six. After resetting `A1`, the same lookup returns default zero.

Although only two operands are promised, the loop would also sum more plus-separated operands if passed. This extra generality does not interfere with the specified format.

**Why string keys are sufficient.** Cell references are canonical: one capital letter followed by a valid one-indexed row number. Two references name the same cell exactly when their strings are equal. There are only 26 columns, but no conversion to numeric coordinates is required for equality or lookup.
After any sequence of updates, the dictionary contains the most recently assigned value for every explicitly set, non-reset cell; cells absent from it have semantic value zero. The constructor establishes the invariant with an empty dictionary. `setCell` establishes the requested mapping, and `resetCell` removes it without changing others. During `getValue`, each numeric token is interpreted as its literal value and each cell token is evaluated according to this invariant. Adding the two operand values therefore returns exactly the formula result.

The evaluation does not store formulas or dependencies. The contract asks only for immediate sums, so changing a cell automatically affects later calls because each call performs fresh dictionary lookups.

## Complexity detail

Let $q$ be the total number of method calls and $s$ the number of dictionary entries currently stored. Dictionary set, pop, and get operations take expected $O(1)$ time. Parsing a reference or formula technically costs time proportional to its short string length, but column count, row digits, and numeric literal digits are bounded by the constraints. Under the problem's model, each operation is $O(1)$ expected time and all $q$ calls cost $O(q)$, matching the manifest.

The dictionary uses $O(s)$ space, where $s$ is the number of distinct cells explicitly set and not reset. The object does not allocate by the declared row count. Formula splitting creates only two bounded-size token strings per call, so temporary auxiliary space is constant under the stated limits.

Worst-case `s` is the number of distinct cells touched by up to $10^4$ calls, bounded also by `26 * rows`.

## Alternatives and edge cases

- **Allocate a full two-dimensional grid:** It gives direct indexed access but uses $O(26\cdot rows)$ space even when very few cells are set.
- **Parse references into numeric coordinates:** This is necessary for an array grid but optional for a dictionary with canonical string keys.
- **Store reset cells as zero:** It is correct but keeps unnecessary entries; removing them restores the sparse default representation.
- **Unset cell in a formula:** `get(cell, 0)` supplies the required zero.
- **Repeated `setCell`:** Dictionary assignment replaces the old value, so only the latest setting matters.
- **Repeated `resetCell`:** `pop(..., None)` makes resetting an absent cell harmless.
- **Explicitly set zero:** The source stores it until reset; value semantics are still identical to an absent cell.
- **Two numeric operands:** No spreadsheet state is needed and both tokens are converted with `int`.
- **Two cell operands:** Each is looked up independently, including when both references are the same.
- **Mixed operand order:** The token test handles either `cell+number` or `number+cell`.
- **Constructor row count:** The source ignores it because inputs guarantee valid references; an API requiring validation would need to retain and check it.
- **No formula caching:** Results should reflect the latest cell values, so evaluating fresh lookups is the correct simple design.
