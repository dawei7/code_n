## General

**Focus on the highest set bit of `n`.** Let:

$$
p=\lfloor\log_2 n\rfloor.
$$

Then:

$$
2^p\le n<2^{p+1}.
$$

Every integer from $2^p$ through $n$ has bit $p$ set to one. Therefore, the bitwise AND of any interval `[x,n]` lying entirely at or above $2^p$ must retain that bit and cannot be zero.

This immediately gives an upper bound on a valid `x`:

$$
x<2^p.
$$

The largest integer satisfying that inequality is $2^p-1$.

**Show that the upper bound is attainable.** Candidate:

$$
x=2^p-1
$$

has binary representation consisting of $p$ lower one bits:

`00...0011...11`.

The interval also contains $2^p$, whose representation has the high bit set and every lower bit zero:

`00...0100...00`.

The AND of these two numbers is already zero because they share no set bit. Adding the other interval numbers to an AND cannot turn a zero bit back on. Therefore, the AND of every number from $2^p-1$ through `n` is zero.

So $2^p-1$ is both valid and the largest possible valid value.

**Translate the proof into `bit_length`.** For positive `n`, `n.bit_length()` is the number of bits required to represent it, which equals $p+1$. The highest set-bit position is therefore:

`n.bit_length() - 1`.

The source computes its power of two with:

`1 << (n.bit_length() - 1)`

and subtracts one. Shifting one left by $p$ positions produces $2^p$, so the return expression is exactly the proven answer.

**A trace for `n=7`.** Binary seven is `111`, its bit length is three, and $p=2$. The source returns `(1 << 2) - 1 = 3`, binary `011`. The interval includes 3 and 4, whose bitwise AND is zero. Any `x >= 4` leaves highest bit two set throughout `[x,7]`, so no larger answer works.

For `n=9`, binary is `1001`, bit length four, and $p=3$. The result is seven, binary `0111`. The interval `[7,9]` includes eight, binary `1000`, which clears every lower bit when ANDed with seven.

For `n=17`, the highest power of two is 16 and the answer is 15. Again, 15 and 16 have disjoint set bits.

**Why examining every interval is unnecessary.** A naive approach could start from `n` and repeatedly extend the range leftward while maintaining an AND. In the worst case, a large number such as a power of two minus one would require walking down to the preceding boundary. The highest-bit proof jumps directly to the only possible maximal boundary.

**The interval includes both endpoints.** Validity relies on including $2^p-1$ and $2^p$. The reference defines `[x,n]` inclusively, and `n >= 2^p` guarantees the power of two is present.

**A formal maximality proof.** If `x > 2^p-1`, integer values force `x >= 2^p`. Every number between `x` and `n` is below $2^{p+1}$ and at least $2^p$, so each has bit $p$ equal to one. Their AND has that bit one and is nonzero. Thus no larger `x` is valid.

For `x=2^p-1`, the interval contains two numbers with disjoint bit sets, making the full AND zero. Necessary and sufficient sides meet at the same candidate.

## Complexity detail

Conceptually, finding the highest set bit examines $O(\log n)$ bits, matching the local manifest's time bound. Python implements `int.bit_length()` and shifting in low-level integer operations; their bit complexity is proportional to the number of machine words representing `n`.

The method stores only a few integer values implicit in one expression, so auxiliary space is $O(1)$ under the usual word-level model. The returned integer itself needs $O(\log n)$ bits, as does the input.

No loop, recursion, array, or string conversion is present in `solution.py`.

## Alternatives and edge cases

- **Repeated range AND:** Decrease `x` and maintain the cumulative AND until zero. Correct but can be far slower.
- **Loop to find highest power of two:** Repeatedly shift `n` right; it explicitly takes $O(\log n)$ time and reaches the same formula.
- **Use logarithms:** Floating-point `log2` can introduce precision issues for large integers; `bit_length` is exact.
- **`n = 1`:** Highest power is one and answer is zero; interval `[0,1]` has AND zero.
- **`n` a power of two:** Answer is `n - 1`, and the two endpoint bit patterns are disjoint.
- **`n = 2^{p+1}-1`:** Answer remains `2^p-1`; every larger start preserves bit $p$.
- **Maximum constraint:** Python handles $10^{15}$ exactly.
- **Inclusive interval:** Ensures the boundary power of two participates.
- **Highest-bit persistence:** It proves every larger candidate impossible.
- **Lower-bit clearing:** The all-ones predecessor and power of two share no one bits.
- **Positive input:** Guarantees `bit_length() - 1` is nonnegative.
- **Return may be zero:** The contract asks for an integer `x <= n` and does not require `x` positive.
- **No overflow:** Python shifts arbitrary-precision integers safely.
- **No mutation:** `n` is read once.
- **Direct formula:** It is not merely a shortcut; it follows from an exact attainable upper bound.
