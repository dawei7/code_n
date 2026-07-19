## General
**Bound the possible distance:** The farthest two cells in a `rows` by `cols` matrix differ by at most `rows - 1` vertically and `cols - 1` horizontally. Every center-to-cell distance is therefore an integer from $0$ through `rows + cols - 2`.

**Group cells by exact distance:** Allocate one bucket for each possible distance. Visit every coordinate `[row, col]`, compute `distance = abs(row - r_center) + abs(col - c_center)`, and append the coordinate to that bucket.

**Emit buckets in increasing order:** Concatenating bucket zero, bucket one, and so on includes every cell exactly once. All coordinates in an earlier bucket have a smaller distance than all coordinates in a later bucket; ties remain unrestricted, so the result satisfies the complete ordering contract.

## Complexity detail
Computing and storing a bucket for each of the $M$ cells takes $O(M)$ time. The number of buckets is `rows + cols - 1`, which is $O(M)$ for positive dimensions, and flattening them visits $M$ entries. The buckets and returned coordinates use $O(M)$ space.

## Alternatives and edge cases
- **Comparison sorting:** Enumerate all cells and sort by Manhattan distance. This is concise but takes $O(M\log M)$ time.
- **Breadth-first expansion:** Start from the center and visit unvisited orthogonal neighbors by layers. It is also $O(M)$ but needs a visited structure and queue.
- **Diamond-ring generation:** Generate only in-bounds points at each exact radius. It avoids sorting but requires careful handling of corners and duplicate axis points.
- **Single cell:** A `1 x 1` matrix returns only the center at distance zero.
- **Equal distances:** Their relative order is deliberately unspecified and must not be overconstrained.
- **Edge or corner center:** Buckets naturally omit coordinates outside the matrix without special distance rules.
