## General

**Only consecutive nonempty rows can connect**

Suppose two device-containing rows have another nonempty row between them. That middle row contains a security device, so the beam condition fails for every pair across the outer rows.

Therefore, beams exist only between consecutive rows in the sequence of nonempty rows. Completely empty rows may lie between them without blocking anything.

The source tracks `pre`, the number of devices in the most recent nonempty row.

**Count devices in the current row**

For each binary string `row`,

`row.count("1")`

computes the number of devices. The assignment expression

`cur := row.count("1")`

stores that count while testing whether it is positive.

If `cur == 0`, the row is ignored and `pre` remains unchanged. This is important: an empty row does not become a new beam endpoint and does not block beams.

**Multiply endpoint choices**

When the current row contains `cur` devices and the preceding nonempty row contains `pre` devices, every device in the earlier row forms one beam with every device in the current row.

The number of pairs is the product

`pre * cur`.

After adding it to `ans`, the current row becomes the new most recent nonempty row, so `pre = cur`.

For the first nonempty row, `pre` is zero. It creates no beam because no earlier nonempty row exists, then initializes the state for the next one.

**Trace the first example**

Device counts by row are 3, 0, 2, and 1.

- The row with 3 devices contributes $0\cdot3=0$ and sets `pre=3`.
- The empty row is skipped, leaving `pre=3`.
- The row with 2 devices contributes $3\cdot2=6$ and sets `pre=2`.
- The row with 1 device contributes $2\cdot1=2$.

The total is 8.

No beams connect the first and last nonempty rows because the two-device row lies between them and blocks that relationship.

**Why every cross-product pair is valid**

Between two consecutive nonempty rows, every intervening physical row is empty by definition. The beam condition depends only on the absence of devices in intermediate rows, not on columns.

Thus every choice of one device from the first row and one from the second produces a distinct beam. There are exactly the product of their counts.

**Why no other beams are missed**

Take any valid beam between rows $r_1<r_2$. Every intermediate row must be empty, so $r_1$ and $r_2$ are consecutive among nonempty rows. The algorithm multiplies their counts when it processes $r_2$, including that device pair.

Conversely, every pair counted by a product lies in consecutive nonempty rows and has only empty rows between, so it satisfies both beam conditions.

Each beam belongs to one consecutive-row pair and is counted once.

**Why beam independence needs no extra state**

The problem says beams do not interfere or merge. Therefore, sharing a device or crossing another conceptual beam does not reduce the count.

Simple pair multiplication is sufficient; there is no need to mark devices as used.

**Maintain the precise loop invariant**

Immediately before a nonempty current row is processed, `pre` equals the device count in the nearest earlier nonempty row, or zero if none exists. Empty rows leave this statement unchanged.

The product therefore counts beams against exactly the one earlier row that can satisfy the no-intermediate-device condition. Assigning `pre = cur` reestablishes the invariant for all later rows.

This invariant explains both important updates: skip empty rows entirely, but replace `pre` after every nonempty row.

**Why row distance is irrelevant**

The number of empty rows between two consecutive nonempty rows does not affect beam count. The rule requires only that those intermediate rows contain no devices; it does not impose a maximum vertical distance or a same-column condition.

Thus two nonempty rows separated by one empty row and by one hundred empty rows contribute the same cross product when their device counts match.

## Complexity detail

Let

$$
S=\sum_{\text{row}\in\texttt{bank}}\lvert\text{row}\rvert,
$$

the number of cells in the matrix.

Each row count scans its characters once, so total time is $O(S)$.

Only `ans`, `pre`, and `cur` are stored. Auxiliary space is $O(1)$.

The answer may contain products of row counts, but Python integers handle the constraint range safely.

## Alternatives and edge cases

- **Store all nonempty row counts:** Then multiply consecutive entries. It is correct but uses $O(m)$ storage that `pre` avoids.
- **Compare every pair of nonempty rows:** Most are blocked by an intermediate nonempty row and would add unnecessary quadratic work.
- **Track device columns:** Columns do not affect whether a beam exists, so only row counts matter.
- **All rows empty:** `pre` stays zero and the answer is zero.
- **Only one nonempty row:** There is no second row for a beam.
- **Empty rows between endpoints:** They are skipped and do not break eligibility.
- **Nonempty row between endpoints:** It becomes the new `pre` and prevents counting across it.
- **One device per consecutive row:** Each adjacent nonempty-row pair contributes one.
- **Many devices:** Every cross-row pair is independent and counted.
- **First nonempty row:** Its product with initial zero contributes nothing.
- **Walrus operator:** It stores the count and tests positivity in one expression.
- **Input preservation:** Row strings and the bank array are unchanged.
- **Nearest earlier nonempty row:** `pre` always refers to this row, never merely the immediately preceding physical row.
- **Vertical gap length:** Any number of empty rows is allowed and does not alter the product.
