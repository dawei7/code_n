## General
**End each directional run at the current cell**

When `mat[row][column]` is one, its horizontal run extends the cell to the left, its vertical run extends the cell above, its diagonal run extends the upper-left cell, and its anti-diagonal run extends the upper-right cell. A zero resets all runs ending there.

**Keep horizontal and vertical state directly**

A scalar tracks the current row's horizontal run and resets at each zero or new row. An array indexed by column tracks vertical runs and is updated in place as rows advance.

**Separate previous-row diagonal arrays**

Store diagonal and anti-diagonal lengths from the previous row. Build fresh arrays for the current row so an update cannot overwrite a value still needed by a later column.

**Update the global maximum at every one**

The four values ending at a cell cover every allowed line whose final cell is there. Comparing all of them against the best seen so far captures lines in every direction.

**Why every maximal line is measured**

Choose the endpoint reached last in row-major processing for any allowed line. Its preceding cell lies left, above, upper-left, or upper-right according to the direction, and the corresponding recurrence has accumulated exactly the line's consecutive ones since the most recent zero or boundary. Thus every line contributes its length at an endpoint, while each stored run follows only adjacent ones in one legal direction.

## Complexity detail
Every one of the `r × c` cells performs constant work, giving $O(rc)$ time. The vertical, previous-diagonal, current-diagonal, and anti-diagonal arrays each have `c` entries, so auxiliary space is $O(c)$.

## Alternatives and edge cases
- **Full three-dimensional DP table:** stores four lengths per cell and uses $O(rc)$ space without improving time.
- **Scan four directions from every one:** is correct but repeatedly revisits cells and can take $O(rc \cdot \max(r, c))$ time.
- **All zeros:** produces zero because no run is extended.
- **Single row:** only horizontal runs can exceed one.
- **Single column:** only vertical runs can exceed one.
- **Anti-diagonal:** must read the previous row's next column, not the current row.
- **Zeros between runs:** reset the relevant directional state and prevent separated ones from combining.
