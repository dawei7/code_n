## General

Complementing a positive integer means flipping only the bits in its ordinary binary representation, from the highest `1` down to the least significant bit. Infinite or fixed-width leading zeros are not part of that representation and must not be flipped.

The exact solution builds a mask containing one `1` for every meaningful bit of `num`, then XORs the mask with `num`. XOR with one flips a bit, so the operation complements exactly the intended width.

**Find the meaningful width**

`num.bit_length()` returns the number of bits required to represent positive `num` without leading zeros. For example:

- `1` is binary `1`, so its bit length is one.
- `5` is binary `101`, so its bit length is three.
- `8` is binary `1000`, so its bit length is four.

Let this width be `b`. The highest meaningful position is `b - 1`, and positions at `b` or above are implicit leading zeros that must remain outside the operation.

The contract guarantees `num >= 1`, so `b` is always positive. Python defines `0.bit_length()` as zero, but the exact source does not need a separate zero policy for this problem.

**Construct `b` one-bits**

The expression `1 << b` shifts a single one left by `b` positions, creating the binary pattern `1` followed by `b` zeros. Subtracting one borrows through those zeros and produces exactly `b` trailing ones:

$$
(1\ll b)-1=\underbrace{11\ldots1}_{b\text{ bits}}.
$$

For `b = 3`, `1 << 3` is binary `1000`, and subtracting one gives `111`.

This is the exact width mask needed for `num`.

**Why XOR performs the complement**

For one bit `x`, XOR has these relevant identities:

$$
x\oplus1=1-x,
\qquad
x\oplus0=x.
$$

Every meaningful bit is aligned with a mask bit of one, so it flips. Every higher position is aligned with mask zero, so it stays zero and creates no unwanted leading ones.

The returned expression is therefore

`num ^ ((1 << num.bit_length()) - 1)`.

**Trace `num = 5`**

`5` is binary `101`, so `bit_length()` is three. The mask is `(1 << 3) - 1 = 111` in binary. XOR gives

```text
101
111
---
010
```

Binary `010` represents decimal two, which is the expected complement.

For `num = 1`, width is one, the mask is `1`, and `1 XOR 1 = 0`.

For a power of two such as `8 = 1000`, the four-bit mask is `1111`; XOR yields `0111`, or seven. This illustrates why the mask must extend through the original highest one-bit: every zero below it becomes one.

**An equivalent subtraction identity**

Within a `b`-bit width, the all-ones mask has numerical value $2^b-1$. Complementary numbers add to that mask because each bit pair is one and zero. Therefore the result also equals

$$
(2^b-1)-\texttt{num}.
$$

XOR expresses the bit-flipping intention more directly, while subtraction provides another way to verify the answer.

**Why Python's ordinary `~num` is not enough**

Python models signed integers with an unbounded two's-complement-style bitwise behavior. `~num` is mathematically `-num - 1`, which flips conceptual leading zeros into leading ones and produces a negative number. Masking is required to restrict inversion to the no-leading-zero representation specified by the problem.

## Complexity detail

Let $b=\lfloor\log_2(\texttt{num})\rfloor+1$ be the bit length. At the arbitrary-precision bit-operation level, determining bit length, constructing the mask, and applying XOR require $O(b)=O(\log\texttt{num})$ bit work. This matches the manifest.

The input is below $2^{31}$, so `b` is at most 31. Under the customary fixed-width machine model, all operations are constant time and the algorithm is also described as $O(1)$.

Only the mask and result integers are needed. Under the fixed-width constraint, auxiliary space is $O(1)$. In an arbitrary-precision bit model, representing the mask uses $O(b)$ bits, which is still proportional only to the input representation.

## Alternatives and edge cases

- **Flip one bit at a time:** Walk through `num`'s bits with a shifting one-bit mask. It is correct but uses a loop instead of one same-width XOR.
- **Propagate the highest bit downward:** Repeated OR-with-shift operations turn every lower position into one, then XOR. This avoids `bit_length` but is more verbose.
- **Use `~num` directly:** Incorrect in Python because it flips unbounded leading sign bits and returns a negative value.
- **Subtract from the mask:** `(1 << b) - 1 - num` is algebraically equivalent to XOR for this all-ones width.
- **`num = 1`:** The one meaningful bit flips to zero.
- **Power of two:** The leading one becomes zero and every lower zero becomes one, yielding one less than the original number.
- **All bits already one:** A value such as `7 = 111` complements to zero.
- **Leading zeros:** They are intentionally excluded by `bit_length`; complementing a fixed 32-bit width would solve a different problem.
- **Zero outside the contract:** A separate definition would be needed because its ordinary representation policy varies by problem; this source guarantees positive input.
- **Why XOR stays within the intended width:** The mask contains zeros above the highest meaningful bit, so XOR leaves every higher position zero while toggling precisely the represented binary digits.
