## General

**Color the board by coordinate parity.**  On a checkerboard, two cells have the same color exactly when the sums of their coordinates have the same parity. In zero-based coordinates:

- a cell `[x, y]` belongs to one color when `(x + y) % 2 == 0`;
- it belongs to the other color when `(x + y) % 2 == 1`.

The names “black” and “white” are unimportant. Only the two parity classes matter, and adding the coordinates gives a simple numerical way to identify them.

**Every knight move changes the color.**  A knight changes one coordinate by `2` and the other by `1`. Signs do not affect parity, so the change in the coordinate sum is one of `3`, `1`, `-1`, or `-3`. Every one of these numbers is odd.

Adding an odd number flips parity:

- even becomes odd;
- odd becomes even.

Therefore, after one knight move the piece is on the opposite color. After two moves it is back on its starting color class. After three it is on the opposite class again, and so on. More generally:

- every even-length knight route ends on the same color as it started;
- every odd-length knight route ends on the opposite color.

This immediately proves that different-colored endpoints cannot have an even-length route. No choice of moves can evade the color flip because it happens on every individual move.

**Why matching colors are also sufficient on an 8 by 8 board.**  A parity argument alone gives a necessary condition, but one more board property is needed to conclude that it is sufficient: the knight-move graph of a standard `8 \times 8` chessboard is connected.

Think of each square as a graph vertex and each legal knight move as an edge. Connectivity means that some knight route exists between every pair of squares. Corners and edge squares are not isolated: for example, a corner has legal moves into the board, and those inner squares connect through the central region to the rest of the board. Repeating this across the symmetric edges and corners covers all `64` cells. This is a fixed property of the standard chessboard; the algorithm is not assuming the same fact for an arbitrary tiny or irregular board.

Now suppose `start` and `target` have the same color. Connectivity guarantees at least one route between them. Every route between same-colored vertices must have even length because every edge flips color. Thus an even route exists.

Suppose instead that the endpoints have different colors. Connectivity still gives routes, but every such route must have odd length. An even route is impossible.

So the existence question is equivalent to one comparison:

$$
(\texttt{start}[0]+\texttt{start}[1]) \bmod 2
=
(\texttt{target}[0]+\texttt{target}[1]) \bmod 2.
$$

That equation is precisely what the source returns.

**The method does not need the route or the shortest distance.**  The problem asks whether the knight can use an even number of moves, not how few moves are required and not which squares should be visited. Once endpoint colors determine the parity of every possible route, constructing a route would provide no additional information needed by the return value.

For the first example, `start = [1, 1]` has coordinate sum `2` and `target = [2, 2]` has coordinate sum `4`. Both are even, so an even route exists. The statement exhibits one with four moves, but the formula needs only the two sums.

For the second example, `start = [4, 5]` has sum `9`, which is odd, while `target = [6, 6]` has sum `12`, which is even. The colors differ, so every possible route has odd length. The answer is therefore `false`.

**The zero-move case fits naturally.**  If `start == target`, both coordinate sums are identical. The source returns `true`. This is correct because remaining on the starting square uses zero moves, and zero is even. There is no need for a special equality branch.

Another equivalent test would be

$$
\bigl((\texttt{target}[0]-\texttt{start}[0])
(\texttt{target}[1]-\texttt{start}[1])\bigr) \bmod 2 = 0,
$$

because subtracting the two coordinate sums tells whether their parities agree. Comparing the two endpoint sums directly is clearer and avoids reasoning about the signs of coordinate differences.

## Complexity detail

The source reads four coordinates, performs two additions, two remainder operations, and one equality comparison. The amount of work does not depend on the positions or on the number of possible routes.

- Time complexity is `O(1)`.
- Auxiliary space complexity is `O(1)`.

The board itself has a fixed `64` cells, but the solution does not allocate or traverse even that fixed graph. The result comes directly from the invariant preserved across pairs of moves.

## Alternatives and edge cases

- **Breadth-first search with move parity:** A BFS over states `(x, y, parity)` can answer the question and is small on an `8 \times 8` board. It is unnecessary because the checkerboard invariant reduces the answer to constant-time arithmetic.
- **Ordinary shortest-path BFS:** Computing only the shortest distance would be more information than needed. The color classes already determine whether every route length is even or odd.
- **Searching for one explicit route:** A found route demonstrates one answer but requires predecessor or queue state. The endpoint parity proves the answer for all routes at once.
- **Manhattan or Euclidean distance:** These distances do not determine knight reachability parity. Knight movement is governed by the `(2,1)` displacement and its resulting color flip.
- **Start equals target:** Zero moves are allowed by “can move ... in an even number of moves.” Since zero is even, the method correctly returns `true`.
- **One legal knight move apart:** A single move always changes color, so the method returns `false` for even-move reachability. Any route between those opposite colors must have odd length.
- **Same color but not directly reachable:** Direct reachability is irrelevant. Connectivity supplies some route, and matching endpoint colors force that route's length to be even.
- **Different colors with a long detour:** Adding detours cannot change the required parity between the two color classes. Every additional closed detour in this bipartite graph has even length.
- **Board boundaries:** The sufficiency argument uses the connected standard `8 \times 8` knight graph. On a smaller or obstructed board, matching colors might not be sufficient because the graph could be disconnected.
- **Coordinate convention:** Whether `x` is viewed as a row or a column does not matter. A knight changes one coordinate by `2` and the other by `1` in either convention.
- **Maximum coordinate values:** Coordinates `0` and `7` behave exactly like interior coordinates for the parity test. Boundaries affect which particular moves are legal, but not the color-flip rule.
- **Boolean result:** The equality comparison already produces Python's `True` or `False` value, so no conditional statement or conversion is needed.
