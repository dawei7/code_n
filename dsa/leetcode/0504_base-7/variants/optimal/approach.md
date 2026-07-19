## General
**Extract digits from least significant to most significant**

For a nonnegative value, division by `7` separates its representation into a smaller prefix and one final digit. If `value = 7 * quotient + remainder`, then `remainder` is the least-significant base-7 digit and `quotient` contains every digit still to be produced. Repeating `divmod(value, 7)` until the quotient becomes zero therefore extracts all digits.

**Reverse the extraction order**

Successive remainders arrive from right to left. Store them in a list, then reverse that list once to form the usual most-significant-first string. Every step preserves the equality between the original magnitude and the already-extracted suffix plus the unprocessed quotient times the appropriate power of seven, so when the quotient reaches zero the reversed digits represent exactly the input magnitude.

**Handle sign separately from digits**

Convert `abs(num)` using the same nonnegative loop and prepend `-` only after assembling the digits. This avoids relying on language-specific division and remainder behavior for negative operands. Zero needs an explicit return because its conversion loop performs no iterations, while its representation must contain one digit.

## Complexity detail
Each division removes one base-7 digit, so there are $O(\log |num|)$ iterations for nonzero input. The digit list and returned string contain $O(\log |num|)$ characters. Zero takes constant time and space.

## Alternatives and edge cases
- **Recursive repeated division:** naturally emits the quotient before the remainder and has the same asymptotic bounds, but uses one call-stack frame per digit.
- **Built-in radix conversion:** is concise where a language supports arbitrary bases, but Python's standard integer formatter does not directly target base 7 and the exercise is intended to implement the conversion.
- **Repeated subtraction:** can find each quotient without division, but takes $O(|num|)$ total time rather than logarithmic time.
- **Zero:** must return `"0"`, not an empty string.
- **Negative input:** the minus sign is not a base-7 digit and must appear only once at the front.
- **Exact powers of seven:** produce `1` followed by zeros, so the loop must retain zero remainders.
