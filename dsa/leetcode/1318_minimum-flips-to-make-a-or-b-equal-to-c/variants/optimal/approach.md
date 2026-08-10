## General

Bitwise OR operates independently at every bit position. Flipping one bit of `a` or `b` affects only that position, so the global minimum is the sum of independent per-bit minimums.

The exact solution inspects 32 positions. At position `i`:

`x = a >> i & 1`, `y = b >> i & 1`, and `z = c >> i & 1`.

Right shift moves the desired bit into the least-significant position, and AND with one discards every other bit.

**When the target bit is zero**

If `z == 0`, the OR result must be zero. OR is zero only when both input bits are zero.

Each current one must therefore be flipped independently:

- `x = 0, y = 0` needs zero flips;
- exactly one of `x` and `y` is one, so one flip is needed;
- both are one, so both must change and two flips are needed.

Because `x` and `y` are each zero or one, `x + y` is exactly that required count. This explains the expression `x + y if z == 0`.

**When the target bit is one**

If `z == 1`, the OR result needs at least one input one.

If either `x` or `y` is already one, the condition is satisfied and no flip is needed. If both are zero, one of them must be flipped to one. Flipping both would be unnecessary.

`int(x == 0 and y == 0)` converts this Boolean condition to one when both are zero and zero otherwise.

**Adding independent costs**

`ans` accumulates the required contribution for all positions. A choice made at one bit cannot help or hurt another bit, so choosing the local minimum at every position produces a globally minimum total.

For `a = 2`, `b = 6`, and `c = 5`:

- at bit zero, input bits are zero and zero while the target is one, costing one;
- at bit one, input bits are one and one while the target is zero, costing two;
- at bit two, input bits are zero and one while the target is one, costing zero.

All higher relevant bits are zero. The total is three.

**Why 32 iterations are sufficient**

The inputs are positive and at most $10^9$, which fits within 30 binary value bits and certainly within 32. Bits above their highest set positions are all zero in all three numbers and contribute nothing.

The fixed loop avoids mutating the input numbers. A generalized arbitrary-precision version should loop until the shifted values are all zero or use the maximum bit length rather than assuming 32 positions.

**Why the answer is minimum**

At each bit, the OR truth table gives the exact necessary changes described above. Any valid final pair must pay at least that local cost. The algorithm exhibits a way to achieve it by flipping precisely the offending ones for target zero or one arbitrary input zero when both are zero for target one.

Since bit positions do not interact, these locally achievable minima can all be applied together. Their sum is both a lower bound and achievable, proving optimality.

## Complexity detail

The exact code always performs 32 iterations with constant work, so under the stated bounded integer type its running time is $O(1)$ and auxiliary space is $O(1)$.

If $M = \max(a,b,c)$ and bit width is treated as variable, only $O(\log M)$ positions are relevant. The manifest expresses this generalized time as $O(\log M)$.

No arrays, strings, or recursion are used. `ans` and the three extracted bits are constant storage.

Python integers are unbounded, but the input constraint makes the fixed 32-bit scan sufficient. For values beyond 32 bits outside the contract, the exact code could miss necessary flips.

## Alternatives and edge cases

- **Shift values in a while loop:** Repeatedly inspect `a & 1`, `b & 1`, and `c & 1` and right-shift until all become zero. It naturally adapts to bit length but mutates local copies.
- **Population-count formula:** Count set bits in `(a | b) ^ c`, then add another count for positions where both `a` and `b` are one but `c` is zero. It is concise but less transparent.
- **Target zero with two ones:** This is the only per-bit case requiring two flips; one remaining one would keep OR equal to one.
- **Target one with two zeros:** Exactly one flip is enough; the algorithm must not count two.
- **Already matching OR:** Every position contributes zero, so the answer is zero.
- **Higher zero bits:** They add nothing because `x = y = z = 0`.
- **32-bit assumption:** It is safe for values at most $10^9$ but not for unrestricted Python integers.
- **Operator precedence:** The exact expressions rely on shifts and bitwise AND producing the selected bit; parentheses can make `(a >> i) & 1` easier to read.
- **Flips apply only to `a` and `b`:** `c` is a fixed target, and the algorithm never changes it.
- **Independence:** There are no carries in bitwise OR, unlike addition, so per-position optimization is valid.
