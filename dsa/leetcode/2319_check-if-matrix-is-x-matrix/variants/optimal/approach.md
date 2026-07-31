## General

**Classify a cell from its coordinates**

A coordinate `(row, column)` lies on the main diagonal when `row == column`
and on the secondary diagonal when `row + column == n - 1`. If either equation
holds, the cell must be nonzero. If neither holds, it must be zero.

Scan every coordinate and compare that required category with the cell's zero
status. A diagonal coordinate containing zero or an off-diagonal coordinate
containing a nonzero value immediately disproves the X-matrix property. If the
scan finishes, every cell satisfies its unique requirement, so both defining
conditions hold.

## Complexity detail

The matrix contains $n^2$ cells and each is checked once, giving $O(n^2)$ time
and $O(1)$ auxiliary space. This is asymptotically optimal: any uninspected
cell could be changed into the only violation without affecting inspected
entries.

## Alternatives and edge cases

- **Check diagonals then the remainder:** Separate passes are correct but require careful handling to avoid overlooking or redundantly treating diagonal cells.
- **Build a coordinate set:** Materializing both diagonals simplifies membership tests but uses $O(n)$ extra space unnecessarily.
- **Odd-sized center:** The center belongs to both diagonals but has the same nonzero requirement.
- **Even-sized matrix:** The diagonals do not share a cell.
- **Nonzero magnitude:** Any positive value is valid on a diagonal; no particular value is required.
- **Early exit:** Finding one violating cell is sufficient to return false.
