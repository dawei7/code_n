## General
**Enumerate the bounded neighborhood of each cell**

Create a separate result matrix so original values remain available while later cells are computed. For output position `(row, column)`, inspect row offsets and column offsets from `-1` through `1`. Include a candidate only when both coordinates remain inside the image, accumulating its value and the number of included cells.

**Apply floor division after the complete sum**

Store `total // count` in the output cell. Corners average four cells, non-corner boundary cells average six, interior cells average nine, and smaller image dimensions naturally reduce those counts further.

Every included coordinate differs by at most one on each axis, so it belongs to the required neighborhood. Conversely, the two offset loops visit every in-bounds coordinate satisfying that condition exactly once. The accumulated quotient is therefore precisely the required floored average for every cell.

## Complexity detail
There are $R \cdot C$ output cells, and each checks at most nine candidates, giving $O(R \cdot C)$ time. The returned matrix uses $O(R \cdot C)$ space; aside from the output, only constant-sized counters are needed.

## Alternatives and edge cases
- **Two-dimensional prefix sums:** answer each clipped neighborhood sum in constant time after $O(R \cdot C)$ preprocessing, but the fixed 3×3 kernel makes direct enumeration simpler.
- **Encode results in the original cells:** can reduce auxiliary space by preserving old bits and writing new bits separately, but it obscures the straightforward read-old/write-new contract.
- **Scan the entire image for every output cell:** is correct when filtering by coordinate distance, but takes $O((R \cdot C)^2)$ time.
- A one-cell image remains unchanged.
- One-row and one-column images average only the existing linear neighbors.
- Floor division occurs after summing all valid neighbors, not after incremental pairwise averaging.
