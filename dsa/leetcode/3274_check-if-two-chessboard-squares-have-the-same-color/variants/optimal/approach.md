## General

**Encode the checkerboard with parity**

Number the columns from zero, so files `a` through `h` have indices $0$ through $7$. Keep the row's digit as its integer value. For a coordinate, add those two values and retain only whether the sum is even or odd.

Moving one square horizontally changes the column index by one, while moving one square vertically changes the row by one. Either move flips the sum's parity, exactly as it flips the square's color. Consequently, all squares with one parity share a color and all squares with the other parity share the opposite color. The two coordinates name the same color precisely when their parity values are equal.

## Complexity detail

Each coordinate always has exactly two characters. The algorithm reads those fixed positions and performs constant arithmetic, so it uses $O(1)$ time and $O(1)$ space.

## Alternatives and edge cases

- **Explicit color table:** A set containing all 32 squares of one color permits membership comparison, but it stores information that parity derives directly.
- **Compare character-code sums:** Adding the file character code and rank digit also preserves the needed parity, though converting to documented board indices makes the reasoning clearer.
- **Use coordinate differences:** The squares match when the sum of the absolute column and row differences is even; this is equivalent but needs both differences.
- Identical coordinates necessarily have the same color.
- Opposite corners `a1` and `h8` have the same color because both coordinates change by an odd amount.
- Adjacent squares always have different colors because exactly one coordinate changes by one.
- The input guarantee removes any need to validate string length, file, or rank.
