## General

**Count only blocks that a black cell can affect**

An `m` by `n` grid can be enormous, with up to about `10^10` cells, while the input contains at most `10^4` black coordinates. Enumerating every `2 x 2` block would ignore this sparsity and is infeasible.

There are exactly

$$
(m - 1)(n - 1)
$$

possible blocks because a top-left row can range from zero through `m - 2` and a top-left column from zero through `n - 2`. Most of these blocks contain no black cell. The exact solution counts the comparatively few blocks touched by at least one black coordinate and derives the untouched count by subtraction.

**A cell belongs to at most four blocks**

Suppose a black cell is at `(x, y)`. In a `2 x 2` block containing it, that cell can occupy one of four roles:

- top-left, making the block's top-left coordinate `(x, y)`;
- top-right, making the block's top-left coordinate `(x, y - 1)`;
- bottom-right, making the block's top-left coordinate `(x - 1, y - 1)`;
- bottom-left, making the block's top-left coordinate `(x - 1, y)`.

The exact code generates these four offsets compactly with

`pairwise((0, 0, -1, -1, 0))`.

Consecutive pairs from that sequence are `(0, 0)`, `(0, -1)`, `(-1, -1)`, and `(-1, 0)`. Adding each pair to `(x, y)` yields the four candidate top-left coordinates above.

**Discard candidates outside the block grid**

Not every candidate is real. A black cell on the top row cannot be a bottom cell of a block above the grid, and a cell on the far-right column cannot be a left cell of a block extending past the grid.

The condition

`0 <= i < m - 1 and 0 <= j < n - 1`

tests whether `(i, j)` is a legal block top-left coordinate. Only legal candidates are entered in the counter.

**Use a counter keyed by block position**

`cnt[(i, j)] += 1` records one black cell inside block `(i, j)`. Because input coordinates are pairwise distinct, the same physical black cell is processed once and contributes at most once to any particular block. After all coordinates have been processed, each counter value is exactly the number of black cells in that block, from one through four.

Blocks with zero black cells never appear in `cnt`. This omission is intentional: there may be billions of them, and their total can be computed without individual entries.

**Turn block counts into the five answer buckets**

The answer array has indices zero through four. For every value `x` in `cnt.values()`, the code executes `ans[x] += 1`. In other words, a touched block containing `x` black cells contributes one to the bucket for exactly `x`.

The number of touched blocks is `len(cnt.values())`, equivalently `len(cnt)`. Every other possible block has zero black cells. Therefore:

`ans[0] = (m - 1) * (n - 1) - len(cnt.values())`.

This subtraction is the step that makes the algorithm depend on the number of black coordinates rather than the grid area.

**A boundary walkthrough**

Take a `3 x 3` grid with one black cell at `(0, 0)`. The grid has four blocks total. The four candidate top-left coordinates generated for this cell are `(0, 0)`, `(0, -1)`, `(-1, -1)`, and `(-1, 0)`. Only `(0, 0)` passes the boundary test, so the counter contains one block with value one.

The bucket pass sets `ans[1] = 1`. There is one touched block, so `ans[0] = 4 - 1 = 3`. Other buckets remain zero, producing `[3, 1, 0, 0, 0]`.

For an interior black cell, all four candidates are legal and four counters are incremented. If neighboring black cells share a block, they update the same key, increasing its value rather than creating duplicate block entries.

**Why the counts are exact**

Every increment corresponds to a legal `2 x 2` block that contains the processed black cell, because the four offsets enumerate its only possible roles and the boundary check validates the block. Conversely, if a legal block contains a black cell, that cell occupies exactly one of those four roles, so processing it generates that block's top-left key and increments it. Thus each counter value equals the exact number of black cells in its block.

The bucket loop classifies every touched block once. Blocks absent from the counter contain no black coordinate by the converse argument, so subtracting touched keys from the total gives exactly the zero-black count. All possible blocks are thereby classified into one and only one of the five buckets.

## Complexity detail

Let `k` be `coordinates.length`. Each black coordinate generates exactly four candidates and performs a constant amount of boundary checking and expected-time hash-counter work. This costs `O(k)` expected time. The final loop visits at most four distinct blocks per coordinate, so it also costs `O(k)`. Computing the zero bucket is constant time. Total expected time is `O(k)`, independent of `mn`.

The counter has at most `4k` keys, so auxiliary space is `O(k)`. The five-element answer uses `O(1)` space. Python integers can represent the potentially large product `(m - 1)(n - 1)` without overflow.

Hash-map operations provide expected constant-time behavior. Even though many cells can touch the same block, merging them under one key only reduces storage.

## Alternatives and edge cases

- **Enumerate every block:** Inspecting four cells for all `(m - 1)(n - 1)` blocks costs `O(mn)` and is impossible at the largest dimensions.
- **Materialize the whole grid:** A Boolean `m x n` matrix also costs `O(mn)` space despite the sparse black input.
- **Store black cells and query neighboring blocks:** One could build a black-coordinate set and inspect candidate blocks, but care is needed to deduplicate blocks. The counter accumulates and deduplicates in one structure.
- **No black coordinates:** The counter remains empty, all blocks belong to bucket zero, and the answer is `[(m - 1)(n - 1), 0, 0, 0, 0]`.
- **Corner black cell:** It belongs to exactly one block, and three generated candidates fail the boundary check.
- **Edge but non-corner cell:** It belongs to two blocks; the same general candidate filter handles this.
- **Interior black cell:** It belongs to four blocks.
- **Fully black block:** Four distinct input cells increment the same key, placing that block in `ans[4]`.
- **Shared block:** Neighboring black cells update one counter key rather than being counted as separate blocks.
- **Distinct-coordinate guarantee:** It prevents one black cell from incrementing the same block twice through duplicate input rows.
- **Minimum `2 x 2` grid:** There is exactly one possible block, and the counter value or untouched subtraction classifies it.
- **Huge grid with sparse coordinates:** Only touched keys are stored; the large zero count is represented by one integer.
