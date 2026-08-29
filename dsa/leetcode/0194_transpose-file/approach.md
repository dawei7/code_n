## General

**Translate rows into growing output columns**

Transposing swaps the two dimensions of a rectangular table. Input field at
row $r$, column $c$ must appear at output row $c$, position $r$. Because the
script reads input one row at a time, it maintains one accumulated string for
each input column. After all rows are read, each accumulated string is exactly
one output row.

`awk` supplies the needed coordinates automatically. `NR` is the current
one-based input row number, `NF` is the number of fields on that row, and `$i`
is field `i`. Default field splitting treats runs of whitespace as separators;
the Reference's space-separated rows fit that model.

**Visit every field in the current row**

For each input record, the loop runs `i` from 1 through `NF`. Array `res` is an
associative array indexed by column number. Every visit updates `res[i]`, so all
values from input column `i` collect in the same destination entry.

The equal-column-count guarantee is crucial. It means every normal input row
contributes one field to every output row, and no destination must represent a
missing cell or invent padding.

**Initialize from the first row without a leading space**

When `NR == 1`, the result string for each column should become just that first
field. Starting with the field itself avoids a leading delimiter in final
output. Later rows can safely prepend exactly one space before each appended
field.

The exact assignment is written `res[i] = re$i`, not the clearer
`res[i] = $i`. In awk, adjacency denotes string concatenation. The token `re`
is an uninitialized variable whose value is the empty string, followed by field
expression `$i`. Consequently, `re$i` evaluates to the current field in this
script and the output is correct.

This is nevertheless a fragile and confusing source detail. If `re` ever
received a value, that text would be prefixed to every first-row field. Writing
`res[i] = $i` directly would express the intended initialization without
depending on an unrelated empty variable.

**Append later rows with one separator**

For every row after the first, the assignment constructs
`res[i] " " $i`. It preserves the accumulated fields, adds one literal space,
and appends the new field. Therefore, after processing input rows 1 through
$r$, `res[i]` contains fields `(1,i)` through `(r,i)` in row order with exactly
one space between adjacent values.

The script does not reorder input rows, so each output row preserves their
original top-to-bottom order as left-to-right order.

**Print one accumulated entry per input column**

The `END` action runs after the file has been consumed. Its loop prints
`res[1]` through `res[NF]`. In awk, `NF` after input ends retains the field count
of the last record. Since every row is guaranteed to have the same number of
columns, that value is also the table's column count.

Using a dedicated saved variable such as `cols = NF` on the first row would be
more explicit. The exact source's last-row `NF` dependency is still correct
under the rectangular-input guarantee.

**Trace the example**

After reading `name age`, the two entries are `res[1] = "name"` and
`res[2] = "age"`. After `alice 21`, they become `name alice` and `age 21`.
After `ryan 30`, they become `name alice ryan` and `age 21 30`.

`END` sees `NF = 2` and prints those two entries in increasing column order,
which is the required transpose.

**Why every output position is exact**

For a fixed column `i`, the script visits `$i` once for each input row and
appends it to `res[i]` in that row's processing order. No field from another
column enters that entry. Hence output line `i` contains exactly the original
column `i`, ordered by input row.

The final loop emits every column index once, in increasing order. Together,
these facts establish the transpose mapping from every input coordinate
`(row, column)` to output coordinate `(column, row)` without loss or
duplication.

**Input and output boundaries**

The script reads the literal relative path `file.txt` and prints to standard
output. It does not write back to the file. Fields should not themselves contain
spaces because spaces are delimiters. Default awk splitting also collapses
multiple spaces, which is harmless for field values but does not preserve empty
columns if a broader file format allowed them; the Reference uses separated
fields rather than empty-cell encoding.

## Complexity detail

Let $r$ be the number of rows and $c$ the number of columns. The nested logical
processing visits each of the $rc$ fields once, giving $O(rc)$ work under the
standard field-operation model. Output also contains all $rc$ fields.

The array stores $c$ strings containing the entire transposed output, totaling
$O(rc)$ characters, matching the manifest. Repeated immutable-string
concatenation can cause extra copying in a particular awk implementation and
make character-level runtime worse than linear in very tall tables; the stated
bound treats each accumulated append according to the conventional pipeline
model.

## Alternatives and edge cases

- **Clear first-row assignment:** Replace `re$i` with `$i`; this removes reliance on an uninitialized variable without changing the algorithm.
- **Store individual cells:** Save `cell[NR,i]` and print later; clearer indexing but still $O(rc)$ storage and more output logic.
- **Stream by repeated column scans:** Read the file once per column to reduce stored output, but multiplies file I/O and requires knowing the column count.
- **Single row:** Each input field becomes a one-field output line.
- **Single column:** All input fields become one space-separated output line.
- **Empty file:** Default `NF` is zero and nothing is printed.
- **Unequal row widths:** Outside the guarantee; final `NF` could omit stored columns or missing values could misalign output.
- **Multiple separator spaces:** Default awk splitting collapses them rather than treating them as empty columns.
- **Fields containing spaces:** Unsupported because space is the delimiter.
- **Working directory:** Must contain `file.txt` at the referenced path.
