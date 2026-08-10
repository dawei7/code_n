## General

**Chessboard colors alternate with coordinate parity**

Square `a1` is black. Moving one file horizontally, such as from `a1` to `b1`, changes the color. Moving one rank vertically, such as from `a1` to `a2`, also changes the color.

Therefore color depends only on whether the total number of one-step moves from `a1` is even or odd. An even number of color toggles returns to black; an odd number reaches white.

If files `a` through `h` are numbered 1 through 8 and ranks already use 1 through 8, a square is white exactly when the file number and rank number have opposite parity. Their sum is then odd.

**Use character-code parity without explicit conversion**

The protected solution computes

`ord(coordinates[0]) + ord(coordinates[1])`

and checks whether the sum is odd.

This works because consecutive file letters have consecutive character codes, so moving one file changes code parity. Consecutive digit characters also have consecutive codes, so moving one rank changes parity.

The absolute starting codes do not matter as long as their combined parity agrees with `a1`. In ASCII and Unicode code points used by Python:

- `ord('a') = 97`, which is odd;
- `ord('1') = 49`, which is odd;
- their sum 146 is even.

Thus even code sum corresponds to black at `a1`. Every single horizontal or vertical step changes one code by one and flips the sum parity, exactly matching the board's color alternation. Odd sum therefore means white.

**Following the examples**

For `"a1"`, code sum is `97 + 49 = 146`, which is even. The expression comparing remainder to one returns `false`, correctly identifying black.

For `"h3"`, `ord('h') = 104` and `ord('3') = 51`. Their sum is 155, which is odd, so the method returns `true` for white.

For `"c7"`, the codes are 99 and 55. Their sum 154 is even, so the square is black and the result is `false`.

**Equivalent normalized-coordinate reasoning**

One could calculate zero-based coordinates

$$
x=\operatorname{ord}(\texttt{file})-\operatorname{ord}(\texttt{'a'})
$$

and

$$
y=\operatorname{ord}(\texttt{rank})-\operatorname{ord}(\texttt{'1'}).
$$

Then `a1` is $(0,0)$ and white squares satisfy $(x+y)\bmod2=1$.

The exact solution omits the subtractions because their combined value `ord('a') + ord('1')` is even. Subtracting an even constant cannot change parity:

$$
(A-B)\bmod2=A\bmod2
$$

when $B$ is even. The shorter code is therefore mathematically identical.

**Why parity completely determines the color**

Any path from `a1` to the requested square requires a fixed horizontal displacement plus a fixed vertical displacement. Alternative routes may add pairs of opposite moves, changing path length by an even number and leaving parity unchanged.

Each step toggles color. Consequently, only the parity of total displacement matters, and the character-code sum captures it. There is no need to store an eight-by-eight board or list white squares.

**Why the return condition uses equality to one**

Modulo two yields either zero or one for the nonnegative code sum. Remainder one means odd and therefore white. The Boolean comparison directly returns the required type; no conditional statement is needed.

**Input guarantees used by the method**

The coordinate always has exactly two characters, file first and rank second. Both ranges are consecutive character sequences. Those guarantees make direct indexing safe and ensure character-code parity tracks board movement.

If multi-digit ranks or arbitrary notation were allowed, this exact two-character calculation would not generalize without parsing.

## Complexity detail

The method reads two fixed characters, performs two code conversions, one addition, one modulo, and one comparison. Its work is independent of board size and input beyond the fixed valid format, so time complexity is $O(1)$.

It creates no collection and stores only constant-size intermediate integers. Auxiliary space is $O(1)$. Both bounds match the manifest.

## Alternatives and edge cases

- **Normalize file and rank indices:** Subtract `'a'` and `'1'`, then test the parity of their sum. It is equally correct but slightly more verbose.
- **Hard-coded board matrix:** It uses unnecessary storage and is more error-prone than the alternating-color invariant.
- **Set of white coordinates:** Membership would be constant time but requires listing 32 squares manually.
- **Compare coordinate parities:** White squares have one odd and one even normalized coordinate; this is another form of the same test.
- **`a1` anchor:** Its even code sum must map to black, fixing which parity means which color.
- **Horizontal move:** Incrementing the file letter flips parity and color.
- **Vertical move:** Incrementing the rank digit also flips parity and color.
- **Diagonal move:** Changing both coordinates flips parity twice, so the color stays the same.
- **Corner `h8`:** Both coordinates are seven steps from `a1`; 14 toggles preserve black.
- **Valid-range guarantee:** No bounds check is needed for files or ranks.
- **Length-two guarantee:** Direct access to positions zero and one is safe.
- **Case sensitivity:** Files are guaranteed lowercase; uppercase codes would require rechecking the anchor parity and validity.
- **No parsing:** Rank is a single digit from one through eight, so its character-code parity equals its numerical parity up to a fixed odd offset.
- **Boolean result:** The comparison already yields `True` for white and `False` for black.
