## General

In a one-row grid, the two endpoints have degree one. In every grid with at least two rows and columns, the four corners have degree two, while every other vertex has degree at least three. Thus the vertices of minimum degree are exactly the possible row endpoints: two path endpoints in the one-dimensional case or four corners otherwise.

Choose one such vertex and run breadth-first search until reaching another minimum-degree vertex. BFS reaches a nearest endpoint or corner. For a rectangular grid, the nearest other corner is adjacent along one of the rectangle's two side directions, and a shortest path to it is the straight boundary side. In a path, the only other minimum-degree vertex is the opposite endpoint, so the same search recovers the entire one-row layout. Reconstruct the BFS parent path and use it as the first row.

Once a complete boundary row is fixed, the rest is forced. Mark its vertices used. For each vertex of the current row from left to right, select its first unused graph neighbor as the vertex directly below it. Horizontal neighbors in the current row are already used; from the second column onward, the new row's preceding vertex is also already used. Therefore the only unused neighbor is the matching vertex in the next row. Repeat until all `n` vertices have been placed.

The construction preserves every horizontal and vertical edge. A rectangular grid vertex has no other graph neighbors, so it also introduces no adjacency absent from `edges`. This proves the produced matrix satisfies the required if-and-only-if relation.

## Complexity detail

Let $m=\lvert\texttt{edges}\rvert$. Building the adjacency list and the BFS each take $O(n+m)$ time. Row construction examines each vertex and its at-most-four grid neighbors, adding $O(n)$ time. Total time is $O(n+m)$; the adjacency list, BFS state, used set, and output use $O(n+m)$ space.

## Alternatives and edge cases

- **Arbitrary boundary walk:** Choosing any low-degree neighbor can zigzag across a two-row grid and produce a false first row; shortest-path-to-nearest-corner avoids that ambiguity.
- **Try all factor pairs:** Testing candidate dimensions and validating each completed matrix can repeat graph traversals and is unnecessary once a side is recovered from degrees and distances.
- **One-row grid:** Degree-one endpoints identify the path, and the corner BFS returns every vertex as the sole row.
- **Two-row or two-column grid:** All noncorner vertices have degree three, but the nearest-corner shortest path still selects a complete side of length two or the longer boundary direction when appropriate.
- **Square grid:** Two adjacent corners are equally near; either BFS result defines a valid orientation.
- **Multiple valid layouts:** The semantic judge checks the complete adjacency set, so rotations, reflections, and transpositions are accepted.
