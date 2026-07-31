## General

**Exploit the bounded height coordinate**

Rectangle heights and point $y$-coordinates are at most $100$. Create one
bucket for every possible height and place each rectangle's width in the
bucket matching its exact height. Sort the widths inside every bucket.

**Answer one point**

A point `(x, y)` can belong only to rectangles in height buckets from `y`
through `100`. Within one eligible bucket, the widths are sorted. Binary
search for the first width at least `x`; every width in the suffix represents
a rectangle that reaches the point horizontally as well as vertically. Add
those suffix sizes across all eligible heights.

The query order is preserved by appending each computed count directly to the
answer. Every counted rectangle satisfies both inclusive coordinate
inequalities. Conversely, any containing rectangle lies in an inspected
height bucket and in the binary-searched width suffix, so none is omitted.

## Complexity detail

Let $R=\lvert\texttt{rectangles}\rvert$, $P=\lvert\texttt{points}\rvert$, and
$H=100$ be the bounded height range. Sorting all buckets costs
$O(R\log R)$ in the worst case. Each point performs at most $H$ binary
searches, for $O(PH\log R)$ query time. Total time is
$O(R\log R+PH\log R)$, and the buckets use $O(R+H)$ space.

## Alternatives and edge cases

- **Check every rectangle for every point:** This direct method is correct but costs $O(RP)$ time.
- **One global width ordering:** Width alone cannot determine containment because rectangle height must also reach the point.
- **Sweep by width with a Fenwick tree:** Sorting rectangles and points by decreasing width and querying heights also gives an efficient solution, but the height bound makes buckets simpler.
- **Boundary points:** Use widths and heights greater than or equal to the point coordinates, not strict comparisons.
- **No containing rectangle:** Every eligible bucket suffix can be empty, producing count `0`.
- **Maximum point height:** Only the height-100 bucket needs inspection.
- **Repeated dimensions:** Rectangles are unique as pairs, but widths or heights may repeat and each rectangle still contributes separately.
