## General

Convert `n` to its decimal string, remove every occurrence of the character `"0"`, and convert the remaining character sequence back to an integer.

String replacement examines the digits from left to right, so all nonzero digits retain their order. Since a positive integer cannot consist only of zero digits, the filtered string is non-empty and its integer conversion is well-defined. This directly produces the requested decimal representation.

## Complexity detail

Let $D$ be the number of decimal digits in `n`. Conversion, filtering, and parsing each inspect at most $D$ characters, so time is $O(D)$. The decimal and filtered strings use $O(D)$ auxiliary space. Under the source bound $n \leq 10^{15}$, $D \leq 16$.

## Alternatives and edge cases

- **Arithmetic digit extraction:** Repeated division and remainder operations also work, but digits arrive right to left and must be reconstructed in the original order.
- **Return a string:** The contract requires an integer, so the filtered representation must be parsed.
- **No zero digits:** Filtering returns the original number unchanged.
- **Consecutive zeros:** Remove every zero in the run; no separator or placeholder remains.
- **Trailing zeros:** They disappear instead of becoming leading zeros or changing the order of earlier digits.
- **Maximum value:** `10^15` filters to `1`, demonstrating the complete legal digit-width boundary.
