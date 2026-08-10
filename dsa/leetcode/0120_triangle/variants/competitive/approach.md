## General

The competitive source moves from top to bottom and keeps only the minimum path sums for the most recently completed row. `cur[j]` represents the smallest sum from the triangle's top to position `j` in that row.

For the next row, each position chooses the better of its valid parents. A positive-infinity sentinel after the real row simplifies the right-edge calculation.

**Initialization**

If `triangle` is empty, the method returns zero. The stated constraints guarantee at least one row, but this branch gives the source a sensible extended behavior.

For a nonempty triangle, `cur = triangle[0] + [float("inf")]`. Because the first row contains one value, `cur[0]` is the cost of the only path to the top. The trailing infinity represents a nonexistent parent just beyond the row's right edge.

The concatenation creates a new list, so the input's first row is not modified.

**The top-down state**

Before processing row `i`, real entries `cur[0]` through `cur[i - 1]` are minimum sums from the top to each cell in row `i - 1`. `cur[i]` is infinity.

The next row has `i + 1` cells. The source constructs a fresh list named `next`, then appends a new infinity sentinel after completing the row.

Although `next` shadows Python's built-in iterator function within the method, the built-in is not needed and correctness is unaffected.

**Handling the left edge**

Cell `(i, 0)` has only one valid parent: `(i - 1, 0)`. The source handles it before the general loop:

`triangle[i][0] + cur[0]`.

There is no attempt to read `cur[-1]`, which in Python would incorrectly refer to the sentinel at the list's end rather than represent an absent parent.

**Interior and right-edge positions**

For `j` from one through `i`, the two conceptual parents are prior-row positions `j - 1` and `j`. The update appends:

`triangle[i][j] + min(cur[j - 1], cur[j])`.

For an interior position, both values are finite, so the smaller complete path is chosen.

At the new right edge `j = i`, prior row position `i` does not exist. Its stored sentinel is infinity, so `min(cur[i - 1], inf)` selects the sole real parent. The same formula therefore handles every position except the left edge.

**Why infinity is safe**

Any legal path sum is finite. Comparing it with positive infinity always selects the legal parent, even when the legal sum is very large, positive, or negative.

The sentinel is never returned as a candidate cell cost. After each row is built, `cur = next + [float("inf")]` restores exactly one sentinel after its real entries.

**Why each row contains exact minimum sums**

The top row state is exact because there is one path consisting of its sole cell.

Assume `cur` holds exact minimum costs to every parent in row `i - 1`. Every path reaching `(i, j)` must arrive from `(i - 1, j - 1)` or `(i - 1, j)`, subject to edge existence. Taking the minimum valid parent cost and adding the current cell gives the exact best path to `(i, j)`.

The explicit left-edge rule and infinity-protected general rule cover all positions. Thus the newly built row satisfies the state invariant, which holds through the bottom row.

Every complete top-to-bottom path ends at some bottom-row cell. Returning the minimum finite value in `cur` therefore selects the best complete path.

**Why `reduce(min, cur)` still works with the sentinel**

The final `cur` contains all real bottom-row costs followed by infinity. `reduce(min, cur)` compares them all. Infinity cannot beat a real finite sum, so the result is the minimum bottom cost.

Python's ordinary `min(cur)` would express the same operation. The source imports `reduce` from `functools` and uses it correctly.

**Tracing the main example**

The state starts as `[2, inf]`.

Row `[3, 4]` becomes `[5, 6, inf]`: the left cell comes from two, and the right-edge formula chooses two over infinity.

Row `[6, 5, 7]` becomes `[11, 10, 13, inf]`. The final row becomes `[15, 11, 18, 16, inf]`. Reducing by minimum returns eleven, corresponding to two, three, five, and one.

The source computes path totals rather than retaining paths, which is sufficient because only the smallest sum is requested.

## Complexity detail

Let $N$ be the total number of cells and $r$ the row count. Every cell is processed once with constant work, so time is $O(N)$, equivalent to $O(r^2)$ for a proper triangle.

At row `i`, old `cur`, the growing `next`, and the concatenated replacement may briefly coexist. Each has length $O(r)$, and a constant number of linear-sized lists remains $O(r)$ peak auxiliary space.

The input is not mutated. The final answer is one integer and uses $O(1)$ output space. The manifest's $O(r)$ space accurately describes this rolling-row implementation.

Creating `next + [inf]` copies the completed row once per level. The total copying across all rows is still $O(N)$ and does not change the time bound.

## Alternatives and edge cases

- **Bottom-up rolling row:** Start from the bottom and replace each parent cost with its value plus the smaller of two children. Edge handling is even simpler because every non-bottom cell has two children.
- **In-place bottom-up update:** Store continuation costs directly in `triangle`, reducing extra space to $O(1)$ while mutating input.
- **Full DP table:** Easy to inspect but uses $O(N)$ auxiliary storage unnecessarily.
- **Memoized recursion:** Natural minimum-from-cell formulation with $O(N)$ cached states and $O(r)$ stack.
- **Left sentinel as well:** Pad both sides with infinity and use a uniform parent formula for every cell, at the cost of adjusted indexing.
- **Empty triangle outside constraints:** Returns zero before indexing the first row.
- **Single cell:** `cur` contains the value and infinity; reduction returns the value.
- **Negative values:** Infinity remains safely larger, and complete path sums are compared exactly.
- **Left edge:** Must use only the same-column parent.
- **Right edge:** The infinity sentinel suppresses the nonexistent same-column parent.
- **Interior cells:** Choose between two complete parent path costs, not merely the two immediate parent values.
- **Input preservation:** Fresh `next` rows leave `triangle` unchanged.
- **Shadowing `next`:** Harmless here but renaming it `next_row` would preserve access to Python's built-in.
- **Sentinel placement:** Exactly one infinity must follow the real row so `cur[i]` is safe at the next right edge.
- **Final reduction:** Including infinity cannot change the minimum because the bottom row is nonempty.
