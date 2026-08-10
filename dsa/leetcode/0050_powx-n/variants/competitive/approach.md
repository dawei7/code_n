## General

**Read the exponent one binary bit at a time**

The selected method replaces linear repeated multiplication with exponentiation by squaring. It stores the nonnegative magnitude `abs_n = abs(n)` and repeatedly examines its lowest binary bit.

At bit position $k$, local variable `x` has already been squared $k$ times and therefore represents the original base raised to $2^k$. If `abs_n & 1` is nonzero, the current low bit is 1 and that power is multiplied into `result`. A right shift then discards the processed bit, while squaring `x` prepares the power for the next position.

Although the parameter name `x` is reassigned, this is only a local variable binding. The caller passes a floating-point value, not a mutable numeric object, so no external input is modified.

**Why bit decomposition represents every exponent**

Every nonnegative integer $N$ has a unique expansion

$$
N = \sum_{k \ge 0} b_k 2^k,
$$

where each bit $b_k$ is either zero or one. Therefore,

$$
x^N = \prod_{k:b_k=1} x^{2^k}.
$$

The loop constructs exactly that product. `abs_n & 1` reads $b_k$, `result *= x` includes the corresponding factor when needed, `abs_n >>= 1` moves the next bit into the low position, and `x *= x` changes $x^{2^k}$ into $x^{2^{k+1}}$.

For exponent 10, binary `1010` selects the $2$ and $8$ powers. The loop skips the first $x^1$, includes $x^2$, skips $x^4$, and includes $x^8$, producing $x^{10}$ in four iterations.

**Why the update order is consistent**

The current low bit must be tested before `abs_n` is shifted, because that bit says whether the current squared base belongs in the product. Squaring `x` after the test prepares the next power, and shifting prepares the next bit. In this source, shifting happens immediately before squaring; those two operations are independent because one changes only the exponent variable and the other changes only the base variable. What would be wrong is squaring the base before using a set current bit, because that would multiply the power for the next position instead of the present one.

**A preservation invariant**

Let the original base be $b$ and the magnitude be $N$. At every loop start, the product of `result` and the current `x` raised to `abs_n` equals $b^N$. If the remaining exponent is even, squaring the base and halving the exponent leaves the represented power unchanged. If it is odd, multiplying one current base into `result` first accounts for the extra factor, after which square-and-halving handles the even remainder.

When `abs_n` reaches zero, the remaining power is one, so `result` alone equals $b^N$. This proves correctness for the magnitude.

**Apply the sign of the original exponent once**

The loop always works with `abs(n)`. If the original `n` was negative, the method returns `1 / result`; otherwise, it returns `result`. This implements $x^{-N}=1/x^N$ without complicating the bit loop.

The contract excludes zero with a negative or zero exponent, so valid negative-exponent inputs cannot cause division by zero. `n == 0` makes `abs_n` zero immediately, leaves `result` at 1, and returns 1.

Python can represent `abs(-2**31)` without overflow. In a 32-bit signed integer implementation, the positive magnitude of the minimum value would not fit, so conversion to a wider type would be required before negation.

**Which class is active**

The file also includes a recursive `Solution2`. The harness selects class `Solution`, which is the iterative constant-space method. `Solution2` additionally uses `/` for exponent halving, which would produce floats under Python 3 and is not the selected behavior.

## Complexity detail

Every iteration removes one binary digit from `abs_n`. A nonzero magnitude has $\lfloor\log_2 |n|\rfloor+1$ bits, so time is $O(\log |n|)$. The zero-exponent path is $O(1)$.

The iterative method stores a result, exponent magnitude, and locally squared base. It uses no recursion or proportional collection, so auxiliary space is $O(1)$. This matches the manifest. The analysis uses the problem's standard assumption that each floating-point multiplication or division is constant time.

## Alternatives and edge cases

- **Recursive divide-and-conquer:** Compute the power for half the exponent and square it. It is equally logarithmic in time but needs a logarithmic call stack.
- **Direct multiplication loop:** Multiplying by the base $|n|$ times uses constant space but linear time, failing for very large exponents.
- **Built-in `pow`:** It likely uses an efficient internal strategy but does not expose or implement the requested algorithm.
- **Zero exponent:** The `while` body is skipped and the multiplicative identity is returned.
- **Negative exponent:** Only one reciprocal is taken after computing the positive magnitude, avoiding repeated divisions.
- **Zero base with positive exponent:** Multiplications make `result` zero when a set bit is encountered, producing the correct value.
- **Minimum signed exponent:** Python's arbitrary-precision integer avoids the usual `abs(INT_MIN)` overflow trap.
- **Negative base:** Odd exponents retain a negative factor and even exponents produce a positive result through ordinary multiplication.
- **Local base mutation:** Reassigning and squaring local `x` has no effect on a caller's numeric variable.
- **Unused recursive class:** Its Python 3 division issue does not affect the canonical `Solution`, but it should not be confused with the selected implementation.
- **Floating-point rounding:** Binary exponentiation reduces the number of operations but still returns a floating-point approximation governed by normal rounding rules.
