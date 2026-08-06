## General
The file arrives in row-major order, but each output line needs one value from every input row. The candidate uses an `awk` associative array keyed by `(row, column)` so every input field can be stored once and emitted once in transposed order.

For each record, loop from field `1` through `NF` and assign `$column` to `cells[NR, column]`. Record the first row's field count in `columns`; the rectangular-input guarantee means every later row has that same count.

After the file has been read, reverse the traversal order rather than moving data. The outer `END` loop chooses one original column, and the inner loop visits every original row. Print one space before fields after the first, print the stored field itself, and finish each transposed row with a newline.

For input

```text
name age
alice 21
```

the read phase stores `cells[1,1] = "name"`, `cells[1,2] = "age"`, `cells[2,1] = "alice"`, and `cells[2,2] = "21"`. The output phase visits `(1,1), (2,1)` and then `(1,2), (2,2)`, producing `name alice` followed by `age 21`.

Every source coordinate `(r, c)` is assigned exactly once. During output, the loop for original column `c` visits `(1,c), (2,c), ..., (rows,c)` in order, so it emits precisely original column `c` as transposed row `c`. Iterating columns numerically from one through `columns` preserves their original left-to-right order. Therefore each source cell moves conceptually from `(r,c)` to `(c,r)`, with no omission, duplication, or trailing separator.

## Complexity detail
The read phase visits and stores all $rc$ fields once, and the output phase visits and emits all $rc$ stored fields once, giving $O(rc)$ logical work. The associative array retains every field until `END`, using $O(rc)$ space. Unlike repeated column-string concatenation, no growing prefix is recopied after each newly read row.

## Alternatives and edge cases
- **Growing column strings:** Accumulating one string per output column is compact and common, but immutable-string implementations may repeatedly copy an ever-growing prefix and exceed the stated linear work.
- **Repeated file scans:** Re-reading the file once per column reduces retained state, but performs repeated I/O and requires discovering the column count before emission.
- **Streaming output:** Printing while reading cannot finish an output row until values from all later input rows are known.
- **Single dimensions:** A one-row file becomes one output line per field; a one-column file becomes one line containing all rows.
- **Rectangular input:** The contract guarantees a nonempty table with equal field counts. Ragged rows would require an explicit missing-field policy.
- **Whitespace:** Default `awk` field splitting accepts whitespace runs even though the source guarantees single-space separators; the candidate emits exactly one space between output fields.
