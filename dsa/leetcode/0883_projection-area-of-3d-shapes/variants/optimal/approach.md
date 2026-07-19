## General
**View each shadow as the visible extent of a tower line**

From above, every nonempty tower covers one unit square, regardless of its height. The $xy$-projection is therefore the number of positive entries in `grid`.

Looking along either horizontal axis merges all towers in the same line. In a fixed row, shorter towers are hidden behind the tallest tower, so that row contributes `max(row)` unit squares to one side projection. For the perpendicular side projection, column `j` contributes the greatest height appearing in that column.

**Accumulate all three projections in one row pass**

Maintain an array of column maxima. While visiting each cell, count it when its height is positive and update its column maximum; after each row, add that row's maximum. Finally, add the top count, the row maxima, and the column maxima.

This accounts for every visible unit square exactly once. The top count represents occupied base positions, while each row or column maximum is precisely the vertical extent of that line's shadow. Cubes below the maximum or behind another tower do not enlarge the relevant projection and are intentionally not counted again.

## Complexity detail
The matrix contains $n^2$ cells, and each is processed once, so the running time is $O(n^2)$. The column-maxima array stores $n$ heights and uses $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Scan height layers explicitly:** Testing which rows and columns contain a cube at every height is correct but costs $O(n^2 H)$ time when $H$ is the maximum tower height.
- **Use three separate matrix passes:** Counting positive entries and then scanning every row and column remains $O(n^2)$ and can use $O(1)$ auxiliary space, but it revisits the matrix.
- **Transpose with `zip(*grid)`:** Summing row and transposed-column maxima is concise, although materializing the transposed tuples can use $O(n^2)$ temporary space.
- **Empty positions:** A zero-height cell contributes nothing to any projection and must not be counted from above.
- **Single tower:** A positive `1 x 1` grid contributes one top square plus its height to each side projection.
- **All-zero grid:** Every maximum and the count of positive cells are zero, so the total projection area is zero.
- **Hidden shorter towers:** A tower below the maximum in its row or column does not increase that side's shadow, but it still contributes one square to the top view when positive.
