## General

Preserve the original value because digit extraction will consume a working copy. Repeatedly apply `divmod(n, 10)`: the remainder is the current least-significant decimal digit, and the quotient removes it. Add that digit to a running sum and multiply it into a running product.

After the working value becomes zero, every decimal digit has contributed exactly once to both accumulators. Their sum is therefore precisely the divisor defined by the problem. Test whether dividing the preserved original value by this divisor leaves remainder zero. Because the input is positive, its digit sum is positive, so the divisor cannot be zero even when a zero digit makes the product zero.

## Complexity detail

If `n` has $d=\lfloor\log_{10}n\rfloor+1$ decimal digits, the loop performs one constant amount of work per digit. The time complexity is $O(d)=O(\log n)$, and the few integer accumulators require $O(1)$ auxiliary space.

The legal input has at most seven decimal digits. That bounded domain is too small for trustworthy fourfold runtime scaling in $d$, so the package uses a bounded-domain work proof and boundary cases instead of a measured scaling verdict.

## Alternatives and edge cases

- **Convert to a string:** Iterating over decimal characters is also linear in the digit count but allocates a representation proportional to that count.
- **Single-digit values:** The sum and product both equal the digit, making their total twice `n`; therefore no legal one-digit input passes.
- **A zero digit:** The complete digit product becomes zero, but the digit sum remains positive and solely determines the divisor.
- **Several zero digits:** Each still contributes zero to the sum and keeps the product at zero; all positions must nevertheless be processed.
- **Maximum input:** `1000000` has seven digits and is valid because its sum is 1 and its product is zero.
- **Preserve `n`:** The extraction loop reduces its working copy to zero, so the original is needed for the final modulus.
