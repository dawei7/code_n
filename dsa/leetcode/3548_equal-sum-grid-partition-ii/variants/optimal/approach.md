## General

For a fixed cut, let the two section sums be $A$ and $B$. If they differ, only the larger section can supply a discounted cell, and that cell's value must be exactly $\lvert A-B\rvert$. This turns the numeric part of each cut check into a prefix sum plus a membership query.

**Why four directional scans are sufficient.** A helper scans horizontal boundaries from top to bottom and considers only cases where the accumulated prefix is the larger section. It maintains the prefix sum and a set of values already included. Reversing the row order makes every larger bottom section become a larger prefix for the corresponding boundary. Transposing the grid converts vertical cuts into horizontal cuts; scanning that matrix in both row directions covers larger left and larger right sections. Thus the four calls examine every cut and both choices of larger side.

At each helper boundary, `difference = 2 * prefix - total`. A zero difference means the sums already match. A positive difference is exactly the value that must be discounted from the prefix. Negative differences are deliberately left to the reverse-direction call.

**Connectivity determines the membership rule.** Removing one cell from a rectangle with at least two rows and two columns cannot disconnect the remaining cells: routes can detour around the missing position. Therefore, in that case it is enough for `difference` to occur anywhere in the prefix set. A one-row section is a path of cells, so only its left or right endpoint may be removed. A one-column section is also a path, so only its top or bottom endpoint is safe. A one-cell prefix has no valid discount because removing its only cell leaves no connected remainder; the endpoint logic is reached only at legal boundaries and cannot manufacture a value match unless another cell remains along the row or column.

Every helper considers all its boundaries, and the four orientations cover all possible larger sections. A returned `true` therefore supplies a legal cut and discount, while exhausting the scans proves none exists.

## Complexity detail

Let $N=mn$ be the number of cells. Each directional helper scans its matrix once and performs expected $O(1)$ hash-set operations, so all four scans take $O(N)=O(mn)$ expected time. The transposed matrix and seen-value sets use $O(N)=O(mn)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **Per-value coordinate bounds:** Recording minimum and maximum row and column positions also answers full-strip membership queries in $O(mn)$ time and can avoid materializing every directional view, but requires more specialized boundary logic.
- **Recompute each section for every cut:** This is correct with an explicit connectivity check but can take $O((m+n)mn)$ time.
- **Two-dimensional prefix matrix:** It answers rectangle sums quickly but does not by itself solve value membership or the one-dimensional connectivity restriction.
- **Already equal sums:** A zero difference succeeds without discounting any cell.
- **Single-row section:** Only the first or last cell may be discounted; an interior removal splits the section.
- **Single-column section:** Only the top or bottom cell may be discounted for the same reason.
- **Two-dimensional section:** Any one cell may be discounted without disconnecting the remainder.
- **Discount from the suffix:** Reversing the appropriate orientation turns it into the same prefix case instead of duplicating logic.
- **Positive entries:** The smaller section can never be made equal by discounting a positive value, so only the larger side needs inspection.
