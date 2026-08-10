## General

**Read each zigzag row directly from the original indices**

Instead of simulating the moving row pointer, this implementation discovers the repeating index pattern and emits characters in the final row-by-row order.

For `numRows = R > 1`, a complete trip from the top row down to the bottom and back toward the top consumes

$$
C = 2R - 2
$$

characters. The code names this cycle length `step`:

```python
step = 2 * numRows - 2
```

For `R = 4`, the row sequence over one cycle is

```text
0, 1, 2, 3, 2, 1
```

and its length is `6`. The next character returns to row `0` and begins another cycle. Because this pattern repeats, characters in the same vertical position of a row are separated by exactly `step` input indices.

**Why one row is a special case**

When `numRows == 1`, the zigzag does not move and the answer is `s`. The cycle formula would give `step = 0`, which cannot be used as the step of Python's `range`. Returning immediately is therefore necessary for both correctness and valid iteration.

**The vertical index in every cycle**

For a fixed row `i`, the loop

```python
for j in range(i, len(s), step):
```

visits indices

$$
i,\; i+C,\; i+2C,\; \ldots
$$

These are the characters encountered while the zigzag moves downward through row `i` in successive cycles. The implementation appends `s[j]` first because that vertical character appears first in the row within each cycle.

The top row and bottom row each occur only once per complete cycle. For them, these `j` indices are the entire row.

**Interior rows have a second diagonal character**

Rows satisfying

```python
0 < i < numRows - 1
```

are visited twice per cycle: once while moving downward and once while moving upward. Starting from vertical index `j`, the upward visit occurs at

$$
j + C - 2i.
$$

To see why, consider a cycle that starts at top-row index `qC`.

- The downward occurrence in row `i` is at `qC + i`, which is `j`.
- The upward occurrence in the same row is at `qC + C - i`.
- Their difference is `(qC + C - i) - (qC + i) = C - 2i`.

That gives the exact expression in the code:

```python
j + step - 2 * i
```

The diagonal index is appended only when it remains inside `s`. A final cycle may be incomplete, so this bounds check prevents reading past the string.

**Why vertical then diagonal is the right row order**

Within an interior row and one cycle, the downward character appears in an earlier conceptual column than the upward diagonal character. The next cycle's downward character appears later still. The loop therefore emits

```text
vertical(q), diagonal(q), vertical(q+1), diagonal(q+1), ...
```

which is exactly the left-to-right order of that row in the written zigzag.

Processing `i` from `0` to `numRows - 1` then places complete rows in top-to-bottom order, matching the required readout.

**Walk through `numRows = 4`**

For `s = "PAYPALISHIRING"`, `step = 6`.

- Row `0`: vertical indices `0, 6, 12` give `P`, `I`, `N`.
- Row `1`: vertical indices `1, 7, 13` give `A`, `S`, `G`; the diagonal offset is `6 - 2 = 4`, giving indices `5, 11` and characters `L`, `I`. Careful ordering is per cycle: index `1` (`A`), diagonal index `5` (`L`), index `7` (`S`), diagonal index `11` (`I`), index `13` (`G`), producing `"ALSIG"`.
- Row `2`: the diagonal offset is `6 - 4 = 2`. Indices appear as `2, 4, 8, 10, 14`, producing `"YAHR"` for the in-range positions of this input.
- Row `3`: vertical indices `3, 9` produce `"PI"`.

Together the rows form `"PINALSIGYAHRPI"`.

The initial shorthand list of vertical characters for row `1` is not itself the row output; each cycle's diagonal character must be inserted immediately after its vertical partner. The nested-loop order performs that interleaving correctly.

**Why every input index is emitted exactly once**

Within one cycle, the vertical positions are row offsets `0` through `R - 1`. The upward diagonal positions correspond to offsets `R` through `C - 1` and map back to interior rows. The top and bottom rows have no separate diagonal occurrence, which is why the condition excludes them.

These positions are disjoint and cover all `C` offsets of a full cycle. Adding multiples of `C` covers successive cycles without overlap. The bounds check keeps only positions belonging to the possibly partial last cycle. Consequently every index from `0` through `len(s) - 1` contributes exactly one output character.

Since row loops are outermost, the emitted sequence is the row-major reading of the same zigzag arrangement.

## Complexity detail

Let $n$ be `len(s)` and $R$ be `numRows`.

- **Index-traversal time: $O(n+R)$.** The outer loop considers all $R$ rows. Across its inner loops, each input index is selected exactly once as either a vertical or diagonal position, so there are $n$ append operations. When $R \le n$, this simplifies to $O(n)$. With the permitted case $R > n$, empty row iterations add an explicit $O(R)$ term.
- **Output and auxiliary space: $O(n)$.** The variable `zigzag` holds the returned $n$-character string. Apart from that output, the method keeps only indices and `step`, which is $O(1)$ auxiliary state. The manifest counts the result and records $O(n)$ space; the source comment's $O(1)$ follows the convention of excluding output.

The code uses repeated `zigzag += character` operations. At the Python language level, immutable-string concatenation can copy the growing prefix and has a conservative $O(n^2)$ worst-case construction cost. CPython commonly optimizes uniquely referenced local `+=` strings, which is why competitive implementations often treat this loop as linear in practice. Building a list of characters and calling `''.join(parts)` would make the $O(n+R)$ time guarantee implementation-independent while using the same $O(n)$ output-building space.

## Alternatives and edge cases

- **Row-bucket simulation:** Move a row pointer down and up, append characters to per-row lists, and join the rows. It is easier to derive and guarantees linear string construction, but stores $O(n+R)$ bucket state rather than using direct indices.
- **Two-dimensional matrix:** This follows the visual layout literally but stores blank cells and scans them later, causing avoidable space and time overhead.
- **List plus final `join`:** Replace `zigzag += ...` with `parts.append(...)` and `''.join(parts)`. It preserves the exact index arithmetic and gives a robust $O(n+R)$ time bound in Python at the cost of an explicit character-reference list.
- **One row:** The early return avoids a zero `range` step and correctly returns the unchanged input.
- **Two rows:** `step = 2`; there are no interior rows, so the method outputs even indices followed by odd indices.
- **More rows than characters:** Most outer-loop rows have no valid `j`. Existing characters each occupy a separate downward row, so the output equals `s`; runtime still includes the $O(R)$ row scan.
- **Top row:** It has only indices `0, step, 2 * step, ...`; adding a diagonal character would duplicate another cycle position.
- **Bottom row:** It also has one position per cycle. The interior-row condition excludes it from the diagonal formula.
- **Incomplete final cycle:** `j` is already bounded by `range`, and the explicit diagonal check omits a missing upward character.
- **Punctuation and letter case:** Index arithmetic moves positions only. Every comma, period, uppercase letter, and lowercase letter is copied unchanged.
- **No character loss or duplication:** Vertical and interior diagonal offsets partition every cycle, so the result length remains exactly `n`.
- **Input preservation:** The algorithm indexes `s` and builds a new result; it never modifies the source string.
