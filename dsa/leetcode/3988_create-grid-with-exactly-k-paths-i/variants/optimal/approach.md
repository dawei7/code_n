## General

Because `k` is at most four, the path count can be created inside a constant-size block at the top-left corner. Every route through that block is then forced into one shared corridor leading to the destination.

**Templates for the four path counts**

For `k = 1`, the block is just `(0, 0)`. For `k = 2`, use a fully open $2 \times 2$ block. For `k = 3`, use a fully open $2 \times 3$ block or its transpose. The number of right/down paths through an open $a \times b$ rectangle is

$$
\binom{a+b-2}{a-1},
$$

so these blocks provide one, two, and three routes respectively.

For `k = 4`, a fully open $2 \times 4$ block or its transpose has four routes. When neither orientation fits but both dimensions are at least three, use a $3 \times 3$ block with its top-right and bottom-left cells blocked. The open square has six routes; blocking those two cells removes exactly the all-right-then-down route and the all-down-then-right route, leaving four.

**A corridor preserves the count**

After opening the chosen block, extend a horizontal corridor from its bottom-right cell to the final column and then a vertical corridor down to `(m - 1, n - 1)`. Leave every other cell blocked. All routes through the block merge at its bottom-right cell, and the corridor offers exactly one continuation, so multiplying by that single continuation preserves the block's path count.

The fit tests also characterize impossibility for the allowed values of `k`. A one-dimensional grid has at most one path. A $2 \times 2$ grid has at most two, and a $2 \times 3$ grid or its transpose has at most three. Every larger shape needed for `k = 4` admits one of the listed templates. Thus returning `[]` only when no template fits is exact, rather than merely a limitation of the construction.

## Complexity detail

Creating the mutable grid and joining its rows both examine all $mn$ cells, so the running time is $O(mn)$. The block and corridor edits add only $O(m+n)$ work. The returned grid and its mutable construction buffer occupy $O(mn)$ space; all other state is constant-size.

The source domain contains only $10 \cdot 10 \cdot 4 = 400$ legal input tuples and at most $100$ output cells. This bounded domain is verified exhaustively instead of using misleading runtime-scaling tiers.

## Alternatives and edge cases

- **Search over obstacle masks:** Enumerating layouts can eventually find a valid grid for these small dimensions, but even a $10 \times 10$ grid has $2^{100}$ masks; the template construction is direct and deterministic.
- **Dynamic programming while designing cells:** Path counts can be propagated through a partially built grid, but choosing obstacles to reach an exact total is more complicated than using the four proven blocks.
- **Single row or column:** Only `k = 1` is possible, and the unique corridor must keep every cell free.
- **The $3 \times 3$ four-path block:** Both corner-adjacent extremes `(0, 2)` and `(2, 0)` must be blocked; leaving either open creates a fifth route.
- **Do not open cells around the corridor:** An extra free neighbor can create another way to enter the corridor and change the path count.
- **Non-unique output:** The judge must validate dimensions, characters, and the exact number of paths rather than compare against one serialized grid.
