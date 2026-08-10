## General

**Why multiplying `x` exactly `n` times is unnecessary**

The exponent may have magnitude near $2^{31}$, so a loop performing one multiplication per exponent unit is far too slow. Binary exponentiation uses the fact that repeated squaring creates large powers quickly:

$$
x,\quad x^2,\quad x^4,\quad x^8,\quad x^{16},\ldots
$$

Every nonnegative integer exponent is a sum of distinct powers of two. If the binary representation of $n$ has a 1 in a particular position, the corresponding squared power belongs in the result. The algorithm reads those binary bits from least significant to most significant.

**Meaning of the helper variables**

`qpow(a, n)` is called only with a nonnegative exponent. `ans` accumulates the powers selected by bits already processed. `a` is the base raised to the power represented by the current bit position. The local `n` contains the remaining unprocessed bits.

Initially, `a` is the original base, corresponding to $x^{2^0}$, no bits have been processed, and `ans = 1` is the multiplicative identity. If the low bit of `n` is 1, the test `n & 1` succeeds and `ans *= a` includes that power.

Then `a *= a` advances from $x^{2^k}$ to $x^{2^{k+1}}$, and `n >>= 1` removes the bit just handled. Right shifting a nonnegative integer by one is integer division by two with the remainder discarded, exactly what is needed to expose the next binary bit.

**A concrete binary trace**

For exponent 13, the binary representation is `1101`, meaning $13 = 8 + 4 + 1$. The first low bit is 1, so the algorithm includes $x$. It squares the base to $x^2$ and shifts. The next bit is 0, so $x^2$ is not included. Further squaring yields $x^4$, whose bit is 1, and then $x^8$, whose bit is also 1.

The accumulator becomes

$$
x \cdot x^4 \cdot x^8 = x^{13}.
$$

Only four iterations are needed because 13 has four binary positions, rather than thirteen direct multiplications.

**The invariant that proves correctness**

One useful invariant is that the accumulator times the current base raised to the remaining exponent always equals the originally requested nonnegative power:

$$
\texttt{ans}\cdot a^{\texttt{n}} = x^N,
$$

where $N$ is the exponent supplied to `qpow`.

If `n` is even, write it as $2k$. After squaring `a` and shifting `n` to $k$, the unprocessed factor becomes $(a^2)^k=a^{2k}$, so the invariant is preserved. If `n` is odd, write it as $2k+1$. Multiplying `ans` by `a` accounts for one factor, and the square-and-shift leaves $(a^2)^k$, again preserving the same total product.

Eventually `n` becomes zero. The unprocessed factor is then $a^0=1$, so the invariant reduces to `ans = x^N`. The helper returns the exact binary-exponentiation result, subject only to ordinary floating-point arithmetic behavior.

**Negative and zero exponents**

For `n >= 0`, the public method directly returns `qpow(x, n)`. For a negative exponent, the identity

$$
x^n = \frac{1}{x^{-n}}
$$

turns it into a positive-exponent call. The contract guarantees that zero is not raised to a nonpositive exponent, so this reciprocal does not divide by zero for valid inputs.

When `n == 0`, the helper loop does not run and returns `ans = 1`, which is the standard value of a nonzero number to the zero power. Python integers have arbitrary precision, so negating the minimum 32-bit exponent does not overflow; this is a concern in fixed-width languages but not in this source.

## Complexity detail

Each loop iteration shifts the nonnegative exponent right by one, halving it. The number of iterations is the number of bits in $|n|$, which is $O(\log |n|)$ for nonzero `n`; the zero case is constant time. Every iteration performs only constant-time arithmetic at the algorithmic model used by the problem.

The helper stores `ans`, `a`, and its local exponent. It is iterative and allocates no recursion stack or size-dependent collection, so auxiliary space is $O(1)$. These bounds match the manifest. Floating-point multiplication cost is treated as constant under the problem's numeric model.

## Alternatives and edge cases

- **Recursive exponentiation by squaring:** Compute the half power once, square it, and multiply by `x` for an odd exponent. It has the same time bound but uses $O(\log |n|)$ call-stack space.
- **Naive repeated multiplication:** It is simple but takes $O(|n|)$ time, which is infeasible for the maximum exponent.
- **Built-in power operator:** `x ** n` is concise but bypasses the requested implementation exercise and hides the binary process.
- **Exponent zero:** The untouched multiplicative identity 1 is returned.
- **Negative exponent:** The source computes the positive magnitude first and takes exactly one reciprocal at the end.
- **Minimum 32-bit exponent:** Python safely evaluates `-n` beyond signed 32-bit range. A fixed-width implementation must widen before negation.
- **Base zero:** Valid inputs allow it only with positive `n`, for which repeated squaring correctly returns zero.
- **Base one or negative one:** Squaring quickly stabilizes at one, while selected odd bits preserve the appropriate sign.
- **Negative base:** The parity of selected exponent bits naturally determines the sign; no special branch is needed.
- **Floating-point precision:** The algorithm minimizes multiplication count asymptotically but cannot eliminate ordinary rounding in floating-point operations.
