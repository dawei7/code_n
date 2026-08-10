## General

**Understand what bit swaps preserve**

At each bit position, swapping bits between array elements preserves the total number of ones in that column. Across numbers from zero through $2^p-1$, exactly half have a one at each bit. Excluding zero does not remove any one bits, so each of the $p$ positions contains exactly $2^{p-1}$ ones across `nums`.

The operations can redistribute those column ones among array entries but cannot change these per-column totals. Every final number must remain nonzero because the objective asks for the minimum nonzero product.

Let

$$
M=2^p-1,
$$

the $p$-bit number containing all ones.

**Pair complementary values**

Among values one through $M-1$, pair each $x$ with $M-x$, which is its $p$-bit complement. Across a complementary pair, every bit position contains exactly one one.

By swapping corresponding bits inside the pair, those ones can be redistributed to make one number as small as possible without becoming zero: one. All remaining ones go into the other number, producing $M-1$.

For a pair whose bit totals contain one one in every column, the two numeric values sum to $M$. Among positive integer pairs with this fixed sum, the product is minimized at the most unequal allowed endpoints, $1$ and $M-1$.

There are

$$
q=2^{p-1}-1
$$

such pairs among the $M-1$ nonmaximum values. The all-ones value $M$ remains unpaired. A minimum arrangement therefore contains:

- one copy of $M$;
- $q$ copies of $1$;
- $q$ copies of $M-1$.

Its product is

$$
M(M-1)^q.
$$

The factors of one disappear, leaving exactly the formula computed by the source.

**Read the implementation**

`2**p - 1` is $M$, `2**p - 2` is $M-1$, and `2 ** (p - 1) - 1` is $q$.

Python's three-argument `pow(M - 1, q, mod)` computes the huge exponent modulo $10^9+7$ with repeated squaring. The remaining multiplication by $M$ is reduced by the final `% mod`.

The product is minimized before applying the modulus; modular arithmetic is used only to report that already-derived minimum.

**Why the construction is globally minimal**

For every complementary unit of per-column bit mass, keeping both resulting numbers positive forces at least value one in the smaller member. Moving any available higher bit from that smaller member to its partner makes the pair more unequal while preserving bit totals and does not increase its product. Repeating reaches $(1,M-1)$.

The all-ones value accounts for the extra one present in every bit column beyond the $q$ complementary pair contributions. Concentrating those extras together as $M$ is compatible with the original array and the swaps.

This yields a feasible arrangement and reaches the extreme product permitted by nonzero values and bit-column conservation, proving optimality.

**Small cases**

For $p=1$, $M=1$ and $q=0$. The modular power has exponent zero and equals one, so the result is one.

For $p=2$, $M=3$, $M-1=2$, and $q=1$. The formula gives $3\cdot2=6$.

For $p=3$, it gives $7\cdot6^3=1512$.

**Why the exponent is exactly `q`**

There are $M=2^p-1$ positive array entries. Reserve the single maximum entry $M$. That leaves $M-1=2^p-2$ entries, an even number, so they form

$$
\frac{2^p-2}{2}=2^{p-1}-1=q
$$

pairs. Every pair contributes one factor $M-1$ and one factor one. This count explains both the exponent and why there is exactly one unpaired maximum; it is not merely a pattern guessed from the examples.

## Complexity detail

The exponent $q$ has $O(p)$ bits. Modular exponentiation performs $O(p)$ squaring/multiplication steps, so time is $O(p)$ under fixed-modulus arithmetic. Computing the powers of two also uses integers with $O(p)$ bits.

Only a constant number of integer values are stored, so auxiliary space is $O(1)$ in the standard problem model.

## Alternatives and edge cases

- **Simulate bit swaps:** The conceptual array has $2^p-1$ elements and is impossibly large for $p=60$; the formula avoids constructing it.
- **Ordinary exponentiation then modulo:** It would create an astronomically large integer. Three-argument `pow` reduces after each step.
- **Modulo too early in the optimization:** The minimum must be chosen over actual products, not residues. The proof derives the true product first.
- **$p=1$:** Zero complementary pairs make the exponent zero, which `pow` handles correctly.
- **All-ones factor:** The maximum value appears once and multiplies the repeated $(M-1)$ factors.
- **Nonzero requirement:** It prevents concentrating all bits into fewer numbers while leaving zero entries, which would make product zero.
- **Bit-column conservation:** Swaps never move a bit between positions, only between elements at the same position.
- **Large $p$:** Runtime depends on $p$, not on the exponential number of conceptual array elements.
- **Prime modulus not needed for `pow`:** Repeated squaring works for this nonnegative exponent regardless; the given modulus simply bounds the result.
- **Factors of one:** They are part of the feasible optimal array even though they do not appear in the multiplication expression.
