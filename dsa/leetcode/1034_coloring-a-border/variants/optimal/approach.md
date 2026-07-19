## General
**Traverse the original component:** Record the starting color before any mutation. Use an explicit stack and a `seen` set to visit exactly the four-directionally connected cells with that color.

**Classify a cell while its neighbors are unchanged:** A visited cell is a border if it lies on a grid edge. It is also a border if any of its four neighbor positions is outside the grid or contains a color different from the original component color. Store border coordinates separately instead of recoloring immediately.

**Recolor after discovery:** Once traversal finishes, change every stored border coordinate to `color`. Delaying mutation prevents the new color from making later component cells appear disconnected or falsely bordered.

The traversal reaches every cell in the starting component and no cell outside it. The neighbor test is exactly the source definition of a component border, so every stored cell must be recolored and every unstored component cell must remain unchanged. Cells outside the component are never added to either collection.

## Complexity detail
Each of the $P$ component cells is pushed once and checks four neighbors, so traversal and recoloring take $O(P)$ time. The `seen` set, stack, and border list each contain at most $P$ coordinates, using $O(P)$ auxiliary space.

## Alternatives and edge cases
- **Recursive depth-first search:** It expresses the same traversal compactly, but a 2500-cell component can exceed Python's recursion limit.
- **Temporary in-place markers:** Negate or otherwise mark component values during traversal, then restore interiors and recolor borders. This can reduce separate visited storage but requires care when the target color equals existing values.
- **Repeated reachability tests:** Determine component membership independently for many cells. This repeats traversal work and can take quadratic time.
- **Single-cell component:** Its neighbors are outside the component, so it is always a border.
- **Whole uniform grid:** Only the outer ring changes; interior cells keep the original color.
- **Disconnected equal colors:** Same-colored cells without a connecting path are not part of the selected component.
- **Unchanged color:** If `color` equals the original color, the returned values remain identical even though the border classification is the same.
