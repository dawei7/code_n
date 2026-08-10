## General

Chessboard colors alternate whenever one moves one square horizontally or vertically. Assign a numeric column index to each letter and use the numeric row. The color is determined by the parity of column plus row: squares with equal parity sums have the same color.

The code does not explicitly convert each coordinate to a zero-based pair. Instead, it computes differences:

`x = ord(coordinate1[0]) - ord(coordinate2[0])`

and

`y = int(coordinate1[1]) - int(coordinate2[1])`.

ASCII/Unicode codes for lowercase letters are consecutive, so the letter-code difference equals the difference between column indices. Row characters are converted to integers before subtraction.

Let the two squares have coordinates $(c_1,r_1)$ and $(c_2,r_2)$. They share a color exactly when

$$
(c_1+r_1)\bmod2=(c_2+r_2)\bmod2.
$$

Moving all terms to one side gives

$$
(c_1-c_2+r_1-r_2)\bmod2=0.
$$

That left side is exactly `x + y`, so `(x + y) % 2 == 0` implements the criterion.

For `a1` and `c3`, the column difference is minus two and the row difference is minus two. Their sum is minus four, an even number, so the method returns true.

For `a1` and `h3`, differences are minus seven and minus two, totaling minus nine, which is odd, so the colors differ.

**Why absolute values are unnecessary.** Parity does not change when a number's sign changes. Python also gives remainder zero for every negative even integer under `% 2`. The signed coordinate difference is therefore sufficient.

**Why zero-based versus one-based indexing does not matter.** Adding or subtracting the same constant from both column indices cancels in their difference. One may map `a` to zero or one; the same-color test remains identical. Rows are one-based in notation, but only their difference matters too.

An alternative intuition is Manhattan distance: each horizontal or vertical step flips color, so two squares have the same color when the number of steps between them, `abs(x)+abs(y)`, is even. Signed `x+y` has the same parity as that absolute sum because $-v$ and $v$ have equal parity.

The valid-coordinate guarantee means the source does not need length checks or bounds validation. Both strings contain exactly one column character and one single-digit row character.

## Complexity detail

The method performs a fixed number of character accesses, conversions, subtractions, and one modulo test. Time complexity is $O(1)$.

Only two integer differences are stored, giving $O(1)$ auxiliary space. Inputs are immutable strings and remain unchanged.

The fixed eight-by-eight board size is not traversed or represented in memory.

## Alternatives and edge cases

- **Compute each parity separately:** Convert columns to indices and compare `(column + row) % 2` values. This is equally correct but uses a few more explicit steps.
- **Manhattan-distance parity:** Return whether `abs(dx) + abs(dy)` is even. It expresses the color-flip-per-step interpretation.
- **Hard-coded color table:** An eight-by-eight Boolean table works but wastes space and obscures the general parity rule.
- **Compare only rows or columns:** Either coordinate can flip color; both differences must be combined.
- **Same square:** Both differences are zero, so the method correctly returns true.
- **Same row:** Color matches only when the column difference is even.
- **Same column:** Color matches only when the row difference is even.
- **Opposite corners `a1` and `h8`:** Both differences are odd, their sum is even, and the corners share a color.
- **Negative difference:** Python modulo still identifies evenness correctly.
- **Letter encoding:** Consecutive lowercase letters make code-point subtraction valid. Arbitrary labels would require an explicit map.
- **Single-digit rows:** Direct `int(coordinate[1])` works because legal rows are one through eight. A larger board with multi-digit rows would need slicing.
- **Board orientation:** Rotating or reflecting the standard alternating coloring preserves the same-color equivalence even if black and white labels swap.
- **Why diagonal movement preserves color:** One diagonal step changes both column and row parity, causing two color flips and returning to the original color. This matches an even sum of coordinate differences.
- **Why a knight-like displacement differs:** A change of two in one coordinate and one in the other has odd total parity, so it reaches the opposite color. The formula captures this without knowing chess move rules.
- **Explicit black-square formula:** With `a1` designated black, a square is black when a zero-based column plus one-based row is odd. Choosing the opposite convention swaps color names but leaves equality comparisons unchanged.
- **No dependence on distance magnitude:** Squares far apart can share a color; only whether total displacement is even matters. The code reduces the entire displacement to one parity bit.
- **Character subtraction before conversion:** Column letters need no dictionary because their code points are consecutive. Rows are digit characters, so converting them numerically makes their difference match board steps rather than code-point semantics by coincidence.
- **Modulo rather than bitwise parity:** `(x+y) % 2` works for positive and negative sums. A bit test `((x+y)&1)==0` would also work in Python but can be less immediately readable for signed values.
- **Validation omitted intentionally:** Indexing positions zero and one assumes two-character legal coordinates. The constraints prove that precondition, so defensive branches would not improve results on accepted inputs.
