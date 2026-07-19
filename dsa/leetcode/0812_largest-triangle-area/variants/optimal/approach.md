## General
**Measure area with a cross product**

For points `A`, `B`, and `C`, the absolute cross product of vectors $B - A$ and $C - A$ equals twice the triangle area:

$| (B_{x} - A_{x})(C_{y} - A_{y}) - (B_{y} - A_{y})(C_{x} - A_{x}) |$.

All coordinates are integers, so keep this doubled area as an integer while comparing candidates and divide the maximum by two only once at the end.

**Enumerate every possible triangle**

Use three increasing indices so each unordered group of three points is considered exactly once. The cross-product formula gives the exact area for that group, including zero for collinear points. Since every permissible triangle corresponds to one such index triple, taking the maximum examines and selects the global optimum.

## Complexity detail
There are $\binom{n}{3} = O(n^3)$ point triples, and each area calculation is constant time. Apart from loop indices and the current maximum, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Convex hull reduction:** A maximum-area triangle uses hull vertices; computing the hull can discard interior points, though it adds algorithmic complexity unnecessary for the given constraints.
- **Heron's formula:** Distances and a square root produce the same area but introduce avoidable floating-point calculations.
- **Re-solve every prefix:** Recomputing the largest triangle after each newly included point is correct but repeats earlier triples and takes $O(n^4)$ time.
- **Enumerate every subset mask:** Filtering all $2^{n}$ subsets for those of size three is correct but exponentially wasteful.
- **Collinear points:** Their cross product is zero and they cannot improve a positive maximum.
- **Clockwise order:** The determinant may be negative, so take its absolute value.
- **Half-unit area:** An odd doubled area becomes a result ending in `.5` after division.
- **Interior points:** They are harmless; exhaustive triples need no special geometric classification.
