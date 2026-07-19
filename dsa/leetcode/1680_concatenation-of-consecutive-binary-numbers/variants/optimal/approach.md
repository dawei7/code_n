## General
**Translate concatenation into a shift and append recurrence**

Suppose the already concatenated prefix has residue $A$ and the current integer $i$ occupies $ell(i)$ binary digits. Appending those digits shifts the prefix left by $ell(i)$ positions and fills the new low bits with $i$:

$$
A' = \left(A \cdot 2^{\ell(i)} + i\right) \bmod M.
$$

Because $i < 2^{\ell(i)}$, bitwise OR and addition are equivalent after the shift. Applying the modulus after every append is safe: replacing $A$ by a congruent residue does not change the next expression modulo $M$. This keeps the working value bounded even though the conceptual integer grows rapidly.

**Increase the width only at powers of two**

Binary length stays constant between consecutive powers of two. Maintain a `bit_length` counter starting at zero. An integer `i` is a power of two exactly when `i & (i - 1) == 0`; at those values, increment the counter before appending `i`. The loop therefore avoids recomputing a logarithm or constructing a binary string.

After processing $i$, the maintained residue equals the integer represented by the concatenation from $1$ through $i$, modulo $M$. The base case appends the one-bit representation of $1$. For the inductive step, the recurrence shifts the prior concatenation by exactly the width of $i$ and places precisely the bits of $i$ in the vacated suffix. Modular reduction preserves the residue of that exact concatenation. Thus the value after processing `n` is the requested result.

## Complexity detail
The loop performs constant work for each of the $n$ integers, so it takes $O(n)$ time under fixed-width modular arithmetic. It stores only the residue, current bit length, loop value, and modulus, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Build the complete binary string:** direct concatenation mirrors the definition but stores $\Theta(n \log n)$ bits and requires converting an enormous integer.
- **Process every bit separately:** updating the residue once per binary digit is correct but takes $O(n \log n)$ time over all representations.
- **Use `bit_length()` for every integer:** this remains $O(n)$ in languages where the primitive is constant time and is a clear alternative to power-of-two tracking.
- **Power-of-two boundaries:** the width must increase before appending `2`, `4`, `8`, and every later power of two.
- **Modulo timing:** reducing only after constructing the full value can overflow fixed-width types; reducing after each recurrence is mathematically equivalent.
- **Minimum input:** for `n = 1`, the sole representation is `"1"`, so the answer is one.
