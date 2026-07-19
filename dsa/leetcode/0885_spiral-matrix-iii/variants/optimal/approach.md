## General
**Generate the spiral on the infinite lattice**

A clockwise spiral starting east travels one step east, one south, two west, two north, three east, three south, and so on. Keep the current coordinate, cycle through the directions east, south, west, and north, and increase the segment length after every two directions. This movement rule is independent of the finite grid boundary.

**Record only positions inside the rectangle**

The starting cell is valid and enters the result first. After every subsequent unit step, test whether `0 <= row < rows` and `0 <= column < cols`; append the coordinate only when both inequalities hold. Stop immediately once the result contains `rows * cols` coordinates.

The direction and segment-length schedule traces consecutive expanding square rings without revisiting a lattice point. Every grid cell lies within some finite ring around the start, so the walk eventually reaches it even if intervening portions are outside the rectangle. Filtering preserves the spiral's visit order, and stopping after the grid's full number of distinct cells proves that the result is complete.

## Complexity detail
The farthest grid corner is at coordinate distance $O(m)$ from the start. Reaching the enclosing spiral ring takes $O(m^2)$ unit steps. The returned list contains exactly `rows * cols` coordinate pairs and therefore uses $O(\texttt{rows} \cdot \texttt{cols})$ space; apart from that required output, the simulation uses $O(1)$ space.

## Alternatives and edge cases
- **Turn at grid boundaries:** This ordinary matrix-spiral rule is incorrect because the required path continues outside the rectangle before its scheduled turn.
- **Construct each square ring by its four sides:** Ring endpoints can be generated directly with the same $O(m^2)$ bound, but careful corner handling is needed to preserve the exact order.
- **Track visited coordinates:** The infinite spiral never revisits a lattice position, so a visited set is unnecessary; a list-membership check can make the implementation quadratic in the output size.
- **One-cell grid:** Return the starting coordinate immediately without taking a step.
- **Single row or column:** Most spiral steps are outside the grid, but later re-entry still produces every cell in the required order.
- **Start near an edge:** Do not clamp coordinates or skip movement; update the full outside position on every unit step.
- **Completion condition:** Count recorded in-bounds cells rather than spiral rings, since the final cell may be reached partway through a segment.
