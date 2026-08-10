## General

**A positive power of two has exactly one set bit**

The binary representation of $2^x$ contains one `1` followed by $x$ zeros.
For example, 1 is `0001`, 2 is `0010`, 4 is `0100`, and 8 is `1000`.
Conversely, every positive integer with exactly one `1` bit has value $2^x$,
where $x$ is that bit's zero-based position.

The problem can therefore be reduced from repeated arithmetic division to a
constant-number bit test: determine whether positive `n` has exactly one set
bit.

**Subtracting one changes the least significant set bit and everything below it**

Consider a positive binary number and locate its rightmost `1`. All bits to its
right are zero by definition. Subtracting one changes that rightmost `1` to
zero and changes all lower zeros to ones. Bits to the left remain unchanged.

For example:

`n     = 1011000`

`n - 1 = 1010111`

The rightmost set bit of `n` is cleared in `n - 1`. Lower positions are one in
`n - 1` but zero in `n`. When the two numbers are combined with bitwise AND,
all those positions become zero. Higher set bits, if any, are one in both
numbers and remain set. Thus `n & (n - 1)` clears exactly the rightmost set bit
of `n`.

**Clearing the only set bit distinguishes powers of two**

If `n` is a positive power of two, it has one set bit. Clearing that bit leaves
zero, so `(n & (n - 1)) == 0` is true.

If positive `n` is not a power of two, it has at least two set bits. The AND
operation clears the rightmost one but leaves at least one higher set bit, so
the result is nonzero. This makes the zero comparison both necessary and
sufficient for positive integers.

For `n = 16`, binary `10000` is ANDed with `01111`, producing zero. For
`n = 12`, binary `1100` is ANDed with `1011`, producing `1000`, so the method
returns false.

**Positivity is a required part of the condition**

The bit expression alone would classify zero incorrectly: `0 & (0 - 1)` is
zero, even though zero is not $2^x$ for any integer $x$. The first condition
`n > 0` excludes zero and all negative integers before applying the bit test.

Python's `and` short-circuits. When `n <= 0`, the right-hand expression is not
evaluated, and the method immediately returns `False`. This is especially clear
for negative Python integers, whose bitwise operations behave like an
unbounded two's-complement representation; the mathematical one-set-bit
characterization is intended only for positive values.

For `n = 1`, positivity holds, `n - 1` is zero, and `1 & 0` is zero. The method
correctly recognizes $2^0 = 1$.

**Why the complete boolean expression is exact**

If the method returns true, `n > 0` and clearing its rightmost set bit leaves
zero. Therefore no other set bit existed, so `n` has exactly one and equals a
power of two. If `n` is a power of two, it is positive and has exactly one set
bit, so both sides of the `and` expression are true. Every input is covered by
these two directions.

The parentheses around `n & (n - 1)` make the intended bit operation explicit
before comparison with zero. No loops, recursion, floating-point logarithms,
or repeated division are involved, satisfying the follow-up directly.

## Complexity detail

Under the problem's fixed signed 32-bit input domain, subtraction, bitwise AND,
comparison, and boolean short-circuiting each take constant time. Total time is
$O(1)$ and auxiliary space is $O(1)$.

For arbitrary-precision integers far beyond the stated domain, bit operations
technically scale with the number's machine-word length. That implementation
detail does not alter the required fixed-width complexity claim.

## Alternatives and edge cases

- **Isolate the lowest set bit:** For positive `n`, `n & -n` equals `n` exactly when `n` has one set bit. It is another constant-operation identity based on two's-complement negation.
- **Repeated division by two:** Reject nonpositive input, repeatedly divide even values by 2, and test whether the result reaches 1. It is intuitive but takes $O(\log n)$ time and does not satisfy the no-loop follow-up.
- **Count set bits:** Count ones in the binary representation and test for exactly one. Built-in or iterative counting expresses the criterion but does more work than clearing one bit.
- **Floating-point logarithm:** Test whether $\log_2 n$ is integral. Floating-point rounding near representational boundaries can cause errors, so an exact bit identity is preferable.
- **`n = 0`:** The positivity guard is essential because the bit expression by itself equals zero.
- **`n = 1`:** This is $2^0$ and is accepted even though no trailing zero bits are present.
- **Negative values:** They fail `n > 0` immediately; powers of two in this problem are positive.
- **Largest positive 32-bit power:** $2^{30}$ has one set bit and passes. $2^{31}$ lies outside the signed upper bound.
- **One more or less than a power:** Adding or subtracting one generally creates several set bits, and the AND result remains nonzero.
- **No mutation:** `n` is an immutable integer, and the expression creates only temporary numeric results.
