## General

**Read digits in the same direction as the sign rule**

The most significant digit must be positive, the next negative, and signs continue alternating.

Converting `n` to `str(n)` lists decimal digits from most significant to least significant. `enumerate` assigns index zero to the first digit, index one to the second, and so on.

Thus index parity directly determines the required sign:

- even index: positive;
- odd index: negative.

**Generate the alternating sign**

The factor

`(-1)**i`

equals one when `i` is even and negative one when `i` is odd:

$$
(-1)^0=1,\quad
(-1)^1=-1,\quad
(-1)^2=1,\ldots
$$

Multiplying this factor by digit `int(x)` gives the digit with its prescribed sign.

The generator expression produces those signed values, and `sum` adds them.

**Trace `n=521`**

`str(521)` is `"521"`. Enumeration yields:

- index 0, digit 5: $(-1)^0\cdot5=+5$;
- index 1, digit 2: $(-1)^1\cdot2=-2$;
- index 2, digit 1: $(-1)^2\cdot1=+1$.

The sum is $5-2+1=4$.

**Why the first sign is always correct**

The input is a positive integer. Its string representation has no leading sign character and no leading zeroes. Character at index zero is exactly the most significant decimal digit.

Starting exponent at zero therefore assigns it positive one. No adjustment based on total digit count is needed.

**Odd and even digit counts**

If the number has an odd number of digits, the final digit has even index and receives a positive sign. If it has an even number, the final index is odd and receives a negative sign.

The generator handles both cases automatically.

**Single-digit number**

Enumeration has only index zero. The only digit is most significant and receives positive sign, so the function returns the number itself.

This matches the rule without a special branch.

**Difference from right-to-left extraction**

The manifest summary describes extracting digits from right to left with a recurrence. The protected source does not do that. It converts to a string and scans left to right.

A right-to-left arithmetic method must account for whether the total digit count is odd or use a recurrence that effectively prepends digits. The string method avoids that complexity because it begins at the required positive endpoint.

**Why `sum` and the generator are sufficient**

Every decimal position appears once in the string and once in enumeration. Its sign is a deterministic function of index parity. There is no interaction between digits, carrying, or place value; the task asks for digit values, not the numeric value they form.

The generator is lazy, so signed terms are passed to `sum` one at a time rather than stored in a list.


After consuming positions zero through `i`, the running sum equals the required signed sum of exactly that prefix of digits. The next factor is opposite the prior factor because multiplying $(-1)^i$ by another $-1$ flips sign.

Starting from the correctly positive first digit and extending through every position proves the final sum is exact.

**Input immutability**

The integer `n` is not modified. A decimal string is created as a separate representation.

The maximum $10^9$ has ten digits, but the reasoning works for any positive decimal integer.

**A longer cancellation trace**

For `886996`, indexed contributions are:

$$
+8,\ -8,\ +6,\ -9,\ +9,\ -6.
$$

The first two cancel, the middle $+6$ cancels the final $-6$, and $-9$ cancels $+9$, giving zero. The calculation illustrates that signs depend only on positions, not on whether neighboring digit values happen to match.

**Why exponentiation is harmless here**

Although `(-1)**i` uses exponentiation syntax, the base is fixed and the exponent is at most nine under the constraints. It simply selects one of two values. An explicit sign flip could avoid exponentiation, but it would not change the asymptotic work or result.

Character-to-integer conversion is also exact for each one-character decimal string.

## Complexity detail

Let $d$ be the number of decimal digits. Converting `n` to a string and scanning it both cost $O(d)$ time.

The decimal string itself occupies $O(d)$ space. The generator uses constant incremental state. Therefore, exact auxiliary space is $O(d)$, not the manifest's $O(1)$ arithmetic-extraction claim.

Under the constraints, $d\le10$.

## Alternatives and edge cases

- **Arithmetic right-to-left recurrence:** Repeatedly extract a digit and update `answer=digit-answer`; it can use $O(1)$ space.
- **Explicit sign variable:** Start at one and multiply it by $-1$ after every digit.
- **Single digit:** Return it positively.
- **Even number of digits:** The least significant digit is negative.
- **Odd number of digits:** The least significant digit is positive.
- **Result zero:** Opposite signed contributions may cancel completely.
- **Positive input:** There is no minus-sign character to skip.
- **No leading zeroes:** Index zero is the true most significant digit.
- **Generator scope:** Terms are not materialized as a list.
- **Manifest mismatch:** The exact implementation allocates and scans a string.
