## General

**Start from an upper bound**

For any element $x$, the largest contribution obtainable from its magnitude is $\lvert x\rvert$. Therefore no final matrix can have sum greater than

$$
S=\sum \lvert x\rvert.
$$

If all nonzero entries can be made positive, this upper bound is attainable. The problem is thus not about deciding a separate desired value for every cell; it is about understanding which sign patterns the pair-flip operation can reach.

The source computes `s` as this absolute-value sum. At the same time, it counts initially negative entries in `cnt` and tracks the smallest magnitude in `mi`.

**Understand what one operation changes**

An operation flips the signs at the two endpoints of one grid edge. Imagine recording, for every cell, whether it is flipped an odd or even number of times. Even flips cancel, so only the odd-flipped set determines the final signs.

Every operation toggles exactly two cells. Consequently, the number of cells flipped an odd number of times must be even. Conversely, because the grid is connected, any chosen even-sized set of cells can be toggled: pair its vertices, connect each pair by a grid path, and apply the operation along every edge of that path. Internal path vertices are touched twice and cancel, while the two endpoints are touched once.

This reachability fact is why adjacency does not force a more complicated local greedy strategy. Adjacency restricts individual operations, but paths let sign changes be transported across the connected matrix.

**When the negative count is even**

If `cnt` is even, choose all initially negative cells as the odd-flipped set. Its size is even, so the connected-grid argument says this transformation is reachable. Every negative becomes positive, and every initially nonnegative entry can retain its sign.

The resulting sum is exactly `s`, the absolute-value upper bound. Since no arrangement can exceed that bound, this result is optimal. The source returns `s` when `cnt % 2 == 0`.

**When the negative count is odd and there is no zero**

If all magnitudes are positive, flipping a cell changes whether it is negative. Because only an even number of cells can be toggled overall, the parity of the number of negative cells cannot change. Starting with an odd count means every reachable final state still has an odd count, so at least one entry must remain negative.

To maximize the total, make every other entry positive and assign the unavoidable negative sign to a cell with the smallest absolute value `mi`. Relative to the ideal absolute sum, that entry contributes `-mi` instead of `+mi`. The loss is therefore

$$
(+\texttt{mi})-(-\texttt{mi})=2\texttt{mi}.
$$

The best achievable sum is `s - 2 * mi`. The source expresses exactly this as `s - mi * 2`.

It does not matter whether the minimum-magnitude cell was initially positive or negative. The reachability argument allows the final odd negative sign to be located there while appropriate path operations fix the other signs.

**Why zero removes the penalty**

Zero is a special but naturally handled case. Multiplying zero by negative one still gives zero, so "flipping its sign" has no effect on the matrix value. If the initial negative count is odd, include one zero along with all negative cells in the even-sized set of operation endpoints. All nonzero negatives become positive, while zero remains zero.

In the arithmetic, a present zero makes `mi = 0`. The odd-count branch subtracts `2 * 0` and returns `s`. Thus the compact formula handles the zero case without an explicit condition.

**Read the exact scan**

The nested loops visit every row and every value `x`. In Python, the Boolean result of `x < 0` behaves as integer one for true and zero for false, so

`cnt += x < 0`

increments the count exactly for negative entries.

The source assigns `y = abs(x)` once, then uses it both to update `mi` and to add to `s`. Initializing `mi` to positive infinity guarantees that the first real magnitude replaces it. The matrix is nonempty under the constraints, so `mi` is finite before the return.

**A concrete example**

Suppose the magnitudes are 1, 2, 3, and 4, with three negative entries. The ideal sum is 10, but with no zero an odd negative sign must remain. Leaving magnitude one negative gives

$$
-1+2+3+4=8,
$$

which is `10 - 2 * 1`. Leaving magnitude four negative would instead produce two, so the minimum magnitude is the only optimal place for the unavoidable loss.

If the values include zero, the same odd negative count can be cleared while zero absorbs the parity adjustment, and the full absolute sum is reachable.

**Why the formula proves both possibility and optimality**

For even negative count or a zero, the construction reaches the absolute-sum upper bound. For odd negative count without zero, parity proves that some positive magnitude must carry a negative sign, so every result loses at least twice the smallest magnitude from that upper bound. Connectivity makes a state achieving exactly that loss reachable.

The formula therefore has both halves required for a correctness proof: no answer can be larger, and the stated answer can actually be produced using legal adjacent operations.

## Complexity detail

Let $M$ be the total number of matrix elements. For the required square matrix, $M=n^2$. The nested loops process each value once with constant work, giving $O(M)$ time, equivalently $O(n^2)$.

The variables `mi`, `s`, `cnt`, `x`, and `y` occupy constant auxiliary storage, so space is $O(1)$. The proof uses conceptual paths but the implementation never constructs or simulates them. It also does not modify `matrix`.

## Alternatives and edge cases

- **Simulate adjacent flips greedily:** Local choices are difficult to coordinate and do unnecessary work; the parity invariant determines the answer directly.
- **Search over sign configurations:** There are exponentially many patterns, while only the negative-count parity and minimum magnitude matter.
- **Explicitly construct operations:** This can demonstrate reachability using paths, but the problem requests only the maximum sum, not an operation sequence.
- **Even negative count:** Every negative sign can be removed, so return the full sum of absolute values.
- **Odd negative count without zero:** One negative is unavoidable; place it on the smallest magnitude.
- **Odd negative count with zero:** Zero absorbs the parity adjustment, and subtracting twice the minimum subtracts zero.
- **All entries positive:** The negative count is zero and the matrix already attains the upper bound.
- **All entries negative:** Only the parity of the number of cells decides whether one magnitude must remain negative.
- **Several equal minimum magnitudes:** Any one can carry the unavoidable negative sign; the maximum sum is unchanged.
- **Value already zero:** It is not counted as negative because `0 < 0` is false.
- **Large magnitudes and matrix size:** Python integers hold the total exactly without fixed-width overflow.
- **Connectedness is essential to the proof:** A rectangular grid linked by shared borders is connected, so path operations can realize every even endpoint set.
- **Diagonal cells:** They are not directly adjacent, but a border-connected path can still transfer flips between them.
- **Input side effects:** The exact method reads the matrix only and returns a number without changing any entry.
