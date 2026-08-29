## General

The exponent may have as many as 2000 decimal digits, so converting it to an ordinary fixed-width integer is not a reliable approach. The exact solution processes the exponent one decimal digit at a time while keeping every intermediate value reduced modulo `1337`.

Unlike the manifest summary's most-significant-digit recurrence, the source scans a reversed copy of `b`, from the least significant digit to the most significant. It maintains a modular base corresponding to the current decimal place: first $a^{10^0}$, then $a^{10^1}$, then $a^{10^2}$, and so on.

**Expand the decimal exponent by place value.**

If the exponent digits are

$$
[e_{d-1},e_{d-2},\ldots,e_1,e_0],
$$

where $e_0$ is the last array element, then the represented exponent is

$$
B=e_0\cdot10^0+e_1\cdot10^1+\cdots+e_{d-1}\cdot10^{d-1}.
$$

Exponent rules give

$$
a^B
=a^{e_0\cdot10^0}
 a^{e_1\cdot10^1}
 \cdots
 a^{e_{d-1}\cdot10^{d-1}}.
$$

This product lets the algorithm handle each digit independently. A digit never exceeds nine, and the base for its place can be advanced by raising the previous place base to the tenth power.

**Why modular reduction can happen after every operation.**

For modulus $M=1337$,

$$
(x\bmod M)(y\bmod M)\bmod M=(xy)\bmod M.
$$

Likewise, replacing a base by its remainder does not change the remainder of any nonnegative power. The method may therefore reduce every digit contribution and every place-value base immediately. Intermediate numbers stay below the modulus instead of growing to thousands of digits.

**Meaning of the two changing variables.**

Let the original input base be $A$. Before processing decimal place $p$:

- `ans` is congruent to $A$ raised to the value contributed by the already processed lower $p$ digits.
- the current variable `a` is congruent to $A^{10^p}$ modulo `1337`.

Initially no exponent digits have contributed, so `ans = 1`, the multiplicative identity. The current base is $A=A^{10^0}$, satisfying the invariant for place zero.

**Processing one reversed digit.**

For the current digit `e`, `pow(a, e, mod)` computes

$$
(A^{10^p})^e\bmod1337
=A^{e\cdot10^p}\bmod1337.
$$

Multiplying this contribution into `ans` incorporates exactly the current decimal place. The expression applies `% mod` again so `ans` remains a small residue.

Next, `a = pow(a, 10, mod)` changes the place base from

$$
A^{10^p}
$$

to

$$
(A^{10^p})^{10}=A^{10^{p+1}},
$$

ready for the next digit to the left.

Python's three-argument `pow(base, exponent, modulus)` performs modular exponentiation directly. It does not first construct the enormous unreduced power. Here the digit exponent is at most nine and the place update exponent is always ten, so each call performs only a small fixed amount of modular work.

**A trace for exponent `[1, 0]`.**

The decimal exponent is ten. Reversing the digits yields `0`, then `1`.

- Start with `ans = 1` and current base $A$.
- Digit zero contributes $A^0=1$, so `ans` stays one. The base advances to $A^{10}$ modulo 1337.
- Digit one contributes $(A^{10})^1$, so `ans` becomes $A^{10}\bmod1337$.

For `a = 2`, the result is `1024`, which is already below 1337.

**A larger conceptual trace.**

For digits `[3, 4, 2]`, the exponent is $342=2\cdot1+4\cdot10+3\cdot100$. The reversed loop multiplies residues for $A^2$, then $A^{40}$, then $A^{300}$. Their product is $A^{342}$, and modular reduction preserves its remainder.

**Why the loop invariant proves correctness.**

Assume before one iteration that `ans` contains all processed lower-place contributions and `a` represents $A^{10^p}$. Multiplying by `pow(a, e, mod)` adds exponent $e\cdot10^p$ to the accumulated exponent. Raising `a` to ten advances its represented exponent to $10^{p+1}$. Both statements remain true modulo 1337 because modular multiplication and exponentiation preserve congruence.

After all digits are processed, the accumulated exponent is exactly the decimal value represented by `b`. Therefore `ans` is congruent to $A^B$ modulo 1337 and already lies in the canonical remainder range, so it is the required answer.

Digit zero requires no special branch. `pow(a, 0, mod)` returns one, contributing nothing to the exponent while the place base still advances. Base value one also naturally leaves `ans` equal to one.

## Complexity detail

Let $d$ be the number of exponent digits. The loop performs $d$ iterations. Both modular exponents are bounded by ten, and the modulus is fixed, so each iteration takes $O(1)$ time in the usual word-arithmetic model. Total time is $O(d)$.

The expression `b[::-1]` constructs a reversed list copy containing all $d$ digits. Consequently, the exact source uses $O(d)$ additional space, not the manifest's stated $O(1)$. The changing residues themselves use only constant space. Replacing the slice with `reversed(b)` or an index loop from `d - 1` to zero would preserve the algorithm while reducing auxiliary iteration space to $O(1)$.

Because every modular residue is below 1337, arithmetic operand size remains bounded. The original `a` is at most a 32-bit positive integer and becomes a small residue after the first place update.

## Alternatives and edge cases

- **Most-significant-digit streaming:** Process digits left to right with `ans = pow(ans, 10, mod) * pow(a, digit, mod) % mod`. Appending digit `e` changes exponent prefix $P$ to $10P+e$. This matches the manifest summary and uses $O(1)$ auxiliary space without reversing.

- **Euler or Chinese remainder analysis:** Since $1337=7\cdot191$, one can reason about exponent cycles modulo each prime factor and combine results. This is mathematically interesting but requires careful handling when the base is not coprime to 1337.

- **Convert all digits to one integer:** Python could technically hold it, but constructing and exponentiating by that giant value is unnecessary and does not generalize to fixed-width environments.

- **Ordinary `a ** B` before `% 1337`:** This attempts to materialize an astronomically large integer and is computationally impractical. Three-argument `pow` is essential.

- **A zero digit:** Its contribution is one, but the current base must still be raised to ten for the next decimal place.

- **Exponent with one digit:** The loop simply returns `pow(a, digit, 1337)` after one contribution.

- **Base divisible by 1337:** Its residue is zero. Since the exponent is positive, the final answer is zero.

- **Base one:** Every modular power is one, so the answer remains one regardless of exponent length.

- **No leading zeros:** The contract guarantees a standard positive exponent representation. Internal or trailing zero digits are fully supported.

- **Input preservation:** The slice creates a reversed copy and does not mutate `b`; the parameter variable `a` is reassigned locally without changing the caller's integer.
