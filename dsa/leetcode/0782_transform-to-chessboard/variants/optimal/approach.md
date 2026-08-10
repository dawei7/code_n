## General

**Identify what row and column swaps cannot change**

A chessboard has only two possible row patterns: an alternating row such as `0101` and its exact complement `1010`. Its columns have the same property.

Swapping columns rearranges every row in the same way. Therefore two rows that were identical remain identical, and two rows that were complements remain complements. A column swap cannot turn a third unrelated row pattern into one of the required two patterns.

The symmetric statement holds for columns under row swaps. Consequently a transformable board must already have:

- every row equal to the first row or its bitwise complement;
- every column equal to the first column or its bitwise complement;
- valid counts of the two row types and the two column types;
- valid zero/one counts within each line pattern.

These are invariants of the allowed operations, so an impossible board can be rejected before trying to count swaps.

**Encode one line as a bit mask**

The algorithm stores the first row in `rowMask` and the first column in `colMask`. Bit `i` records the value at index `i` of that line.

The low-`n`-bit mask `(1 << n) - 1` contains exactly `n` ones. XOR with it flips every board bit and no higher bit, so:

- `revRowMask = mask ^ rowMask` is the first row's complement;
- `revColMask = mask ^ colMask` is the first column's complement.

For every row `i` and column `i`, the nested loop builds `curRowMask` and `curColMask`. If either is neither its baseline nor its complement, no sequence of swaps can create a chessboard, and the method immediately returns `-1`.

At the same time, `sameRow` counts how many rows equal `rowMask`, and `sameCol` counts how many columns equal `colMask`.

**Why line-type quantities must be balanced**

An alternating sequence of even length has exactly half of one type and half of the other. Thus, when `n` is even, the two complementary row patterns must each occur `n / 2` times, and so must the two column patterns.

For odd `n`, an alternating sequence begins and ends with the same type. One type occurs `(n + 1) / 2` times and the other occurs `n / 2` times. Either pattern may be the majority, but their counts must differ by exactly one.

The helper `f(mask, cnt)` checks both necessary balances:

- `ones = mask.bit_count()` measures the number of one bits inside the baseline line.
- `cnt` measures how many complete rows or columns use that baseline line rather than its complement.

For odd `n`, `abs(n - 2 * value) == 1` means the value is either floor or ceiling of half. For even `n`, both values must equal `n // 2`.

The first measure validates the pattern distribution along one dimension; the second validates how many complementary lines occur along the other dimension.

**Reduce the remaining work to alternating a binary sequence**

Once every row and column has one of the two allowed complementary patterns, the two dimensions can be fixed independently.

Reordering columns determines whether the bits of `rowMask` alternate. It does not change which complete rows equal `rowMask`. Reordering rows determines whether `colMask` alternates. Row and column swaps commute with respect to their final grid positions, so the minimum total is:

$$
\text{minimum column swaps} + \text{minimum row swaps}.
$$

The call `f(rowMask, sameRow)` calculates the first quantity while validating both associated balances. The call `f(colMask, sameCol)` calculates the second.

**Understand the alternating-position masks**

With bit zero representing index zero:

- `0x55555555` has one bits at even indices `0, 2, 4, ...`.
- `0xAAAAAAAA` has one bits at odd indices `1, 3, 5, ...`.

The constraint `n <= 30` means these constants cover every used bit.

Intersecting a line mask with one of these constants and calling `bit_count()` tells how many one bits are already in the desired parity of positions.

**Count swaps when `n` is odd**

For odd length, only one alternating orientation fits a given number of ones.

If `ones == n // 2`, ones are the minority and must occupy all odd indices, while the sequence starts and ends with zero. There are `n // 2` required odd-position ones. The number not already correct is:

`n // 2 - (mask & 0xAAAAAAAA).bit_count()`.

Every misplaced one lies at an even index, and there is an equally misplaced zero at an odd index. Swapping those two positions fixes both, so the number of missing correct-position ones equals the required number of swaps.

Otherwise the ones are the majority, numbering `(n + 1) // 2`, and must occupy even indices. The corresponding count is:

`(n + 1) // 2 - (mask & 0x55555555).bit_count()`.

There is no second orientation to compare because an odd alternating sequence's starting bit determines which value appears one extra time.

**Count swaps when `n` is even**

An even alternating sequence contains exactly half ones in either orientation. Both `0101...` and `1010...` are possible targets.

`cnt0` measures swaps needed to place ones at odd indices. `cnt1` measures swaps needed to place ones at even indices. The helper returns `min(cnt0, cnt1)` because the board may use whichever valid chessboard orientation requires fewer swaps.

Again, each swap exchanges one misplaced one with one misplaced zero. Counting missing correctly positioned ones already gives the number of swaps; dividing by two again would undercount.

**Trace the already valid two-by-two board**

For `[[0,1],[1,0]]`, the first row mask is `10` in index-bit notation and its complement is `01`. The two rows occur once each, as do the two columns.

Each baseline mask already alternates in one of the allowed orientations, so both helper calls return zero. Their sum is zero.

**Why passing all checks and applying the counts is sufficient**

The pattern checks guarantee that the board consists only of two complementary row types and two complementary column types. The balance checks guarantee those types can occupy alternating positions. The helper counts exactly the minimum exchanges needed to place the baseline and complementary types into such positions.

After the chosen row and column reorderings, adjacent rows use opposite patterns and adjacent columns use opposite bits. Hence every horizontal and vertical neighbor differs, which is precisely a chessboard. The conditions are therefore sufficient as well as necessary.

## Complexity detail

Let $n$ be the board dimension. Constructing the initial masks costs $O(n)$. Building every current row and column mask examines all $n^2$ cells, which dominates the running time. The helper uses a constant number of bit operations, so total time is $O(n^2)$.

The algorithm stores a constant number of `n`-bit integers. Counting their bit width, this is $O(n)$ auxiliary space, matching the package requirement. It does not create copies of all rows or columns.

## Alternatives and edge cases

- **Tuple counters for rows and columns:** Count complete line tuples, verify two complementary patterns, then count mismatches. It is conceptually direct but stores $O(n^2)$ tuple data unless carefully shared.

- **Try row and column permutations:** There are $n!$ possibilities per dimension, far beyond the limit and unnecessary once the invariants are known.

- **Even dimension:** Both alternating starting bits are possible, so take the smaller of two swap counts.

- **Odd dimension:** The majority bit fixes the only possible starting orientation.

- **Third row or column pattern:** It violates an invariant that swaps cannot repair, so return `-1` immediately.

- **Complementary patterns with wrong quantities:** They cannot alternate across the entire dimension, so the helper returns `-1`.

- **Wrong number of ones in a baseline:** No permutation changes a line's zero/one count, making a chessboard impossible.

- **Already a chessboard:** Correct-position counts equal their required totals, producing zero swaps.

- **Swap counting:** Count misplaced ones on their required parity; each actual swap fixes one such one and one corresponding zero.
