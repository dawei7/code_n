## General

Binary addition at one bit has two separate outputs. XOR produces the result bit when carry is ignored, while AND identifies positions where both input bits are one and therefore generate a carry. Shifting that AND result left moves each carry into the next higher position.

The exact solution repeatedly replaces the current operands with

$$
\text{partial}=a\mathbin{\operatorname{XOR}}b
$$

and

$$
\text{carry}=(a\mathbin{\operatorname{AND}}b)\ll1.
$$

When no carry remains, the partial result is the complete sum. To make this work for negative Python integers, the source explicitly simulates a 32-bit two's-complement word with the mask `0xFFFFFFFF`.

**Why XOR is addition without carry.**

For one bit position, the four possibilities are:

```text
0 and 0 -> sum bit 0, carry 0
0 and 1 -> sum bit 1, carry 0
1 and 0 -> sum bit 1, carry 0
1 and 1 -> sum bit 0, carry 1
```

The sum-bit column is exactly XOR. The carry-generation column is exactly AND. A carry produced at bit position $p$ contributes to position $p+1$, explaining the left shift.

For example, adding binary `0101` and `0011` gives XOR `0110` and shifted AND `0010`. The original problem has become the same problem again: combine `0110` and `0010`. Their XOR is `0100` and their carry is `0100`; one more iteration yields `1000` with zero carry, which is decimal eight.

**The invariant across iterations.**

Within a fixed word width,

$$
a+b=(a\mathbin{\operatorname{XOR}}b)+((a\mathbin{\operatorname{AND}}b)\ll1).
$$

The two right-side terms separate bit contributions that do not carry from those that do. Therefore replacing `a` by the XOR and `b` by the shifted AND preserves the represented total modulo $2^{32}$.

Each iteration resolves the current carry positions and may create carries farther left. Because the word has only 32 bits and the carry is masked, carries eventually leave the top of the word and `b` becomes zero. At that moment `a ^ 0` would equal `a` and there is nothing left to propagate, so `a` is the 32-bit sum.

**Why Python needs an explicit mask.**

Languages with fixed-width signed integers naturally discard bits beyond their word size. Python integers have arbitrary precision, and negative values behave as though they have an unbounded sequence of leading one bits in bitwise operations. Without a width limit, carry propagation involving negative operands might never disappear.

The source first applies

```text
a &= 0xFFFFFFFF
b &= 0xFFFFFFFF
```

conceptually, through tuple assignment. `0xFFFFFFFF` has 32 one bits, so masking keeps only the low 32 bits. A negative input is thereby converted to its unsigned 32-bit two's-complement pattern. For example, `-1` becomes `0xFFFFFFFF`.

Every carry is also masked after shifting. Any carry out of bit 31 is discarded, exactly as it would be in 32-bit arithmetic. The partial XOR does not need another explicit mask because XOR of two already masked 32-bit nonnegative values cannot create a bit outside those 32 positions.

**One loop iteration in the source.**

While `b` is nonzero, the method computes

```text
carry = ((a & b) << 1) & 0xFFFFFFFF
a, b = a ^ b, carry
```

The tuple assignment evaluates both right-hand values from the old operands before replacing either variable. This is important: carry must be computed from the same old `a` and `b` used by XOR, not from an already-updated partial result.

After assignment, `a` holds the sum without the current carries and `b` holds exactly the carries still needing addition.

**A positive example.**

For `a = 1` and `b = 2`, their one bits do not overlap. AND is zero, so carry is zero immediately. XOR is three. The loop ends after one iteration and returns three.

For `a = 3` and `b = 1`, XOR first gives two while shifted AND gives two. Adding those produces zero without carry at the low positions and a carry into bit two, eventually yielding four. Repetition is what handles a chain such as `...0111 + 1`.

**How negative operands use the same loop.**

In two's complement, subtraction and sign are encoded in the bit pattern, so the same XOR-and-carry rule handles every sign combination. For instance, `-1` is 32 one bits. Combining it with `1` causes a carry to ripple left through all 32 positions. The final masked result is zero.

The local input bounds make the true sum lie well within signed 32-bit range, so modular 32-bit addition and ordinary mathematical addition agree on the intended result. The algorithm does not need separate positive, negative, or mixed-sign cases.

**Converting the unsigned word back to Python's integer.**

After the loop, `a` lies from `0` through `0xFFFFFFFF`. Values below `0x80000000` have sign bit zero and already equal their nonnegative Python interpretation, so they are returned directly.

Values at or above `0x80000000` have sign bit one and represent negative signed integers. The expression

```text
~(a ^ 0xFFFFFFFF)
```

converts them without `+` or `-`. XOR with the all-ones mask flips the 32 stored bits. Python's bitwise NOT then yields the corresponding negative number. For `a = 0xFFFFFFFF`, XOR gives zero and NOT gives `-1`; for `0x80000000`, XOR gives `0x7FFFFFFF` and NOT gives `-2147483648`.

**Why the returned result is correct.**

Masking maps both inputs to their 32-bit two's-complement representatives. Every iteration preserves their sum modulo $2^{32}$ while moving all unresolved carry into `b`. Termination at `b == 0` leaves the exact modular sum in `a`. The final sign conversion maps that word back to its signed Python integer. Because the promised mathematical sum does not overflow the signed 32-bit range, this signed interpretation is exactly `a + b` in ordinary arithmetic.

## Complexity detail

Let $w=32$ be the simulated word width. Carry can move only toward higher bit positions and is discarded beyond the word, so the loop performs at most $O(w)$ iterations. Each iteration uses a constant number of fixed-width bit operations. Time is $O(w)$, which is $O(1)$ for fixed 32-bit words.

Only scalar integers `a`, `b`, and `carry` are stored, so auxiliary space is $O(1)$. This matches the manifest.

Under arbitrary-precision bit-cost accounting, operations depend on word length, but the mask keeps every intermediate bounded to 32 bits. The fixed-width analysis is exact for this implementation.

## Alternatives and edge cases

- **Separate magnitude addition and subtraction:** Compare absolute values, use XOR/AND for same-sign addition, and XOR/borrow logic for mixed signs. This avoids a simulated signed word but creates more cases and may rely on forbidden arithmetic for sign handling.

- **Recursive carry propagation:** Return the XOR/carry transformation recursively until carry is zero. It expresses the identity neatly but uses call-stack space and is less robust than the loop.

- **Use a wider mask:** A 64-bit mask applies the same method to a 64-bit signed domain. The mask, sign threshold, and final conversion width must remain consistent.

- **One operand is zero:** The loop is skipped when masked `b` is zero, and masked `a` is converted directly to the proper signed result.

- **Both operands positive:** Carries behave like ordinary schoolbook binary addition; sign conversion returns the nonnegative word directly.

- **Opposite signs:** Two's-complement patterns make cancellation emerge from the same carry loop without an explicit borrow branch.

- **Both operands negative:** The sign bit and discarded overflow encode the negative sum correctly as long as the signed result stays in range.

- **Carry through many bits:** Values such as `7 + 1` require several iterations because the carry ripples across consecutive one bits.

- **Why masking carry matters:** Without it, a bit shifted beyond position 31 would remain in Python's unlimited integer and break the fixed-width termination and sign interpretation.

- **Signed overflow outside this contract:** General 32-bit addition wraps modulo $2^{32}$. The local constraints keep sums between `-2000` and `2000`, so no signed overflow ambiguity occurs.

- **Forbidden operators:** The solution never uses binary `+` or `-` to combine the inputs. Bit shifts, masks, XOR, AND, comparisons, and bitwise NOT implement the complete operation.
