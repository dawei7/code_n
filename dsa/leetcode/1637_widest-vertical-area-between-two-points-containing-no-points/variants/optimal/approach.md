## General
**Discard the irrelevant coordinate.** A vertical strip extends without limit along the y-axis. Whether a point lies inside it therefore depends only on that point's x-coordinate; changing any y-coordinate cannot change the answer. Extract the $n$ x-coordinates and sort them.

**Only neighboring x-coordinates can bound an empty strip.** Consider any valid strip whose boundaries are occupied x-coordinates $a<b$. If another point has an x-coordinate strictly between them, that point lies inside the strip regardless of its y-coordinate, contradicting validity. Thus $a$ and $b$ must be consecutive in sorted x-coordinate order. Conversely, the open strip between any consecutive pair is empty by definition of consecutiveness, and points on its boundaries are allowed.

Scan adjacent sorted coordinates and return their largest difference. Duplicate x-coordinates contribute a zero gap but require no special handling. Because every valid candidate corresponds to an adjacent pair and every adjacent pair defines a valid candidate, the maximum scanned difference is exactly the widest area.

## Complexity detail
Extracting coordinates and scanning gaps take $O(n)$ time. Sorting dominates at $O(n\log n)$ time. The extracted sorted array uses $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Sort the points in place:** Sorting full coordinate pairs by their first component avoids a separate extraction pass but mutates the input and has the same asymptotic bounds.
- **Ordered set:** Inserting x-coordinates into a balanced search tree and scanning them also takes $O(n\log n)$ time, with more overhead and no benefit from repeated coordinates.
- **Compare every pair:** Testing all possible boundary pairs is quadratic and still needs a way to establish that no intermediate x-coordinate exists.
- With exactly two points, their absolute x-coordinate difference is the answer, including zero when they share an x-coordinate.
- Multiple points may share one x-coordinate; duplicates create zero-width adjacent gaps and do not hide a wider gap elsewhere.
- Points on a chosen boundary are permitted, while even one point with a strictly intermediate x-coordinate invalidates that strip.
- Extreme y-coordinates have no effect because the strip has infinite height.
