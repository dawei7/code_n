## General

**Separate fixed displacement from flexible moves.** Every `L` contributes one step left, or negative one. Every `R` contributes one step right, or positive one. Underscores can later be assigned either contribution.

Let $L$, $R$, and $B$ be the counts of `L`, `R`, and underscore respectively. Before choosing underscore directions, the fixed endpoint is

$$
R-L.
$$

Its distance from the origin is $|R-L|$.

**Send every flexible move away from the origin.** If the fixed endpoint is positive, choosing every underscore as right adds $B$ to its coordinate and therefore adds $B$ to its distance. If the fixed endpoint is negative, choosing every underscore as left subtracts $B$ from the coordinate and again adds $B$ to its absolute distance.

If the fixed endpoint is zero, either assigning every underscore left or assigning every underscore right reaches distance $B$.

Thus the maximum distance is

$$
|L-R|+B.
$$

The exact source computes that formula as `abs(moves.count("L") - moves.count("R")) + moves.count("_")`.

**Why mixing underscore directions cannot improve it.** Suppose $a$ underscores are assigned right and $B-a$ are assigned left. Their net displacement is $a-(B-a)=2a-B$, whose absolute magnitude is at most $B$. The final coordinate is fixed displacement plus that net flexible displacement.

By the triangle inequality,

$$
\left|(R-L)+(2a-B)\right|
\le |R-L|+|2a-B|
\le |R-L|+B.
$$

Assigning all flexible moves in the direction of the fixed displacement attains this upper bound. Therefore, the formula is not just plausible; it is provably optimal.

**The order of moves does not affect the final point.** Left and right steps add signed unit displacements. Addition is commutative, so only counts matter for the final coordinate. The problem asks for distance after all $n$ moves, not the farthest intermediate point, which is why sequence order can be discarded.

For `"L_RL__R"`, fixed left and right counts leave a net displacement toward the left. Directing every underscore left increases that magnitude and reaches the stated maximum distance.

**Why every underscore uses the same direction in an optimum.** Once the side farther from zero is chosen, an underscore sent the opposite way cancels one unit of progress. Reversing that choice adds two to the final coordinate in the desired direction: it removes one opposing step and adds one supporting step. Repeating this exchange transforms any mixed assignment into the all-aligned optimum.

**Three count calls rather than a literal one-pass loop.** The manifest and editorial call the approach one pass in an asymptotic sense. Python's `str.count` scans the string for each requested one-character substring. The exact expression calls it three times, so it performs three linear scans rather than one scan updating three counters.

Three is a constant, so time remains $O(n)$. A handwritten loop could collect all counts in one physical traversal, but it would not improve the asymptotic bound.

**The source does not construct a move assignment.** Only the maximum distance is required. The proof identifies a valid assignment—every underscore follows the fixed imbalance, or either direction on a tie—so existence is established without returning the chosen string.

**Sign does not matter to the output.** The expression uses `abs` because reaching coordinate negative five and positive five both gives distance five. Swapping every L and R in the input leaves the result unchanged.

## Complexity detail

Let $n$ be `len(moves)`. Each call to `moves.count(character)` scans the string in $O(n)$ time. There are three calls, so exact work is $3n$ character checks up to implementation constants, which is $O(n)$ time.

Only integer counts and the arithmetic result are used. `str.count` does not construct an occurrence list, so auxiliary space is $O(1)$.

The source's multiple scans remain linear, but a literal one-pass counter loop may have a smaller constant factor. Since $n\le50$, either is trivial in practice.

Reading the full input is necessary in the worst case because the final unseen character could change any of the three counts and hence the answer.

## Alternatives and edge cases

- **Literal single loop:** Maintain a signed fixed displacement and underscore count in one traversal, then return absolute displacement plus blanks. This performs one physical pass with the same bounds.
- **Try both extremes:** Compute final coordinate when all underscores are left and when all are right, then take the larger absolute value. These are the only extreme assignments needed and yield the same formula.
- **Enumerate underscore choices:** Testing all $2^B$ assignments is unnecessary because the triangle inequality proves an extreme assignment is optimal.
- **No underscores:** The answer is simply the absolute difference between fixed left and right counts.
- **Only underscores:** All can point the same way, so the answer is the string length.
- **Balanced fixed moves:** Fixed displacement is zero; either uniform underscore direction reaches distance $B$.
- **More left moves:** Assign all underscores left.
- **More right moves:** Assign all underscores right.
- **One underscore:** It always adds one to the maximum fixed distance, including a fixed tie.
- **Move order:** It would matter for a maximum intermediate distance question, but not for the final coordinate asked here.
- **Three physical scans:** The exact count-based expression is still $O(n)$ even though it is not a single traversal internally.
- **Input preservation:** Strings are immutable, and no modified movement string is built.
