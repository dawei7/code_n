## General

**Represent excavation as membership**

Whether an artifact is extractable depends only on which coordinates were dug, not on the order in which they appear. Convert every two-element entry in `dig` to a coordinate tuple and place it in a hash set. This provides expected constant-time membership tests without allocating the full $n \times n$ grid.

For each inclusive artifact rectangle, enumerate rows from `r1` through `r2` and columns from `c1` through `c2`. If any coordinate is absent from the dug set, stop checking that artifact because it cannot be extracted. Count the artifact only if every covered coordinate is present.

An artifact is counted only after all cells of its declared rectangle pass the membership test, so every counted artifact is fully uncovered. If an artifact is fully uncovered, each of those same tests succeeds and the scan reaches the count operation, so no extractable artifact is omitted. The rectangles do not overlap, although correctness does not require that guarantee.

## Complexity detail

Building the set costs expected $O(d)$ time. Each artifact covers at most four cells, so all rectangle checks cost at most $4a=O(a)$ expected time. Total expected time is $O(a+d)$ under standard hash-table behavior.

The dug-coordinate set stores $d$ entries and uses $O(d)$ auxiliary space.

## Alternatives and edge cases

- **Full grid marking:** A boolean $n \times n$ grid also gives constant-time lookup, but wastes $O(n^2)$ space when relatively few cells are dug.
- **Linear search in `dig`:** Searching the coordinate list for every artifact cell is correct but can require $O(ad)$ time.
- **Single-cell artifacts:** Such an artifact is extractable exactly when its one coordinate was dug.
- **Partially uncovered rectangles:** One missing cell is sufficient to reject the entire artifact, so checking can stop immediately.
- **Dug empty ground:** Coordinates not covered by any artifact have no effect on the answer.
