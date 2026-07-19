## General
**Choose a nonnegative remainder:** At each step, `remainder = n & 1` selects `0` or `1` with the same parity as `n`. This ensures `n - remainder` is divisible by `-2` and makes the remainder a valid output digit.

**Advance to the next coefficient:** Append the remainder as the current least significant digit, then execute `n = (n - remainder) // -2`. The quotient may alternate sign, which is expected for a negative base. Repeat until the quotient is zero.

**Reverse the collected digits:** Division produces coefficients from $d_0$ upward, so reverse them to obtain the conventional most-significant-first string. Handle the original value zero directly because its loop would produce no digits.

Every step maintains `old_n = new_n * -2 + remainder` with a digit in `{0, 1}`. Recursively substituting these identities yields exactly the required weighted sum, and termination leaves no unrepresented quotient. The parity choice is unique, so the resulting representation is unique.

## Complexity detail
The quotient's magnitude decreases geometrically, and one step produces each of the $B$ output digits, for $O(B)$ time. The digit list contains $B$ characters and uses $O(B)$ space, including the returned representation.

## Alternatives and edge cases
- **Adjusted divmod:** Dividing by `-2` and correcting a negative remainder produces the same recurrence.
- **Greedy signed powers:** Choosing coefficients from the largest power downward is possible but requires careful reachable-range reasoning.
- **Recompute each quotient:** Deriving every digit anew from the original value is correct but repeats earlier division work and takes $O(B^2)$ time.
- **Zero:** Return `"0"` rather than an empty string.
- **Negative intermediate quotient:** It is part of the conversion and must not be treated as an invalid state.
