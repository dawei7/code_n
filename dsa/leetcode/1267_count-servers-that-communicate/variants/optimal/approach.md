## General
**Count occupancy before classifying servers**

Create one counter per row and one per column. Scan every cell once; whenever `grid[row][col] == 1`, increment both corresponding counters. These counts summarize all possible communication partners without building explicit edges between servers.

**Test the communication condition directly**

Scan the matrix again. A server communicates precisely when its row counter exceeds one or its column counter exceeds one. Count that cell once when either condition holds. The test is sufficient because a count above one guarantees a distinct server on the same line. It is also necessary: if both counts equal one, the current cell is the only server in its row and column, so it has no possible partner.

The logical `or` prevents double-counting a server that communicates along both axes, while servers on an otherwise empty line can still qualify through the other axis.

## Complexity detail
Each of the two scans examines all $V$ cells and performs constant work, for $O(V)$ time. The row and column counters contain $m+n$ integers, giving $O(m+n)$ auxiliary space.

## Alternatives and edge cases
- **Rescan each server's row and column:** It uses no counter arrays but repeats work and can take $O(V(m+n))$ time.
- **Graph traversal:** Connecting servers that share a line and counting non-singleton components is correct, but materializing or exploring those relationships is unnecessary.
- **Union-find:** Rows and columns can be joined through servers, yet the additional structure solves a more general connectivity problem than this direct count requires.
- **Single server:** Its row and column counts are both one, so it is excluded.
- **All-empty grid:** No counters increase and the answer is `0`.
- **Several partners on both axes:** A server still contributes exactly once.
- **Servers with empty cells between them:** Sharing a row or column is sufficient; intervening zeros do not block communication.
