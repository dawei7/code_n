## General

**Represent a ratio exactly**

Two rectangles are interchangeable when their fractions $w/h$ are equal. Using floating-point division as a dictionary key risks rounding concerns and is unnecessary.

The source reduces each fraction to lowest terms. It computes `g = gcd(w, h)` and replaces the dimensions with

`(w // g, h // g)`.

This pair is a canonical exact representation of the ratio.

For example, `(4,8)`, `(3,6)`, and `(10,20)` all reduce to `(1,2)`. Rectangles with unequal ratios reduce to different coprime pairs.

**Why gcd reduction is canonical**

Let $g=\gcd(w,h)$. Dividing both values by $g$ removes every common factor, so the resulting numerator and denominator are coprime.

If two positive fractions are equal, cross multiplication gives $w_1h_2=w_2h_1$. Their reduced coprime representations must have the same numerator and denominator. Conversely, identical reduced pairs clearly represent equal fractions.

Thus tuple equality is necessary and sufficient for ratio equality.

**Count pairs as each rectangle arrives**

`cnt[ratio]` stores how many earlier rectangles have the same reduced ratio. When the current rectangle belongs to a class with count $c$, it forms one new pair with each of those $c$ earlier occurrences.

The source adds `cnt[(w,h)]` to `ans` and then increments the count. Updating after the addition prevents pairing a rectangle with itself.

This online counting automatically enforces index order: every pair is counted when its later index is processed, so the earlier member is already in the counter.

**Trace one ratio class**

For four rectangles all reducing to `(1,2)`, the successive prior counts are zero, one, two, and three. The answer gains

$$
0+1+2+3=6,
$$

which equals $\binom{4}{2}$.

Different ratio classes are stored under different tuple keys and never contribute cross-class pairs.

**Why duplicates remain distinct**

Two identical dimension rows at different indices are distinct rectangles and form a valid pair. `Counter` records occurrences rather than unique input rows, so repeated rectangles contribute normally.

There is no need to store indices because only the number of pairs is requested.

**Why the online sum equals the complete answer**

Every addition pairs the current rectangle only with earlier rectangles of equal canonical ratio, so every counted pair is interchangeable and has distinct ordered indices.

Conversely, take any interchangeable pair $(i,j)$ with $i<j$. Their reduced tuples are equal. When the loop reaches $j$, rectangle $i$ is already included in that tuple's count, so this pair contributes exactly one. It cannot be counted at any other iteration because $j$ is its unique later endpoint.

Therefore `ans` counts all and only valid pairs.

**Connection to the combination formula**

If a final ratio class contains $c$ rectangles, it contributes $\binom{c}{2}=c(c-1)/2$ pairs. The online additions for that class are zero through $c-1$, whose sum is the same formula. The streaming version is therefore not a heuristic; it is an incremental evaluation of the exact group combination count. It also avoids a second pass over the counter and lets `ans` be finalized as soon as the input scan ends.

Each class accumulates independently, so summing these incremental contributions also equals the sum of the combination formula over all ratio classes.

**Avoiding overflow and precision**

The implementation never multiplies widths and heights for cross comparison and never forms a decimal ratio. It uses gcd and bounded integer division. Python would avoid fixed-width overflow anyway, but canonical tuples remain the cleanest hash key.

All widths and heights are positive, so the reduced denominator is positive and there is no need to normalize signs or handle division by zero.

## Complexity detail

Let $N$ be the number of rectangles and $M$ the largest dimension. Euclid's algorithm computes each gcd in $O(\log M)$ time. Counter access is expected $O(1)$, so total expected time is $O(N\log M)$.

At most $N$ distinct reduced ratios are stored, giving $O(N)$ space. Scalar reduced dimensions and the answer use constant additional space.

## Alternatives and edge cases

- **Floating-point ratio key:** Often works under small values but relies on representation details and is less exact than reduced integers.
- **Cross-multiply every rectangle pair:** Avoids floating point but takes $O(N^2)$ time.
- **Group then use combinations:** First count every reduced ratio, then sum $c(c-1)/2$; equivalent to the online method.
- **Identical rectangles:** Counted as interchangeable distinct occurrences.
- **Proportional but different sizes:** Gcd reduction maps them to one key.
- **Only one rectangle:** Its prior count is zero and the answer is zero.
- **All ratios distinct:** Every counter lookup contributes zero.
- **All ratios equal:** The result is $N(N-1)/2$.
- **Positive dimensions:** Guarantee a nonzero denominator and positive gcd.
- **Large pair count:** Python integers hold values beyond 32-bit range.
- **Update order:** Add the prior count before incrementing the current rectangle.
- **Input preservation:** Local `w` and `h` are reassigned, but rectangle rows are not modified.
- **Environment imports:** The exact source assumes `Counter` and `gcd` are available.
