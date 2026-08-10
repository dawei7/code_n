## General

**A power of four has one set bit in an even bit position.**

Every nonnegative power of four can be rewritten as a power of two:

$$
4^x=(2^2)^x=2^{2x}.
$$

A positive power of two has a binary representation containing exactly one `1` bit. The exponent tells us the zero-based position of that bit. Because a power of four has exponent $2x$, its lone set bit is always at an even position: `0`, `2`, `4`, and so on.

For example:

$$
1=4^0=(1)_2
$$

has its set bit at position zero,

$$
4=4^1=(100)_2
$$

has it at position two, and

$$
16=4^2=(10000)_2
$$

has it at position four.

The exact source checks these two properties separately: first it proves `n` is a positive power of two, then it rejects the powers of two whose set bit is at an odd position.

**First require positivity.**

The expression begins with `n > 0`. Every $4^x$ relevant to an integer input is positive. A negative exponent would produce a non-integer fraction, and zero or a negative number cannot equal a power of the positive base four.

This check is also required for the one-set-bit trick. The value zero has no set bits, yet `0 & (0 - 1)` evaluates to zero in Python. Without the positivity condition, zero would be incorrectly treated as a power of two.

Python's `and` short-circuits from left to right. If `n` is nonpositive, later bit-mask expressions do not need to establish anything; the full result is immediately false.

**Use `n & (n - 1)` to demand exactly one set bit.**

Subtracting one from a positive integer changes its rightmost `1` bit to `0` and changes all lower `0` bits to `1`. Taking a bitwise AND with the original number therefore clears the original number's rightmost set bit.

If `n` had exactly one set bit, clearing it leaves zero:

$$
n\mathbin{\&}(n-1)=0.
$$

For `n = 16`, the relevant binary values are

$$
10000_2
\quad\text{and}\quad
01111_2,
$$

whose AND is zero.

If `n` has two or more set bits, clearing only the rightmost one leaves at least one other `1`, so the AND is nonzero. For `n = 5`, binary `101`, subtracting one gives `100`, and their AND is `100`, not zero.

After the positivity and zero-AND checks, `n` is known to be $2^p$ for some nonnegative integer bit position $p$. It may still be a power of two that is not a power of four, such as `2`, `8`, or `32`. The mask performs that final distinction.

**Understand the hexadecimal mask.**

The 32-bit hexadecimal value

`0xAAAAAAAA`

has the repeating binary pattern

$$
10101010101010101010101010101010_2.
$$

Reading bit positions from right to left starting at zero, this mask contains `1` at every odd position—`1`, `3`, `5`, and so on—and `0` at every even position.

The condition

`(n & 0xAAAAAAAA) == 0`

asks whether `n` has no set bit in any odd position. Because the previous test already proved that `n` has exactly one set bit, a zero result means that lone bit must occupy an even position.

For `n = 16`, the bit lies at position four, where the mask has zero, so the AND is zero and the method returns true. For `n = 8`, the bit lies at position three, where the mask has one, so the AND is nonzero and the method returns false.

The signed 32-bit contract limits positive inputs to bit positions zero through thirty. The mask covers every odd position in that range. Its highest bit, position thirty-one, is not a valid positive sign-free input position, but including it in the fixed mask is harmless.

**Why all three checks are necessary.**

The positivity check rules out zero and negative values. The one-set-bit check rules out positive numbers that are not powers of two. The alternating mask rules out odd powers of two.

None is redundant:

- zero passes the raw `n & (n - 1) == 0` equation but must be rejected;
- `5` has no odd-position set bit in the mask intersection? Its multiple bits mean the power-of-two test must reject it regardless of mask behavior;
- `8` is a valid power of two but its exponent is odd, so the mask must reject it.

**Why the method is correct.**

If $n=4^x$, then $n=2^{2x}$. It is positive, has exactly one set bit, and that bit lies at even position $2x$. All three source conditions are true.

Conversely, suppose all three source conditions are true. Positivity and the `n & (n - 1)` test imply $n=2^p$ for a nonnegative integer $p$. The mask condition implies $p$ is even, so $p=2x$ for some nonnegative integer $x$. Therefore

$$
n=2^{2x}=4^x,
$$

and `n` is a power of four. This proves both acceptance and rejection behavior.

## Complexity detail

The input is a fixed-width signed 32-bit integer. The source performs a constant number of comparisons, subtractions, and bitwise AND operations, each fixed-size. Its time complexity is $O(1)$.

It stores no collection and performs no loop or recursion. Auxiliary space complexity is $O(1)$.

The mask is a literal constant, not an array proportional to the input. This method satisfies the follow-up requirement to avoid loops and recursion.

## Alternatives and edge cases

- **Repeated division by four:** While the positive value is divisible by four, divide it by four; accept only if the result reaches one. This is exact and easy to understand, but takes $O(\log_4 n)$ time and does not meet the constant-work follow-up.

- **Power-of-two test plus modulo three:** Even powers of two satisfy $2^{2x}\bmod3=1$, while odd powers satisfy $2^{2x+1}\bmod3=2$. Thus a positive power of two is a power of four exactly when `n % 3 == 1`. It is also constant time under fixed-width arithmetic.

- **Precomputed valid set:** Only sixteen powers from $4^0$ through $4^{15}$ fit in the signed 32-bit positive range. Membership in a constant set works but hides the bit-position structure.

- **Logarithms:** Testing whether $\log_4 n$ is integral is concise, but floating-point rounding near exact powers can make equality checks fragile.

- **`n = 1`:** It is $4^0$, has one bit at even position zero, and passes all checks.

- **`n = 0`:** The first condition rejects it before the otherwise misleading one-set-bit equation can matter.

- **Negative input:** The first condition rejects it, avoiding complications from Python's infinite-sign-extension model for negative bitwise operations.

- **Power of two at an odd position:** Values such as `2`, `8`, and `32` pass the one-set-bit check but intersect the alternating mask and are correctly rejected.

- **Maximum valid power:** $4^{15}=2^{30}$ fits within the signed 32-bit maximum and has its bit at even position thirty, so it passes.
