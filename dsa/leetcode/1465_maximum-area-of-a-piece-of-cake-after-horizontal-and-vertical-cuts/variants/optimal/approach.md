## General

**Separate height from width.** Every cake piece is formed by one horizontal interval and one vertical interval. Its area is the interval height multiplied by the interval width. The greatest possible piece therefore combines the largest gap between horizontal boundaries with the largest gap between vertical boundaries.

This independence is valid because every horizontal cut crosses every vertical strip and every vertical cut crosses every horizontal strip. The rectangle at the intersection of the widest strip and tallest strip always exists.

**Add the outside boundaries as cut coordinates.** The supplied arrays contain only interior cuts. The top and bottom cake edges also bound pieces, at horizontal positions zero and `h`. Likewise, the left and right edges are at vertical positions zero and `w`.

The source appends those boundary coordinates with `extend`. Afterward, every possible piece dimension is the difference between two adjacent coordinates in the corresponding array. This unifies edge pieces with interior pieces and avoids separate first-gap and last-gap formulas.

The operation mutates both input lists. That is acceptable for the judged method, but callers should know that zeros and full dimensions remain appended and that both lists become sorted.

**Sort so geometric neighbors become list neighbors.** Cut coordinates may arrive in arbitrary order. After sorting, consecutive values describe adjacent horizontal or vertical boundaries. A non-adjacent pair spans one or more cuts and therefore does not describe a single uncut piece.

`pairwise(horizontalCuts)` lazily yields every adjacent pair. The generator `b - a for a, b in ...` computes each strip height, and `max` selects the tallest value `x`. The same process on vertical cuts gives widest strip `y`.

For `h = 5` and horizontal cuts `[1, 2, 4]`, adding boundaries and sorting gives `[0, 1, 2, 4, 5]`. Adjacent gaps are one, one, two, and one, so the maximum height is two. With width four and vertical cuts one and three, gaps are one, two, and one, so the maximum width is two. Their product is four.

**Why multiplying independent maxima is correct.** Let every horizontal gap be `H_i` and every vertical gap be `W_j`. Every piece has area `H_i * W_j`. All gaps are positive. For any pair, `H_i` is at most the maximum horizontal gap and `W_j` is at most the maximum vertical gap, so its area cannot exceed the product of those maxima.

The piece at the intersection of the maximizing horizontal interval and maximizing vertical interval achieves that upper bound. Therefore `x * y` is exactly the largest area.

**Apply the modulus only to the final area.** The problem asks for the maximum actual piece area modulo `10**9 + 7`. The code first finds true gap lengths and multiplies them, then applies the modulus. Taking remainders before comparing areas could change ordering and select the wrong piece, so maximization must precede modular reduction.

Python integers grow automatically, so multiplying dimensions up to one billion cannot overflow. In fixed-width languages, a sufficiently wide integer type is needed before the modulo.

**The invariant during each gap scan.** After processing the first several adjacent pairs, the running `max` represents the largest piece dimension among those intervals. Pairwise enumeration covers the top or left edge interval first, every internal interval next, and the bottom or right edge interval last because explicit boundaries are present. No dimension is missed.

## Complexity detail

Let `H` and `V` be the original numbers of horizontal and vertical cuts. Adding two boundaries to each list takes constant amortized work. Sorting costs `O(H log H + V log V)`. Pairwise gap scans take `O(H + V)` and are dominated by sorting.

The input lists themselves grow by two elements. Python's in-place Timsort may require `O(H + V)` temporary memory in the worst case. The pairwise iterators and scalar maxima use constant additional state. The manifest's `O(H + V)` space bound safely covers sort workspace and mutation.

If language-specific in-place sorting workspace is excluded, the explicit algorithm beyond the input lists uses `O(1)` state. Complexity discussions should state which convention is being used.

The output is a single modular integer.

## Alternatives and edge cases

- **Handle edge gaps separately:** Sort only interior cuts, compare the first coordinate, adjacent differences, and dimension minus the last coordinate. It avoids mutating the lists with boundary values but needs more cases.
- **Use sorted copies:** `sorted(horizontalCuts + [0, h])` preserves caller inputs at the cost of explicit `O(H + V)` copied storage.
- **Test every rectangle:** Combining every horizontal and vertical gap is unnecessary; the product of independent maxima proves the answer directly.
- **Unsorted gap scan:** Differences between adjacent input entries are meaningless until coordinates are ordered.
- **One cut in each direction:** Boundaries still create two gaps per dimension, and the larger of each is selected.
- **Cut near an edge:** The small edge gap competes normally with all other gaps.
- **Largest gap at an outer edge:** Appending zero and the full dimension ensures it is included.
- **Several equal maximum gaps:** Any intersection of a maximum height and width gives the same maximum area.
- **Distinct-cut guarantee:** Adjacent sorted differences are positive. Duplicate cuts outside the contract would create zero-width gaps without affecting the maximum.
- **Very large dimensions:** Python avoids multiplication overflow; other languages should widen before multiplying.
- **Modulo placement:** Apply it after choosing and multiplying true maximum gaps.
- **Input mutation:** The exact source extends and sorts both cut lists. Reusing those lists later will observe the changes.
- **Pairwise laziness:** It does not allocate a complete list of adjacent pairs.
- **No need to locate the piece:** Only the area is requested, so retaining gap endpoints is unnecessary.
