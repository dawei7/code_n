## General
**Track which adjacent row pairs are already decided.** For each pair `strs[i]`, `strs[i + 1]`, remember whether an earlier kept column has already made the upper row strictly smaller. Once that happens, later columns cannot reverse this pair's lexicographic order.

**Reject a column only when it creates an unresolved inversion.** Scan columns from left to right. Before keeping a column, inspect every still-unresolved adjacent pair. If any has `strs[i][column] > strs[i + 1][column]`, keeping this column would make that pair permanently out of order at its first difference. The column must therefore be deleted, and no pair state changes.

**Commit every safe column.** If no unresolved pair is inverted, keep the column. Mark a pair resolved wherever its characters are strictly increasing in this column; pairs with equal characters remain unresolved. Keeping a safe column cannot harm an already-resolved pair, and deleting it could only discard useful information. Thus every deletion made by the greedy scan is forced, while every retained column is compatible with some optimal result. The deletion count is minimal when all columns have been considered.

## Complexity detail
Each of the $M$ columns examines at most $N-1$ adjacent pairs, giving $O(NM)$ time. The resolved-state array contains $N-1$ booleans and uses $O(N)$ space.

## Alternatives and edge cases
- **Rebuild retained prefixes:** After tentatively adding each column, reconstruct every row prefix and test whether the array is sorted. This follows the same greedy decisions but repeated prefix construction costs $O(NM^2)$ time.
- **Enumerate deletion subsets:** Testing every column subset finds the minimum but requires exponential time.
- **Confuse rows with columns:** The required order is between whole resulting strings; characters within a row may decrease.
- **Already resolved pair:** Later character inversions are irrelevant after an earlier kept character made the upper row smaller.
- **Equal rows:** They remain valid and may stay unresolved through every column.
- **One row:** There is no adjacent pair to violate the order, so zero deletions are needed.
