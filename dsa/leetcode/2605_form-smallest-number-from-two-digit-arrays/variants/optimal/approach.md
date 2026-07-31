## General

The answer never needs more than two digits. Choosing one digit from each array always produces a valid two-digit number, so any longer number would be larger.

First mark the digits present in `nums1` and scan `nums2` for shared digits. If the arrays intersect, their smallest common digit is a valid one-digit answer. Every one-digit number is smaller than every two-digit number, and choosing the smallest common digit is therefore optimal.

If there is no common digit, the answer must contain two different digits, one supplied by each array. Let $a$ and $b$ be the minimum digits in `nums1` and `nums2`. Replacing either selected digit with a larger one cannot improve the result, so an optimum must use $a$ and $b$. The only candidates are `10 * a + b` and `10 * b + a`; return the smaller one.

## Complexity detail

The source contract limits each array to a subset of the nine nonzero decimal digits. Consequently, at most eighteen entries are inspected, giving $O(1)$ time and $O(1)$ auxiliary space over the complete legal domain.

If the digit alphabet were allowed to grow, the same structure would be linear in the combined input length. The fixed ten-slot presence table does not grow with the input.

## Alternatives and edge cases

- **Pair enumeration:** Trying every digit pair is correct but unnecessary once the minimum digits and any common digit are known.
- **Set intersection:** A language-level set gives concise code with the same bounded behavior, but a ten-slot table makes the fixed digit domain explicit.
- **Several common digits:** Only the smallest common digit matters because it yields the smallest possible one-digit result.
- **No common digit:** Both digit orders must be considered; the smaller digit belongs in the tens place.
- **Singleton arrays:** Distinct singleton digits still form a valid two-digit number, while equal singleton digits produce that digit itself.
- **No zero digit:** Inputs range from $1$ through $9$, so leading-zero semantics never arise.
