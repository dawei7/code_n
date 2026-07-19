## General
**Decimal place values collapse modulo nine**

Because every decimal place value is congruent to one modulo nine, an integer and the sum of its digits have the same remainder modulo nine. Repeating the operation preserves that remainder.

The final digit is congruent to `num` modulo nine. For positive inputs it lies in `1..9`, so remainder zero maps to nine; zero remains the special result zero.

**The residue identifies one positive digit**

Digit summation preserves the value modulo nine until a single digit remains. For a positive input, exactly one value in `1..9` has the same residue: residue one through eight maps directly, while residue zero maps to nine. This is expressed uniformly as `1 + (num - 1) % 9`; zero is handled separately because it never enters the positive range.

## Complexity detail
One comparison and constant-count arithmetic operations take $O(1)$ time and space.

## Alternatives and edge cases
- **Simulate digit sums:** is correct but processes digits repeatedly rather than using the number-theoretic invariant.
- Zero must not be mapped to nine; positive multiples of nine must be.
