## Description

Consider every pair of rows in `Points` as the opposite corners of an
axis-aligned rectangle. Report only the pairs that produce a non-zero area.

Each result row contains `(p1, p2, area)`:

- `p1` and `p2` are the IDs of the two opposite corner points;
- `area` is the rectangle's area and must be non-zero.

Sort the result by `area` descending. Break an area tie by `p1` ascending, then
break any remaining tie by `p2` ascending. The example shows the required
result format.
