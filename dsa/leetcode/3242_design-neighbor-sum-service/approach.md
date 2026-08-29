## General

Each query supplies a tile value rather than its row and column. Searching the whole grid to locate that value on every call would cost $O(n^2)$ per query. Because all values are distinct, initialization can build a direct dictionary from each value to its unique coordinates. Once the coordinates are known, either requested sum examines at most four cells.

The constructor stores the supplied grid reference in `self.grid` and creates `self.d`. While enumerating rows and cells, it assigns `self.d[x] = (i, j)`. Distinctness guarantees that no later cell overwrites the coordinates of the same value. The contract also guarantees every queried value lies in the grid's full value range; combined with the grid containing distinct values in that range, dictionary lookup succeeds.

The two public methods share one helper. `adjacentSum(value)` calls `cal(value, 0)`, while `diagonalSum(value)` calls `cal(value, 1)`. The argument `k` selects one of two compact direction encodings.

For adjacent neighbors, `self.dirs[0]` is the five-number tuple `(-1, 0, 1, 0, -1)`. Applying `pairwise` yields consecutive pairs:

`(-1, 0), (0, 1), (1, 0), (0, -1)`.

These are the top, right, bottom, and left coordinate offsets. The repeated minus one at the end closes the sequence into the left direction without writing four nested tuples.

For diagonal neighbors, `self.dirs[1]` is `(-1, 1, 1, -1, -1)`. Its consecutive pairs are:

`(-1, 1), (1, 1), (1, -1), (-1, -1)`,

representing top-right, bottom-right, bottom-left, and top-left. The order does not affect a sum.

The helper first retrieves `i, j = self.d[value]`. For each selected offset `(a,b)`, it computes candidate coordinates `x = i + a` and `y = j + b`. A candidate is included only when `0 <= x < len(self.grid)` and `0 <= y < len(self.grid[0])`. These bounds discard directions that leave the grid at an edge or corner. Every valid neighbor's value is added once to `s`, which is returned.

For the center value four in the three-by-three example, dictionary lookup gives `(1,1)`. The cardinal offsets reach one, five, seven, and three, summing to sixteen. The diagonal offsets reach two, eight, six, and zero, also summing to sixteen. For corner value eight, only diagonal offset `(-1,-1)` stays in bounds, reaching four.

**What the source actually precomputes.** The variant summary says that both neighbor sums are precomputed for every value. The exact source does not do this. It precomputes only coordinates. Every public query calls `cal` and reads up to four grid cells at that moment. Because four is a fixed constant, each query is still $O(1)$, and the total complexity claim remains appropriate, but the data flow is position lookup plus on-demand summation rather than sum lookup.

This distinction has another consequence: `self.grid` is the original mutable list reference, not a copy. If external code changed a grid value after construction, `cal` would sum the changed grid contents while `self.d` would still describe the original value positions. The LeetCode design contract performs only neighbor-sum calls after construction and supplies no grid-update operation, so this inconsistency cannot arise in legal use.

**Why four directions are enough.** Adjacent neighbors share one side, so their row and column differences are `(|\Delta r|,|\Delta c|) = (1,0)` or `(0,1)`. Diagonal neighbors share a corner and have differences `(1,1)`. The direction tuples enumerate exactly these possibilities, with no center cell and no farther cell.

The dictionary turns value-based service requests into coordinate-based constant work. Bounds checks then make the same helper valid for interior, edge, and corner tiles without separate case branches.

## Complexity detail

Let the grid dimensions be $n\times n$ and let $q$ be the number of method calls after construction. Initialization visits all $n^2$ cells once and performs expected-constant-time dictionary assignments, taking expected $O(n^2)$ time.

Each `adjacentSum` or `diagonalSum` call performs one expected $O(1)$ dictionary lookup and exactly four offset iterations, so each call is expected $O(1)$ and all calls take $O(q)$. The full object lifecycle therefore costs expected $O(n^2+q)$ time.

The coordinate dictionary stores $n^2$ entries, giving $O(n^2)$ auxiliary space. The object also retains a reference to the input grid; it does not copy another $n^2$ cells. Direction data and query-local variables use $O(1)$ space.

Python dictionary bounds are expected rather than adversarial worst-case guarantees. Values are small integers, which are well suited to this use.

## Alternatives and edge cases

- **Precompute both sums:** During construction, compute an adjacent and diagonal sum for every value and store them in two arrays or maps. Initialization remains $O(n^2)$ and queries become direct lookups, but on-demand calculation is already constant-time and stores less per value.
- **Value-to-position array:** Since values cover `0` through `n^2 - 1` exactly, a list indexed by value could replace the dictionary. It has deterministic $O(1)$ lookup and the same $O(n^2)$ space.
- **Search for the value on every call:** This avoids the coordinate map but costs $O(n^2)$ per query, which is unnecessary when up to $2n^2$ calls may occur.
- **Write eight explicit branches:** Separate neighbor checks work but duplicate bounds logic. Direction iteration is shorter and less error-prone once the offsets are understood.
- **Corner tile:** It has two adjacent neighbors and one diagonal neighbor. The other offsets fail the bounds checks and contribute nothing.
- **Non-corner edge tile:** It has three adjacent neighbors and two diagonal neighbors.
- **Interior tile:** All four offsets of either selected direction family remain valid.
- **Value zero:** It is a legitimate tile value, not a sentinel. Dictionary membership and summation handle it normally.
- **Distinctness requirement:** If duplicate values were allowed, later assignments to `self.d[x]` would overwrite earlier coordinates, making value-only queries ambiguous. The problem explicitly rules this out.
- **Missing `pairwise` import:** The source assumes `pairwise` is available from `itertools` in the execution harness or imports. In an ordinary standalone module, `from itertools import pairwise` is required; otherwise calls to `cal` raise `NameError`.
- **External grid mutation:** Legal operations never change the grid. If a caller mutates it anyway, the stored coordinate map is not rebuilt, so behavior no longer represents a coherent initialized service state.
