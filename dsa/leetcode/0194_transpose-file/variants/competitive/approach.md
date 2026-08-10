## General

**Accumulate one string for each original column**

The competitive script reads `file.txt` with `awk` and builds array `s`, where
`s[i]` represents input column `i`. Every input row contributes its field `i`
to the end of that string. When input is complete, printing `s[1]`, `s[2]`, and
so on converts original columns into output rows.

This design is necessary for a one-pass read because the first output row needs
one field from every input line. The script cannot print that row completely
until it has seen the whole file, so it buffers the transposed content in its
associative array.

**Use awk's row and field metadata**

For each record, `NF` gives the current field count and `$i` retrieves field
`i`. The loop from 1 to `NF` visits all cells of that input row. `NR` identifies
the first input row.

The Reference guarantees a rectangular table, so every row has the same field
count. As a result, each array entry receives the same number of appended
fields and no output line needs padding.

**Initialize each column from row one**

When `NR == 1`, the assignment `s[i] = $i` stores the first field directly.
This special case prevents a leading space before the first output value.

For later records, `s[i] = s[i] " " $i` appends exactly one space and then the
new field. The literal delimiter in the output is therefore controlled by the
script rather than inherited from whatever spacing appeared in the input.

Even if input fields were separated by several spaces, default `awk` splitting
would identify the same fields and the output would normalize them to one
space. Under the exact Reference, a single space already separates fields.

**Print after all accumulation**

The `END` block starts at index one and continues while `s[i] != ""`. It prints
each completed column string. Because valid fields are understood to contain
nonempty values, `s[1]` through the last column are nonempty and the first
unset entry terminates the loop.

This stopping condition is less explicit than saving the column count. If an
empty field were representable, an empty `s[i]` could stop output early. Default
whitespace field splitting does not preserve empty fields between delimiters,
and the Reference does not define empty columns, so the source is correct for
its intended domain. Tracking `cols = NF` and looping through `cols` would be a
more robust general form.

**Trace all array states for the sample**

After row `name age`, `s[1]` is `name` and `s[2]` is `age`.

After row `alice 21`, the entries are `name alice` and `age 21`.

After row `ryan 30`, they are `name alice ryan` and `age 21 30`.

The end loop prints index one before index two, yielding the exact required
output. No sorting occurs, so original row order becomes field order within
each output line and original column order becomes output line order.

**Why the mapping is complete**

Consider original cell in row $r$ and column $c$. During processing of row
$r$, loop iteration `i = c` appends `$c` to `s[c]`. Earlier rows have already
placed their column-$c$ fields before it, and later rows append after it. Thus
the cell occupies position $r$ on output line $c$.

Every input cell receives exactly one such visit, and every populated `s[c]`
is printed once. Therefore the script implements the transpose bijection
without dropping, duplicating, or reordering fields.

**Interpret the source's square notation**

The source comments state $O(n^2)$ time and space, which assumes or informally
imagines an $n$-by-$n$ table. The actual Reference allows $r$ rows and $c$
columns. The precise data-volume bound is $O(rc)$, as the manifest records.

There is also a lower-level caveat: each update concatenates a longer string.
If the awk implementation copies the entire prior string on every append, one
column can incur quadratic character copying in the number of rows. The
manifest uses the standard cell-processing abstraction; real performance on
very tall, long-field inputs can depend on string implementation.

**Streaming limits and file assumptions**

Although input is read once, output is not fully streaming because all column
strings remain in memory until `END`. A general transpose cannot emit its first
line early unless it rereads input or uses external storage, because future rows
still contribute to that line.

The command expects `file.txt` in the working directory. It uses default awk
whitespace splitting, so literal spaces inside a field are not supported and
multiple delimiters do not encode empty cells.

## Complexity detail

For $r$ rows and $c$ fields per row, the loops visit $rc$ cells and later print
$c$ accumulated strings containing $rc$ total fields. Under the conventional
model, time is $O(rc)$ and stored output text is $O(rc)$, matching the manifest.

The associative array has $c$ keys, but the strings behind those keys contain
the whole output. Counting only keys as $O(c)$ would understate memory. Repeated
concatenation may add implementation-dependent copying beyond the abstract
$O(rc)$ traversal.

## Alternatives and edge cases

- **Track column count explicitly:** Save `cols = NF` and print `i <= cols`; clearer and safer than testing `s[i] != ""`.
- **Optimal source:** Uses the last row's `NF` as its end bound but has a confusing uninitialized-variable concatenation in first-row setup.
- **Cell matrix:** Store by `(row,column)` and assemble output later; easier to adapt but still stores all cells.
- **Repeated file scans:** Print one column per pass, trading memory for extra I/O.
- **One row:** Produces one output line per field.
- **One column:** Produces one output line containing all rows.
- **Empty file:** No `s[1]` exists, so the end loop prints nothing.
- **Empty field:** Not represented by default whitespace splitting; a different parser and explicit column bound would be needed.
- **Unequal row lengths:** Outside the contract and can create missing or extra accumulated entries.
- **Long fields:** Total character size and repeated concatenation cost matter beyond simple cell counts.
