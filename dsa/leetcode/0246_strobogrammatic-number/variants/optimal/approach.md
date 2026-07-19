## General
**Rotation couples mirrored positions**

Valid rotations are `0->0`, `1->1`, `6->9`, `8->8`, and `9->6`. Move pointers inward and require the rotated left digit to equal the right digit.

Before each step, every digit pair outside the pointers is known to rotate into its mirrored partner.

**Pairwise compatibility is necessary and sufficient**

A 180-degree rotation reverses position order and applies the digit mapping. Therefore every valid numeral must match each left digit with its mapped right digit. If all mirrored pairs satisfy the mapping, rotating every digit reconstructs the original string in reverse positional order, so the entire numeral is strobogrammatic.

## Complexity detail
At most half the string is examined, giving $O(n)$ time. The fixed five-pair mapping and two indices use constant space.

## Alternatives and edge cases
- **Build the rotated string:** is simple but uses $O(n)$ extra space.
- Digits `2`, `3`, `4`, `5`, and `7` are immediately invalid; a middle digit must be `0`, `1`, or `8`.
