## General

**Fill one rectangular perimeter at a time**

The unfilled region is described by inclusive `left`, `right`, `top`, and `bottom` bounds. They initially enclose the whole square. One `while` iteration writes the current perimeter clockwise, then moves all four bounds inward.

`num` is always the next integer to write. Every successful cell assignment is followed immediately by `num += 1`, keeping matrix position order synchronized with numeric order.

**Top edge: left to right**

The first loop fills row `top` from column `left` through `right`, including both top corners. These are the first cells of the current spiral layer.

Since the corners are already assigned, subsequent edge loops either exclude those corners by range or guard degenerate layers to prevent overwriting them.

**Right edge interior: top to bottom**

The second loop uses rows `top + 1` through `bottom - 1` at column `right`. It excludes the top-right corner written by the top loop and the bottom-right corner reserved for the bottom loop.

When no interior row exists, the range is empty and no number is consumed.

**Bottom edge: right to left only when distinct**

The third loop traverses columns from `right` back through `left` in row `bottom`. The append/assignment occurs only if `top < bottom`.

If the remaining layer is one row tall, top and bottom identify the same row. That row was already filled left to right, so writing it again would overwrite values with later numbers and cause the sequence to exceed the available cells. The strict inequality prevents both the overwrite and the corresponding increments.

**Left edge interior: bottom to top only when distinct**

The final loop traverses rows `bottom - 1` down through `top + 1` at column `left`. It excludes both corners. Assignment occurs only if `left < right`.

For a one-column layer, left and right are the same column, and earlier edge phases already cover its cells. The guard prevents duplicate writes. Placing the condition inside the loop may perform unused iterations in a degenerate layer, but `num` does not change during them.

**Shrink and repeat**

After completing the perimeter, incrementing `left` and `top` and decrementing `right` and `bottom` removes precisely the cells just written. The next iteration begins with the interior square.

The loop condition requires both a nonempty row range and a nonempty column range. When the bounds cross, no zero cell remains.

**Correctness invariant**

At the start of each layer, cells outside the bound rectangle contain exactly the numbers from 1 through `num - 1` in clockwise spiral order, and every cell inside remains zero.

The four traversals cover the perimeter exactly once: top and bottom include corners, while vertical edges exclude them; guards resolve a single remaining row or column. Assigning increasing `num` values therefore extends the spiral without gaps or duplicates.

Shrinking the rectangle restores the invariant. At termination, every layer has been removed, so all $n^2$ cells contain exactly 1 through $n^2$ in required order.

**A three-by-three center case**

The first iteration writes values 1 through 8 around the outer ring. Bounds then all become 1, describing the center cell. The top loop writes 9. The bottom guard fails because top equals bottom, and the left guard fails because left equals right, so the center is not overwritten.

**Why the final number must be exactly correct**

The four edge descriptions are disjoint after their corner exclusions and guards. Every actual assignment increments `num` once, while every skipped duplicate position increments it zero times. Since the peeled layers partition all $n^2$ cells, exactly $n^2$ assignments occur. Starting from 1 means the last written value is $n^2$, with neither a missing number nor an extra write beyond the matrix.

## Complexity detail

Every one of the $n^2$ cells is assigned exactly once. Degenerate guarded loops add only boundary-proportional checks and do not change the bound. Time is $O(n^2)$.

The returned matrix requires $\Theta(n^2)$ output space. The four bounds, `num`, and loop indices use constant storage; ranges and reversed ranges are lazy in Python 3. Auxiliary space excluding output is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Direction simulation using output zeros:** Walk cell by cell and turn when the next coordinate is outside or already nonzero. It is equally constant-auxiliary because the output itself marks visits.
- **Move conditions around loops:** Guard whole bottom and left loops instead of each assignment. This avoids unnecessary degenerate iterations while keeping identical output.
- **Separate marker grid:** It is unnecessary because all unwritten output cells are zero and written values are positive.
- **`n = 1`:** The top edge writes the only value, and both duplicate-prevention guards fail.
- **Odd `n`:** A single center cell forms the last layer and is written once.
- **Even `n`:** The innermost layer has no lone center; ordinary edge traversals complete it.
- **Number synchronization:** `num` advances only after an actual write, so skipped degenerate traversals cannot create gaps.
- **Corners:** Horizontal edges own them; vertical ranges exclude them.
- **Fresh output:** No caller-owned collection is mutated.
- **Constraint `n > 0`:** Initial bounds describe at least one cell; no empty-matrix special case is needed.
