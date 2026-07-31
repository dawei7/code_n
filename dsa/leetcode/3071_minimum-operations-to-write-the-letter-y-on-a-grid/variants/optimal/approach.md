## General

**Separate geometry from target values.** Let `middle = n // 2`. A cell `(row, column)` belongs to the Y when it lies on either upper diagonal, `row <= middle` and (`column == row` or `column == n - 1 - row`), or on the lower vertical stem, `row >= middle` and `column == middle`. These conditions intentionally overlap at the center but each matrix cell is visited only once.

**Count the three values in both regions.** Maintain one three-entry frequency array for Y cells and another for background cells. A single traversal classifies every cell geometrically and increments the frequency of its current value in the corresponding region.

**Evaluate every legal final coloring.** There are only three possible values. For each ordered pair of distinct values `(y_value, background_value)`, the cells already correct are exactly `counts[Y][y_value] + counts[background][background_value]`. Every other cell needs one operation, so the cost is $n^2$ minus that sum. Take the minimum over the six ordered pairs.

For any chosen pair, the computed cost is necessary because every mismatching cell must change, and it is sufficient because changing each such cell once produces that coloring. Since every valid final grid uses one of the six distinct pairs, the minimum evaluated cost is globally optimal.

## Complexity detail

The matrix contains $n^2$ cells, each classified and counted once, so the traversal takes $O(n^2)$ time. Evaluating six value pairs is constant work. The two frequency arrays always contain six counters, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Construct a Y-coordinate set:** Precomputing all Y positions makes membership explicit, but it needs $O(n)$ additional space and hash lookups that the direct coordinate test avoids.
- **Rescan for every value pair:** Testing all six target pairs by traversing the entire matrix each time remains $O(n^2)$ because six is constant, but it repeats the dominant work and hides the useful frequency reduction.
- **Try only unordered pairs:** The roles are not interchangeable: assigning `0` to the Y and `1` to the background can cost differently from the reverse assignment, so all six ordered pairs are required.
- **Center overlap:** The two diagonals and the stem meet at one center cell; visiting cells rather than drawing three separate segments prevents counting it multiple times.
- **Minimum grid:** For $n=3$, the Y has five cells and the background has four, and the same classification applies without a special case.
- **Already valid:** One ordered pair retains every cell, producing a cost of zero.
- **Single initial value:** The final Y and background must differ, so one of the two regions must change even when the starting matrix is uniform.
- **Third value:** A final coloring uses two distinct values; cells containing the unused third value necessarily change unless that value is selected for their region.
