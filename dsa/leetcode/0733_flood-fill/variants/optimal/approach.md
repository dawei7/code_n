## General

**Flood fill changes one connected component, not every matching pixel**

The starting pixel has an original color `oc = image[sr][sc]`. The fill must recolor exactly the pixels that can be reached from that start by repeatedly moving up, right, down, or left through pixels of color `oc`.

A pixel elsewhere in the image may have the same numeric color yet remain unchanged if no four-directional path of original-color pixels connects it to the start. Diagonal contact alone is not a connection.

The exact solution performs a depth-first search from the starting coordinate. The image itself records which connected pixels have already been visited: as soon as DFS enters one, it changes that pixel to the requested `color`.

**Why the original color must be saved first**

The search decision for a neighbor is whether its value equals the color the component had before filling. Once the first pixel is changed, reading `image[sr][sc]` would no longer reveal that value. Saving it in `oc` before starting preserves the criterion for the entire traversal.

Every recursive call compares possible neighbors with this same `oc`. The target `color` is used only for marking and output.

**Generate the four directions compactly**

The tuple

`dirs = (-1, 0, 1, 0, -1)`

works with adjacent pairs. `pairwise(dirs)` yields

`(-1, 0), (0, 1), (1, 0), (0, -1)`.

These are precisely up, right, down, and left. There are no diagonal pairs. For a current pixel `(i, j)`, adding a pair `(a, b)` produces neighbor `(i + a, j + b)`.

Before reading a neighbor, the solution verifies that its row and column lie inside the image. This prevents negative indices from wrapping around in Python and prevents indices beyond the bottom or right edges.

**Recoloring doubles as the visited marker**

When `dfs(i, j)` begins, it immediately assigns

`image[i][j] = color`.

It then recurses only into neighbors whose current value still equals `oc`. Because a visited pixel now has the new color, it no longer passes that test. No separate `visited` matrix or coordinate set is necessary.

Marking before exploring neighbors is important. If the pixel were marked only after its recursive children returned, two adjacent recursive calls could re-enter one another indefinitely.

**Why equal old and new colors need an early return**

The image-based visited technique works only when recoloring changes the stored value. If `oc == color`, assigning the target color would leave a visited pixel indistinguishable from an unvisited original-color pixel. Adjacent pixels could recurse back and forth forever.

The solution therefore calls DFS only when `oc != color`. When the colors are equal, the desired final image is already the input image, so returning it unchanged is both correct and necessary for safe traversal.

**A connected-component trace**

For

`[[1, 1, 1], [1, 1, 0], [1, 0, 1]]`

starting at `(1, 1)` with target color `2`, DFS changes the center from one to two. It then visits every side-connected one: the left neighbor, cells above, and the connected top row. Each is recolored on entry.

The bottom-right one remains unchanged. Although its value matches the original color, its side neighbors are zero, so no valid original-color path reaches it. The traversal never enters it.

**The traversal invariant**

Whenever DFS is called on `(i, j)`, that pixel belongs to the start’s original-color component and has not previously been processed. The initial call satisfies this because it is the start itself. A recursive call is made only to an in-bounds side neighbor that still equals `oc`, so appending that edge to the path proves the neighbor belongs to the component. Its unchanged value also proves it has not been visited when old and new colors differ.

On entry, DFS marks that pixel and examines all four possible continuation edges. Therefore every processed pixel is valid, and every valid adjacent continuation is eventually processed.

**Why the returned image is correct**

No pixel outside the component is changed because calls follow only side adjacency through `oc` pixels from the start. Conversely, take any pixel inside the component. A finite valid path connects it to the start. DFS examines every edge from each earlier path pixel, so induction along that path shows the target pixel is eventually reached and recolored.

Thus exactly the connected component receives `color`. All other values remain untouched, and returning the mutated `image` gives the required result.

## Complexity detail

Let `m` be the row count and `n` the column count. Every pixel in the filled component is entered at most once because recoloring removes it from future `oc` checks. Each entry examines four neighbors, a constant amount of work.

If the component contains `K` pixels, the traversal costs `O(K)` time. In the worst case the whole image is one component, so the bound is `O(mn)`.

The recursion stack can contain `O(K)` calls in a path-shaped component, hence `O(mn)` auxiliary space in the worst case. No explicit visited matrix is allocated. The image is modified in place and also returned.

In Python, a very long narrow component may approach the interpreter’s recursion limit even though the mathematical space bound is valid. An iterative traversal avoids that implementation limit.

## Alternatives and edge cases

- **Breadth-first search with a queue:** Recolor on enqueue and process neighbors iteratively. It has the same `O(mn)` worst-case time and space and avoids recursion-depth limits.

- **Explicit visited set:** Track coordinates separately instead of using the changed color. This works even when colors match but uses extra storage. The early equality check makes it unnecessary here.

- **Scan every matching pixel globally:** This is incorrect because equal-colored pixels in disconnected components must remain unchanged.

- **Include diagonal neighbors:** This changes the definition of connectivity and would incorrectly fill pixels touching only at corners.

- **Old color equals target color:** Return immediately. The output is already correct, and DFS could not use recoloring as a visited mark.

- **One-pixel image:** If colors differ, the single pixel is recolored; if they match, it is returned unchanged.

- **Start on an image boundary:** Bounds checks simply discard missing neighbors, so no special branch is needed.

- **Cycles in the component:** Recoloring on entry prevents any previously processed pixel from being entered again, even when several paths lead to it.

- **Input mutation:** The method deliberately edits `image` rather than constructing a copy. Callers needing the original image must copy it first.
