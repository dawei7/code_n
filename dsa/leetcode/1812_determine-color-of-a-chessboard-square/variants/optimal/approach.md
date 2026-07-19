## General
**Convert both labels to zero-based indices**

Map the file letter to `0` through `7` by subtracting the code point of `"a"`. Convert the rank digit to an integer and subtract one. The reference square `"a1"` then becomes `(0, 0)`.

**Use the checkerboard parity invariant**

Moving one file or one rank flips color, so every unit change flips the parity of the coordinate sum. A square is the same color as `"a1"` when its zero-based file and rank sum is even, and the opposite color when that sum is odd. Since `"a1"` is black, return whether the sum is odd.

This rule is sufficient because any square can be reached from `"a1"` using exactly its file-index plus rank-index unit moves. An even number of color flips ends on black; an odd number ends on white.

## Complexity detail
The method performs a fixed number of character conversions, additions, and parity operations, independent of the chosen square. It therefore takes $O(1)$ time and uses $O(1)$ space.

## Alternatives and edge cases
- **Explicit set of white squares:** A 32-entry lookup works but stores data that the parity rule derives directly.
- **Parity of raw character codes:** Adding the file code and rank value can be shortened algebraically, but explicit zero-based indices make the `"a1"` reference easier to verify.
- **Adjacent squares:** Moving one step horizontally or vertically must invert the result.
- **Diagonal neighbors:** Moving one file and one rank performs two flips and preserves color.
- **Board corners:** `"a1"` and `"h8"` are black, while `"a8"` and `"h1"` are white.
- **Input validation:** The contract guarantees exactly one valid file and rank, so no malformed-coordinate branch is needed.
