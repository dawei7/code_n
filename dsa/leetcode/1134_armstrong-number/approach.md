## General

**The exponent is the decimal digit count**

An Armstrong test uses one shared exponent $k$, equal to the number of digits in the original number. The code computes it once with `len(str(n))`.

The input is positive, so its ordinary string has only decimal digits and no minus sign. There is no special zero representation to handle under the stated range.

Computing `k` before consuming digits is essential. If digit count were recomputed from the shrinking `x`, later digits would receive smaller exponents and the sum would no longer match the definition.

**Keep the original value intact**

Variable `x` is a disposable copy used for digit extraction, while `n` remains unchanged for the final comparison.

This separation is necessary because repeatedly dividing the working number eventually turns it into zero. Comparing the sum with that destroyed working copy would be meaningless.

**Extract digits arithmetically**

While `x` is nonzero, `x % 10` yields the current rightmost decimal digit. Raising it to power `k` gives that digit’s Armstrong contribution.

The contribution is added to `s`, and `x //= 10` removes the processed rightmost digit.

For 153, the loop processes three, five, and one. The order is reversed from written notation, but addition is commutative, so:

$3^3+5^3+1^3$

equals the required sum.

**Why every digit contributes once**

Before each iteration, `x` contains exactly the unprocessed leading portion of the original number and `s` contains powered contributions from all removed trailing digits.

Modulo selects the last unprocessed digit, and floor division removes exactly that digit. The invariant continues until `x = 0`, when no digits remain.

Repeated digits are processed in separate iterations. A zero digit contributes `0 ** k`, which is zero, but division still advances past its decimal position.

For a number such as 100, $k=3$. The two zero positions each add zero, and the leading one adds one. The sum is one, so 100 is correctly rejected. Zeros do not reduce the exponent because they still occupy decimal positions.

**Return exact equality**

After processing all $k$ digits, `s` equals $\sum d_i^k$. The method returns `s == n`, true exactly when the definition holds.

There is no tolerance or approximate arithmetic. All powers and sums are integer operations.

**Examples of the century-style digit logic**

For 153, `k = 3` and the powered sum is 153, so the result is true. For 123, the sum is one plus eight plus twenty-seven, or 36, so equality fails.

A one-digit positive number always satisfies the property because $d^1=d$. The loop naturally returns true for values one through nine.

Not every multi-digit number fails. Values such as 370, 371, and 407 satisfy the cubic rule. The method needs no catalog of known values because it evaluates the definition directly.

## Complexity detail

The repository playbook classifies this as bounded-domain complexity. The legal maximum `10^8` has nine decimal digits, so string conversion, digit extraction, and power accumulation perform a fixed bounded amount of work.

Under that source domain, time and space are $O(1)$, matching the manifest.

The bound is constant because at most nine iterations are legal, not because the loop is independent of digit count in a generalized mathematical sense.

For a generalized $k$-digit integer, the loop has $k$ iterations and string conversion also processes $k$ digits, giving $O(k)$ high-level time. The exact bit complexity of exponentiation depends on integer sizes, but source bounds keep every value fixed.

Only a few integers and a temporary decimal string of at most nine characters are used, so legal-domain storage is constant.

Each exponentiation uses a digit from zero through nine and exponent at most nine, so powered values are themselves bounded under the source contract. The accumulated sum remains an ordinary finite integer.

The original input need not be copied as a string for the whole loop; the string exists only to determine length, while arithmetic extraction keeps additional state constant.

## Alternatives and edge cases

- **String digit iteration:** Convert once, set `k` to its length, and sum `int(c) ** k` for each character. It is concise but uses textual conversion for extraction too.
- **Logarithm for digit count:** `floor(log10(n)) + 1` works for positive inputs but introduces floating-point boundary concerns.
- **Arithmetic digit-count loop:** Divide a second copy to count digits, then another copy to sum powers. It avoids strings but makes two arithmetic passes.
- **One-digit number:** Every legal one-digit positive value is Armstrong.
- **Digit zero inside the number:** It contributes zero and remains a real digit in $k$.
- **Repeated digits:** Every occurrence contributes separately.
- **Power shared across digits:** The exponent is total digit count, not the digit’s position or value.
- **Maximum input:** `10^8` has nine digits and stays within the bounded certificate domain.
- **Original preservation:** `n` must remain intact while `x` is consumed.
- **Integer arithmetic:** No rounding or tolerance is involved.
- **Positive-input guarantee:** The loop runs at least once and no sign character affects digit count.
- **Generalized zero:** Outside this positive domain, zero would need deliberate handling because the while loop would skip it.
