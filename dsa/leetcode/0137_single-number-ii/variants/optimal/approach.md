## General

**Count each bit modulo three**

Ordinary XOR solves the version where every repeated value appears twice because XOR is addition modulo two at each bit. Here repeated values occur three times, so pairs do not cancel. The corresponding idea is to count ones at each bit position and keep the remainder modulo three.

Consider a fixed bit position `i`. Every tripled value contributes either:

- three zero bits, adding zero; or
- three one bits, adding three.

Both contributions are zero modulo three. The singleton contributes either zero or one at that position. Therefore:

$$
\left(\sum_{\texttt{num}\in\texttt{nums}}
\operatorname{bit}_i(\texttt{num})\right)\bmod 3
$$

is exactly bit `i` of the unique number.

The solution applies this reasoning independently to all 32 positions of the signed integer domain.

**Extract one position from every number**

For each `i` from zero through 31, the generator computes:

`num >> i & 1`

Right shift moves bit `i` into the least significant position. Bitwise AND with one clears every other position, leaving either zero or one. Parentheses are unnecessary because Python gives shifting higher precedence than bitwise AND in the intended grouping, but the expression means `(num >> i) & 1`.

`sum(...)` adds that bit over the whole array. If `cnt % 3` is zero, the singleton has zero at position `i`, so `ans` needs no change. If it is nonzero, the valid frequency guarantee means the remainder is exactly one and the singleton has that bit set.

For positions zero through 30, `ans |= 1 << i` places the bit into the answer. Left-shifting one creates a mask with only position `i` set, and OR preserves bits already reconstructed.

For `[2, 2, 3, 2]`, binary `2` contributes its bit pattern three times. At every position, those contributions vanish modulo three. The remaining remainders are the bits of `3`, so the result is three.

**Why the sign bit needs different reconstruction**

The constraints use signed 32-bit values from $-2^{31}$ through $2^{31}-1$. Position 31 is the sign bit in two’s-complement representation.

Python integers do not have a fixed 32-bit width. If the code handled position 31 with ordinary OR, it would construct the unsigned value having that high bit set, a positive integer at least $2^{31}$, rather than the required negative value.

Suppose the singleton’s lower 31 bits form the nonnegative value $L$ and its sign bit is one. Its unsigned 32-bit pattern has value:

$$
2^{31}+L.
$$

The signed value represented by the same pattern is:

$$
(2^{31}+L)-2^{32}=L-2^{31}.
$$

That is why the source uses `ans -= 1 << 31` for `i == 31`. At that moment, `ans` already equals $L$. Subtracting $2^{31}$ converts the reconstructed lower bits to the correct signed integer.

Python’s right shift of a negative number sign-extends with ones, which is consistent with two’s-complement bits at the 32 positions being examined. Applying `& 1` still extracts the desired position.

**Why the entire reconstructed value is exact**

For every one of the 32 positions, all tripled numbers contribute a multiple of three to `cnt`; taking the remainder removes them. The singleton alone determines whether that answer bit is zero or one.

The lower positions are placed independently, so no carry can contaminate another position. The special sign-bit conversion maps the final 32-bit pattern back into Python’s signed integer value. Since every allowed input fits in 32 signed bits, there are no unexamined value bits.

The algorithm never tries to identify which elements form triples. Their positions and order do not matter. It also does not modify `nums`.

**Why exactly 32 iterations are enough**

The loop bound is derived from the Reference’s numerical range, not an arbitrary optimization. Every allowed value has a complete signed representation in 32 bits. If the input domain allowed larger Python integers, the fixed loop would omit higher positions and could return a wrong answer; the width would need to be expanded or inferred under a defined signed representation.

## Complexity detail

Let $n$ be the array length.

The outer loop has exactly 32 iterations. Each iteration scans all $n$ numbers once, so work is $32n$, which is $O(n)$ because 32 is fixed by the contract.

The algorithm stores `ans`, `i`, `cnt`, and generator iteration state. It has no input-sized table, set, or counter, so auxiliary space is $O(1)$. The generator passed to `sum` yields one bit at a time rather than constructing a list.

If integer width were a variable $w$, the more general bound would be $O(wn)$ time. Here $w=32$ is constant, giving the manifest’s $O(n)$ time and $O(1)$ space.

## Alternatives and edge cases

- **Two-mask finite-state machine:** Maintain masks for bits seen once and twice modulo three. It processes all bit positions in parallel and also runs in $O(n)$ time and $O(1)$ space, but its Boolean transitions are less immediately intuitive.
- **Frequency dictionary:** Count complete integers and return the count-one key. It is linear expected time but requires $O(n)$ extra space.
- **Sort and scan triples:** Sorting makes equal values adjacent, but costs $O(n\log n)$ time and may mutate the input.
- **Set-and-sum formula:** `(3 * sum(set(nums)) - sum(nums)) // 2` derives the singleton algebraically, but the set violates constant space and fixed-width sums can overflow.
- **One element:** Its bits alone determine every remainder, so the same reconstruction returns it.
- **Singleton zero:** All position remainders are zero and `ans` remains zero.
- **Negative singleton:** The position-31 subtraction is necessary to return a negative Python integer instead of an unsigned 32-bit magnitude.
- **Negative repeated values:** Each sign-extended bit is still counted three times and vanishes modulo three.
- **Remainder two:** Valid input cannot leave remainder two at any bit because only the singleton survives and contributes at most one. The code treats any nonzero remainder as set, trusting the contract.
- **Runtime dependency:** The selected source uses `List` without importing it. A standalone module needs `from typing import List`.
