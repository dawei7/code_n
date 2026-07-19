## General
**Determine the shared exponent.** Copy `n` and repeatedly apply integer division by `10`, incrementing `digits` once per extracted decimal position. This obtains the number of digits without changing the original value needed for the final comparison.

**Accumulate each digit's contribution.** Reset the working copy to `n`. Repeatedly compute `digit = remaining % 10`, add `digit ** digits` to `total`, and update `remaining //= 10`. Each decimal digit is extracted exactly once and raised to the same exponent.

When no digits remain, `total` is precisely the sum in the Armstrong definition, so `total == n` is necessary and sufficient. The computation uses the original number only for comparison and never mistakes a partial sum or truncated working copy for the target.

## Complexity detail
The arithmetic method performs two passes over the $d$ digits and uses constant scalar storage. Abstractly this is $O(d)$ time and $O(1)$ space, but the public domain fixes $d \le 9$, so runtime and space are both $O(1)$ over every valid input.

## Alternatives and edge cases
- **Decimal string:** Convert `n` to a string, use its length as $d$, and sum converted character powers; this is concise but allocates $O(d)$ string space.
- **Precomputed Armstrong set:** Membership in the finite set of Armstrong numbers under $10^8$ is constant time, but it hides the defining calculation and is less adaptable.
- **Single-digit number:** Every value from `1` through `9` is Armstrong because $x^1=x$.
- **Internal zero digits:** Zero positions contribute nothing but still count toward the exponent $d$.
- **Power exponent:** The exponent must be recomputed from the complete number; using a hard-coded cube handles only three-digit inputs.
