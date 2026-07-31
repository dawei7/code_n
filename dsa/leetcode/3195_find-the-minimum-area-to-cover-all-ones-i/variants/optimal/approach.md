## General

**A valid rectangle is determined by four extremes**

Let `top` and `bottom` be the smallest and largest row indices containing a
`1`, and let `left` and `right` be the corresponding column extremes. Any
rectangle covering every `1` must reach at least these four coordinates. It
therefore cannot have height smaller than `bottom - top + 1` or width smaller
than `right - left + 1`.

Scan every matrix cell once. Whenever a `1` is found, update each relevant
minimum or maximum. The problem guarantees at least one `1`, so all four
boundaries are defined after the scan. The rectangle bounded by those
coordinates contains every `1` by construction, and the preceding lower
bounds show that no valid rectangle can be shorter or narrower. Its area,
`(bottom - top + 1) * (right - left + 1)`, is consequently minimal.

## Complexity detail

Let $R$ and $C$ be the numbers of rows and columns. Inspecting all $RC$ cells
takes $O(RC)$ time. Only four boundary indices are maintained, so the
auxiliary space usage is $O(1)$.

## Alternatives and edge cases

- **Collect all occupied coordinates:** Storing every `1` position before
  taking coordinate minima and maxima is correct, but uses $O(RC)$ space in a
  dense matrix without simplifying the scan.
- **Search inward from all four borders:** Four directional scans can stop
  after locating each boundary, but still require $O(RC)$ worst-case time and
  revisit cells.
- A single occupied cell produces height and width one, hence area one.
- A one-row or one-column grid reduces the rectangle to the inclusive span
  between its first and last `1`.
- Zeros inside the boundary rectangle do not matter; only containment of all
  ones is required.
- The guarantee of at least one `1` removes the need for an empty-result case.
