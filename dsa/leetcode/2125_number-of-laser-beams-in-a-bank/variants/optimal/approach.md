## General

**Discard empty rows conceptually**

Count the devices in each row. Empty rows neither supply a beam endpoint nor
block a beam, so after ignoring them, beams exist only between consecutive
nonempty rows. Any two nonconsecutive nonempty rows have another device row
strictly between them and cannot connect.

Keep `previous_devices`, the count in the most recent nonempty row. When the
current row has $c>0$ devices, every one of its devices connects independently
to every device in that preceding row, contributing
`previous_devices * c`. Add that product and replace the stored count with
$c$. Empty rows leave the stored count unchanged.

Each valid beam joins one unique device pair in consecutive nonempty rows and
is counted in their Cartesian product. Conversely, every pair included by such
a product has only empty physical rows between its endpoints, so it satisfies
the beam condition. The accumulated products therefore count every beam once
and no invalid pair.

## Complexity detail

Counting devices inspects each of the $S=mn$ cells once, for $O(S)$ time. The
algorithm stores only the previous row count and total, so auxiliary space is
$O(1)$.

## Alternatives and edge cases

- **Enumerate every device pair:** Test whether two devices use different rows
  and scan every intervening row. This is correct but can take quadratic or
  worse time in the number of cells.
- **Materialize nonempty row counts:** Filter all positive counts and sum
  products of adjacent entries. This also takes $O(S)$ time but uses $O(m)$
  extra space.
- Empty rows never reset the previous nonempty count.
- A bank with fewer than two nonempty rows has zero beams.
- Adjacent physical rows have no intervening row, so all their cross-row device
  pairs qualify.
- A nonempty middle row blocks beams between the nonempty rows on either side.
