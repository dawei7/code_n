## General

**Treat each layer as an independent cycle.** A layer is the rectangular perimeter at equal distance `p` from all four outer boundaries. Its cells never move into another layer, so every perimeter can be extracted, rotated, and written back separately. There are `min(m,n) // 2` layers because both dimensions are even and every layer has positive height and width.

**Choose one consistent coordinate order.** Helper `rotate(p, k)` collects layer values starting at its top-left corner. It walks the top edge left to right, the right edge top to bottom, the bottom edge right to left, and the left edge bottom to top. This is clockwise order around the rectangle.

Each loop excludes its final corner, which becomes the first cell of the next edge. The top loop excludes top-right, right loop includes top-right but excludes bottom-right, bottom loop includes bottom-right but excludes bottom-left, and left loop includes bottom-left but excludes top-left. Thus every perimeter cell appears exactly once.

**Translate counter-clockwise movement into a list shift.** Along the stored clockwise sequence, the adjacent counter-clockwise position of a value is one index earlier. After one required rotation, old value `nums[1]` moves into coordinate position zero, old `nums[2]` moves into position one, and so on. Therefore a counter-clockwise rotation is a left shift of the stored values.

The expression `nums = nums[k:] + nums[:k]` performs that left shift. Writing the shifted sequence back along the same coordinate order places every original value at its counter-clockwise neighbor.

**Reduce huge rotations modulo perimeter length.** After as many rotations as there are cells in the layer, every value returns to its starting point. `k %= len(nums)` keeps only the effective remainder, making values as large as $10^9$ harmless. Different layers can have different perimeter lengths, so modulo is computed independently inside each helper call.

**Skip unnecessary rewriting.** If the remainder is zero, `rotate` returns immediately. The layer is already correct, and avoiding the four write-back loops saves work. Its extracted `nums` list is still created because the length is needed for modulo.

**Write the shifted sequence back exactly once.** Local variable `k` is reset to zero and reused as an index into the shifted list. The same four edge loops run in the same bounds and order as extraction. Every coordinate receives the corresponding shifted value, with no collision because all original values were copied before any grid cell was overwritten.

**Trace the two-by-two example.** Clockwise extraction of `[[40,10],[30,20]]` is `[40,10,20,30]`: top-left, top-right, bottom-right, bottom-left. Left-shifting by one gives `[10,20,30,40]`. Writing back in that order produces `[[10,20],[40,30]]`, exactly one counter-clockwise layer rotation.

**Why in-place output is safe across layers.** Layers are disjoint coordinate sets. Rotating one modifies no cell that a later inner layer will read. Within one layer, extraction finishes before writing starts, so overwriting cannot corrupt an uncollected source value.

**Why the algorithm is complete.** Every grid cell belongs to exactly one layer because both dimensions are even and there is no unlayered central row or column. Each layer extraction is a bijection between its coordinates and cyclic list positions. The left shift implements $k$ counter-clockwise neighbor moves, and write-back applies that permutation. Processing all layers therefore yields the required whole matrix.

**Input mutation is part of the exact behavior.** The method changes `grid` directly and returns that same matrix object. A caller needing the original grid must pass a deep copy.

## Complexity detail

Let the grid have $m$ rows and $n$ columns. Across all layers, extraction and write-back visit each cell a constant number of times. List slicing and concatenation also process each layer perimeter linearly. Total time is $O(mn)$.

At one time, the helper stores one perimeter list and, during concatenation, a shifted list whose length is that perimeter. The largest outer perimeter has $O(m+n)$ cells, so exact peak auxiliary space is $O(m+n)$. The manifest's $O(mn)$ space is a valid loose upper bound but not tight for this source.

The recursion depth is zero because layers are processed iteratively. Modulo and index arithmetic are constant-time for the bounded dimensions and Python integers.

## Alternatives and edge cases

- **Store coordinates as well as values:** This makes write-back visually direct but uses additional perimeter arrays. The exact source regenerates coordinates with identical loops.
- **Rotate one step `k` times:** Correct but can cost $O(kmn)$ and is impossible for $k$ up to $10^9$. Modulo plus slicing applies the net permutation once.
- **In-place cycle replacement:** Can reduce auxiliary space toward $O(1)$ but is more delicate because cycle gcds and saved values must be handled correctly.
- **Different layer lengths:** Each layer takes its own modulo; using the outer perimeter length for every layer would be wrong.
- **Two-row or two-column layer:** The edge bounds still include every cell once without duplicate corners.
- **Rotation multiple of perimeter:** The helper returns without writing because the layer is unchanged.
- **Even dimensions:** They ensure every cell belongs to a complete perimeter layer. Odd dimensions would leave a central row or column that stays fixed and would need explicit interpretation.
- **Direction trap:** Coordinates are stored clockwise, so counter-clockwise value movement requires a left shift, not a right shift.
- **Input preservation:** The returned grid is the mutated input object, not a separately allocated matrix.
