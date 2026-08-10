## General

**Reverse deletions into additions**

Disjoint-set union efficiently merges connected components, but it does not efficiently split a component when a brick is removed.

Process the hits backward. In reverse time, each meaningful hit restores one brick. Components only merge, which is exactly the operation union-find supports.

The forward question “how many stable bricks lose their roof connection after this deletion?” becomes the reverse question “how many bricks gain a roof connection when this brick is restored?”

**Create the grid after all requested hits**

The method deep-copies `grid` into `g` so the original remains available for deciding whether a hit location originally held a brick.

For every hit `(i,j)`, it sets:

`g[i][j] = 0`.

Hits are unique, so each requested position is removed at most once.

This `g` is the board on which reverse processing begins. It may contain brick components not connected to the top. Those components are deliberately retained in union-find as unstable groups; if a later restoration connects them to the roof, their entire size becomes relevant.

**Represent the roof with a virtual node**

Flatten cell `(i,j)` to index:

`i * n + j`.

Indices zero through `m*n-1` represent grid cells. Extra index `m*n` is a virtual roof.

Every brick in row zero is united with this virtual node. A brick is stable exactly when its flattened index belongs to the roof node's component.

The roof component's stored size includes the virtual node itself. Differences of roof sizes cancel that constant, so no special subtraction is needed until counting the restored brick.

**Maintain component representatives and sizes**

Array `p` stores parent links. Function `find` follows links to a representative and applies path compression on return.

Array `size` is meaningful at representatives. To unite roots `pa` and `pb`, the code attaches `pa` under `pb` and adds:

`size[pb] += size[pa]`.

If both inputs already have the same representative, no size changes.

The parent choice is arbitrary for connectivity. The exact source does not choose by rank or component size, a detail that matters for the strongest theoretical complexity claim but not correctness.

**Build connectivity in the post-hit grid**

First, every surviving top-row brick is united with the roof.

For later rows, each present brick checks only its upper and left neighbors. This is sufficient because every four-directional adjacency is encountered once:

- a vertical pair is handled by its lower cell checking upward;
- a horizontal pair is handled by its right cell checking leftward.

Checking down and right as well would repeat unions without changing components.

Top-row bricks do not need explicit horizontal unions. They are already connected through the common virtual roof, and stability cares only about roof-component membership.

**Skip reverse hits that originally targeted empty space**

If `grid[i][j] == 0`, the forward hit erased no brick and caused no change. Reverse processing must likewise restore nothing.

The method appends zero and continues. Looking at the original grid rather than `g` distinguishes a genuinely removed brick from an originally empty position.

**Restore a real brick**

For an original brick, set `g[i][j] = 1`. At this moment the DSU does not yet contain any connections for that cell, so setting the grid flag alone does not alter roof size.

The method records:

`prev = size[find(m * n)]`.

If the brick is in row zero, it unites it with the roof. It then checks all four neighboring coordinates and unites the restored brick with every present neighbor in `g`.

After these merges:

`curr = size[find(m * n)]`

is the new roof-component size.

**Convert the roof-size increase into fallen bricks**

If restoration connects the brick and some previously floating components to the roof, `curr - prev` counts every newly roof-connected real brick, including the brick just restored.

In forward time, the hit brick is erased directly; it is not counted among bricks that fall afterward. Therefore subtract one:

`curr - prev - 1`.

If the restored brick fails to connect to the roof, `curr == prev` and this expression is negative one. `max(0, ...)` correctly reports zero falling bricks.

If it connects only itself, the difference is one and the result is also zero.

**Why floating components in `g` are useful**

After all hits are removed, `g` can contain bricks outside the roof component. They may represent bricks that would already have fallen during forward simulation.

Deleting them physically is unnecessary and would lose component-size information. They remain inactive with respect to stability until some reverse restoration connects their component to the roof.

At that moment, the entire component becomes newly stable in reverse. Those are exactly the bricks that lost stability together at the corresponding forward hit.

**Trace the first example**

After removing hit `(1,0)`, the remaining bottom bricks at columns one and two form a two-brick component disconnected from the top brick.

Reverse restoration adds brick `(1,0)`. It connects upward to the roof-stable top brick and sideways to the two-brick floating component.

The roof size grows by three real bricks: the restored brick plus the two formerly floating bricks. Subtracting one reports two, matching the forward fall count.

**Why answers are reversed at the end**

Reverse processing considers the last forward hit first, so values are appended in reverse chronological order.

`ans[::-1]` restores the original hit order required by the return contract.


At every reverse step, the DSU represents all brick adjacencies in the current restored grid, and its roof component is exactly the set of stable bricks.

Restoring a hit can only merge components. The increase in roof-component size identifies exactly those bricks whose stability depends on that restored brick. Reversing time, removing the same brick disconnects those other bricks and makes them fall. Excluding the erased brick itself gives the required count.

Empty hits produce no state change in either direction. Induction over reversed hits proves every appended value corresponds to its forward event, and reversing the result places them correctly.

## Complexity detail

Let $N = m\cdot n$ be the number of cells and $H$ the number of hits. Copying and scanning the grid costs $O(N)$, and each brick/hit causes only a constant number of union/find operations.

The manifest states $O((N+H)\alpha(N))$, the standard bound when path compression is paired with union by rank or size. The exact source applies path compression but always attaches `pa` under `pb` without rank/size selection. A safe bound for path compression alone is $O((N+H)\log N)$ amortized in this workload model; the inverse-Ackermann guarantee is not justified by the displayed union rule alone.

The copied grid, parent array, size array, and DSU representation use $O(N)$ space. The answer uses $O(H)$ required output space; excluding output, auxiliary space is $O(N)$.

## Alternatives and edge cases

- **Add union by size or rank:** Choose the smaller/ranked root as the child while updating sizes. Together with path compression, this supports the manifest's inverse-Ackermann bound.

- **Forward flood fill after every hit:** Recomputing roof reachability costs up to $O(HN)$.

- **Delete from DSU directly:** Standard union-find cannot split components efficiently, which motivates reverse time.

- **Hit on original zero:** Append zero and do not restore a brick.

- **Top-row restoration:** Unite directly with the virtual roof.

- **Restoration stays unstable:** Roof size does not grow, and the clamped result is zero.

- **Restoration connects several components:** Union sizes make their complete newly stable populations count at once.

- **Subtract one:** The restored/re-erased brick itself is not a falling brick.

- **Top-row horizontal neighbors:** Direct unions are unnecessary during initialization because all present top bricks share the roof node.
