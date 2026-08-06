## General

**Count columns and relevant whole-row patterns**

Scan every row once. Convert the row to an immutable tuple, count its black pixels, and increment the global count
for each black column. Only a row containing exactly `target` black cells can satisfy the first source rule, so record
the frequency of only those row patterns.

**Recognize a complete block of identical rows**

Suppose a qualifying pattern occurs exactly `target` times. Every black position in that pattern appears in those
same `target` identical rows. If that position's global column count is also `target`, no additional different row can
contain a black pixel in the column. Both source rules then hold for all `target` pixels at that position.

For each pattern with frequency `target`, inspect its black positions. Every position whose column count is `target`
contributes all `target` pixels at once. Conversely, any valid pixel has a row with `target` black cells, a column with
`target` black cells, and identical rows at all those column positions. Its pattern must therefore occur exactly
`target` times, so this grouped calculation includes every valid pixel and no invalid one.

## Complexity detail

Creating row tuples, counting black cells and columns, and scanning qualifying patterns process
$O(rows \cdot cols)$ characters. Stored row-pattern keys can occupy $O(rows \cdot cols)$ space, and column counts use
$O(cols)$ additional space, for $O(rows \cdot cols)$ total auxiliary space.

## Alternatives and edge cases

- **Validate every black pixel directly:** repeatedly counts axes and compares whole rows, which can become
  polynomially slower on a dense picture.
- **Store row-index lists per pattern:** is equivalent to frequencies but retains identities the final count does not
  need.
- **Correct row count but wrong column count:** contributes nothing.
- **Correct counts with differing rows:** violates the second rule even when both axis totals match.
- **Pattern occurring more than `target` times:** makes each of that pattern's black columns exceed the target count.
- **No qualifying pattern:** naturally leaves the answer at zero.
